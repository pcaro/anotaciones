---
title: Ampliar disco de VM Aurora en Unraid y redimensionar particiones
slug: ampliar-disco-vm-aurora-unraid
date: 2026-04-24
category: Linux
tags: [aurora, linux, unraid, vm, btrfs, disco]
lang: es
summary: Cómo expandir el disco virtual de una VM Aurora ejecutándose en Unraid y redimensionar las particiones Btrfs dentro del sistema operativo.
featured_image: /images/ampliar-disco-vm-aurora-unraid.png
---

# Ampliar disco de VM Aurora en Unraid y redimensionar particiones

Me quedé sin espacio en mi prueba de la distribución **Aurora Linux**. Como la ejecuto en una VM en mi NAS Unraid, simplemente aumenté el disco virtual y luego redimensioné las particiones dentro del sistema.

Esta es una distribución basada en **Fedora Kinoite** (imágenes OSTree/bootc) del proyecto Universal Blue, que usa un sistema de archivos **Btrfs** con subvolúmenes.

## Situación inicial del disco

Antes de la expansión, el disco tenía aproximadamente **15GB** y la partición principal estaba al límite:

![Diagrama de expansión del disco - antes y después](/images/ampliar-disco-vm-aurora-unraid.png)

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
vda    253:0    0   60G  0 disk 
├─vda1 253:1    0  600M  0 part /boot/efi
├─vda2 253:2    0    2G  0 part /boot
└─vda3 253:3    0 12,4G  0 part /var/home, /var, /etc...
```

El filesystem Btrfs mostraba:

```
Device size:         12.41GiB
Device unallocated:    1.00MiB
Free (estimated):    512.12MiB (min: 512.12MiB)
Usage:               93%
```

## Paso 1: Expandir el disco en Unraid

Desde la terminal de Unraid, con la VM apagada:

```bash
# Apagar la VM
virsh shutdown Aurora

# Expandir el disco a 60GB (triplicando el tamaño original)
qemu-img resize -f raw /mnt/user/domains/Aurora/vdisk1.img 60G

# Verificar el nuevo tamaño
ls -lh /mnt/user/domains/Aurora/vdisk1.img
qemu-img info /mnt/user/domains/Aurora/vdisk1.img

# Encender la VM
virsh start Aurora
```

## Paso 2: Instalar growpart en Aurora

Aurora es un sistema inmutable basado en OSTree, así que necesité instalar la herramienta `growpart` usando `rpm-ostree`:

```bash
# Instalar cloud-utils-growpart
sudo rpm-ostree install cloud-utils-growpart

# Reiniciar (requerido después de rpm-ostree install)
systemctl reboot
```

## Paso 3: Expandir la partición

Una vez reiniciado el sistema, expandí la partición 3 para ocupar todo el espacio del disco:

```bash
# Expandir la partición 3 del disco /dev/vda
sudo growpart /dev/vda 3
```

Output:
```
CHANGED: partition=3 start=5425152 old: size=26030080 end=31455231 new: size=120403935 end=125829086
```

## Paso 4: Redimensionar el filesystem Btrfs

Aurora usa una estructura especial con múltiples subvolúmenes Btrfs:
- `root` (ID 256) - sistema base (montado read-only en /sysroot)
- `home` (ID 257) - directorios de usuario
- `var` (ID 258) - variables del sistema

El truco está en que `/sysroot` está montado como **read-only** (por ser OSTree inmutable), pero puedo hacer el resize desde cualquier mount point con escritura del mismo filesystem Btrfs:

```bash
# Redimensionar desde /var (que tiene escritura)
sudo btrfs filesystem resize max /var
```

Output:
```
Resize device id 1 (/dev/vda3) from 12.41GiB to max
```

## Resultado final

Después del redimensionamiento, el filesystem Btrfs muestra:

```
Device size:         57.41GiB    ← Antes era 12.41GiB ✓
Device unallocated:  45.00GiB    ← Espacio disponible
Device slack:          3.50KiB   ← Antes era 45.00GiB ✓
Free (estimated):    45.50GiB    ← Espacio libre para usar
Usage:               ~20%        ← Antes estaba al 93%
```

Verificando con `lsblk`:

```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
vda    253:0    0   60G  0 disk 
├─vda1 253:1    0  600M  0 part /boot/efi
├─vda2 253:2    0    2G  0 part /boot
└─vda3 253:3    0 57,4G  0 part /var/home, /var, /etc...
```

## Resumen de comandos

```bash
# === EN UNRAID (VM apagada) ===
qemu-img resize -f raw /mnt/user/domains/Aurora/vdisk1.img 60G

# === EN AURORA ===
sudo rpm-ostree install cloud-utils-growpart
systemctl reboot
sudo growpart /dev/vda 3
sudo btrfs filesystem resize max /var

# === VERIFICAR ===
lsblk
df -h /var
df -h /var/home
df -h /etc
sudo btrfs filesystem usage /var
```

## Notas importantes

1. **Sistemas OSTree**: En distribuciones inmutables como Aurora, el sistema base es read-only. El resize debe hacerse desde un subvolumen con escritura (`/var`, `/etc`, o `/var/home`).

2. **Btrfs dinámico**: El espacio en Btrfs se asigna dinámicamente a los subvolúmenes según necesidad. No es necesario asignar espacio específico a cada subvolumen.

3. **Reinicio requerido**: Después de `rpm-ostree install`, siempre hay que reiniciar para que los cambios surtan efecto.

4. **Backup**: Aunque el proceso es seguro, siempre es recomendable tener backup antes de operar sobre particiones. En mi caso no hizo falta por no tener nada importante. Es una VM de prueba.
