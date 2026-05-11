Title: Configurar permisos udev para Vial en Linux
Date: 2026-05-11
Tags: vial, linux, udev, keyboard, keychron, qmk
Slug: vial-linux-udev
Lang: es
Featured_image: /images/vial-linux-udev.png
Summary: Cómo configurar reglas udev para que Vial detecte tu teclado con firmware Vial en Linux, usando la regla universal basada en el serial mágico.
Category: Linux

Al conectar un teclado con firmware Vial (como el Keychron Q10) en Linux, la GUI de Vial no lo detecta porque el usuario no tiene permisos sobre los dispositivos `/dev/hidraw*`.

La documentación oficial de Vial recomienda usar una **regla udev universal** que identifica el teclado por su serial mágico `vial:f64c2b3c`. Esto es mejor que usar vendor/product ID porque funciona con cualquier teclado Vial que conectes.

Primero, identifica tu teclado con `lsusb`. El mío aparece como:

```
Bus 003 Device 015: ID 3434:01a1 Keychron Keychron Q10
```

![Vial udev rules on Linux](/images/vial-linux-udev.png)

El comando para crear la regla, recargar y aplicar:

```bash
export USER_GID=`id -g`; sudo --preserve-env=USER_GID sh -c 'echo "KERNEL==\"hidraw*\", SUBSYSTEM==\"hidraw\", ATTRS{serial}==\"*vial:f64c2b3c*\", MODE=\"0660\", GROUP=\"$USER_GID\", TAG+=\"uaccess\", TAG+=\"udev-acl\"" > /etc/udev/rules.d/59-vial.rules && udevadm control --reload && udevadm trigger'
```

Esto crea `/etc/udev/rules.d/59-vial.rules`, recarga las reglas y las dispara. Después, desconecta y vuelve a conectar el teclado. Vial debería reconocerlo al instante.

Si prefieres una regla específica para tu modelo, añade los IDs:

```bash
export USER_GID=`id -g`; sudo --preserve-env=USER_GID sh -c 'echo "KERNEL==\"hidraw*\", SUBSYSTEM==\"hidraw\", ATTRS{serial}==\"*vial:f64c2b3c*\", ATTRS{idVendor}==\"3434\", ATTRS{idProduct}==\"01a1\", MODE=\"0660\", GROUP=\"$USER_GID\", TAG+=\"uaccess\", TAG+=\"udev-acl\"" > /etc/udev/rules.d/59-vial.rules && udevadm control --reload && udevadm trigger'
```

La regla universal es más simple y cubre cualquier teclado Vial futuro.

_Fuente original_: [Vial - Configuring udev on Linux](https://get.vial.today/manual/linux-udev.html)
