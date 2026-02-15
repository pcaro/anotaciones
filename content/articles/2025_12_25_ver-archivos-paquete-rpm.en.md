---
title: How to View Files in an RPM Package on Linux
date: 2025-12-25 15:15
tags: linux, rpm, packages, commands, systems, administration, dnf, yum
lang: en
category: Systems
slug: ver-archivos-paquete-rpm
summary: Quick guide to inspecting the contents of RPM packages and determining which packages own specific files on your Linux system.
---

On RPM-based Linux systems (like Red Hat, CentOS, Fedora, openSUSE), it is common to interact with packages in `.rpm` format. Often, we need to know what files a package contains before installing it, or which package is responsible for a specific file already installed on the system. For this, the `rpm` tool offers several useful options.

## 1. List Files of an RPM Package Without Installing

If you have a downloaded `.rpm` file and want to see what files it will install (and where) without installing it, you can use the `-qlp` option:

```bash
rpm -qlp package_name.rpm
```

*   `-q`: Query mode.
*   `-l`: List files.
*   `-p`: Query a package file instead of an installed one.

**Example:**

```bash
rpm -qlp nginx-1.20.1-1.el8.x86_64.rpm
```

## 2. Find the Owner Package of an Installed File

If you find a file on your system and want to know which RPM package it belongs to (useful for debugging or knowing if you can safely delete it), use the `-qf` option:

```bash
rpm -qf /path/to/file
```

**Example:**

```bash
rpm -qf /etc/nginx/nginx.conf
# Expected output: nginx-1.20.1-1.el8.x86_64
```

## 3. Get Detailed Information about a Package

To see complete information about a package (version, description, dependencies, etc.), whether installed or an `.rpm` file, you can use `-qi` (for installed packages) or `-qip` (for package files):

```bash
rpm -qi installed_package_name
# Example: rpm -qi nginx

rpm -qip package_name.rpm
# Example: rpm -qip nginx-1.20.1-1.el8.x86_64.rpm
```

## Conclusion

Mastering these simple options of the `rpm` command gives you much greater control over packages and files on your Linux system, facilitating administration and debugging. They are essential tools for any system administrator or developer working with RPM-based distributions.

*Original article*: [Cómo Ver los Archivos de un Paquete RPM o Deb](https://comulinux.blogspot.com/2010/04/como-ver-los-archivos-de-un-paquete-rpm.html)
