---
title: Cómo ver los archivos de un paquete RPM en Linux
date: 2025-12-25 15:15
tags: linux, rpm, paquetes, comandos, sistemas, administración, dnf, yum
lang: es
category: Sistemas
slug: ver-archivos-paquete-rpm
summary: Guía rápida para inspeccionar el contenido de paquetes RPM y determinar qué paquetes poseen determinados archivos en tu sistema Linux.
---

En sistemas Linux basados en RPM (como Red Hat, CentOS, Fedora, openSUSE), es común interactuar con paquetes en formato `.rpm`. A menudo, necesitamos saber qué archivos contiene un paquete antes de instalarlo, o qué paquete es el responsable de un archivo específico ya instalado en el sistema. Para ello, la herramienta `rpm` nos ofrece varias opciones útiles.

## 1. Listar Archivos de un Paquete RPM sin Instalar

Si tienes un archivo `.rpm` descargado y quieres ver qué archivos instalará (y dónde) sin necesidad de instalarlo, puedes usar la opción `-qlp`:

```bash
rpm -qlp nombre_del_paquete.rpm
```

*   `-q`: Modo de consulta (query).
*   `-l`: Lista los archivos (list files).
*   `-p`: Consulta un paquete (package file) en lugar de uno instalado.

**Ejemplo:**

```bash
rpm -qlp nginx-1.20.1-1.el8.x86_64.rpm
```

## 2. Encontrar el Paquete Dueño de un Archivo Instalado

Si encuentras un archivo en tu sistema y quieres saber a qué paquete RPM pertenece (útil para depuración o para saber si puedes borrarlo de forma segura), usa la opción `-qf`:

```bash
rpm -qf /ruta/al/archivo
```

**Ejemplo:**

```bash
rpm -qf /etc/nginx/nginx.conf
# Salida esperada: nginx-1.20.1-1.el8.x86_64
```

## 3. Obtener Información Detallada de un Paquete

Para ver información completa sobre un paquete (versión, descripción, dependencias, etc.), ya sea instalado o un archivo `.rpm`, puedes usar `-qi` (para paquetes instalados) o `-qip` (para archivos de paquete):

```bash
rpm -qi nombre_del_paquete_instalado
# Ejemplo: rpm -qi nginx

rpm -qip nombre_del_paquete.rpm
# Ejemplo: rpm -qip nginx-1.20.1-1.el8.x86_64.rpm
```

## Conclusión

Dominar estas sencillas opciones del comando `rpm` te proporciona un control mucho mayor sobre los paquetes y archivos de tu sistema Linux, facilitando la administración y la depuración. Son herramientas esenciales para cualquier administrador de sistemas o desarrollador que trabaje con distribuciones basadas en RPM.

*Artículo original*: [Cómo Ver los Archivos de un Paquete RPM o Deb](https://comulinux.blogspot.com/2010/04/como-ver-los-archivos-de-un-paquete-rpm.html)
