Title: Configuring udev permissions for Vial on Linux
Date: 2026-05-11
Tags: vial, linux, udev, keyboard, keychron, qmk
Slug: vial-linux-udev
Lang: en
Featured_image: /images/vial-linux-udev.png
Summary: How to set up udev rules so Vial can detect your Vial-firmware keyboard on Linux, using the universal magic serial rule.
Category: Linux

When you plug in a Vial-firmware keyboard (like a Keychron Q10) on Linux, the Vial GUI won't detect it because your user lacks permissions on `/dev/hidraw*` devices.

Vial's official docs recommend a **universal udev rule** that identifies the keyboard by its magic serial `vial:f64c2b3c`. This beats vendor/product ID rules because it works with any Vial keyboard you connect.

First, find your keyboard with `lsusb`. Mine shows up as:

```
Bus 003 Device 015: ID 3434:01a1 Keychron Keychron Q10
```

![Vial udev rules on Linux](/images/vial-linux-udev.png)

The one-liner to create the rule, reload and trigger:

```bash
export USER_GID=`id -g`; sudo --preserve-env=USER_GID sh -c 'echo "KERNEL==\"hidraw*\", SUBSYSTEM==\"hidraw\", ATTRS{serial}==\"*vial:f64c2b3c*\", MODE=\"0660\", GROUP=\"$USER_GID\", TAG+=\"uaccess\", TAG+=\"udev-acl\"" > /etc/udev/rules.d/59-vial.rules && udevadm control --reload && udevadm trigger'
```

This creates `/etc/udev/rules.d/59-vial.rules`, reloads the rules and applies them. Then unplug and replug your keyboard. Vial should recognize it right away.

If you prefer a model-specific rule, add the IDs:

```bash
export USER_GID=`id -g`; sudo --preserve-env=USER_GID sh -c 'echo "KERNEL==\"hidraw*\", SUBSYSTEM==\"hidraw\", ATTRS{serial}==\"*vial:f64c2b3c*\", ATTRS{idVendor}==\"3434\", ATTRS{idProduct}==\"01a1\", MODE=\"0660\", GROUP=\"$USER_GID\", TAG+=\"uaccess\", TAG+=\"udev-acl\"" > /etc/udev/rules.d/59-vial.rules && udevadm control --reload && udevadm trigger'
```

The universal rule is simpler and covers any future Vial keyboards.

_Source_: [Vial - Configuring udev on Linux](https://get.vial.today/manual/linux-udev.html)
