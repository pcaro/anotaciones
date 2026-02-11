Gestionando instalaciones desde GitHub con gah
##############################################

:date: 2026-02-11 20:23
:tags: linux, herramientas, cli
:lang: es
:category: Linux
:slug: gestionando-instalaciones-desde-github-con-gah
:summary: Instala binarios directamente desde releases de GitHub de forma sencilla con gah.
:status: published

`gah <https://github.com/get-gah/gah>`_ es una herramienta que facilita la instalación de programas que distribuyen sus binarios a través de releases de GitHub. Es una alternativa ligera cuando no quieres depender del gestor de paquetes de tu distribución o cuando necesitas una versión más reciente.

Instalación
-----------

Para instalar **gah**, puedes usar el siguiente script oficial:

.. code-block:: bash

    bash -c "$(curl -fsSL https://raw.githubusercontent.com/get-gah/gah/refs/heads/master/tools/install.sh)"

Uso
---

Una vez instalado, usarlo es muy directo. Aquí tienes un par de ejemplos que he usado recientemente para instalar herramientas populares escritas en Rust:

Para instalar `fd` (una alternativa rápida a ``find``):

.. code-block:: bash

    gah install sharkdp/fd

Para instalar `ripgrep` (una alternativa rápida a ``grep``):

.. code-block:: bash

    gah install BurntSushi/ripgrep

Gah se encarga de descargar el asset correcto para tu arquitectura, descomprimirlo y colocarlo en tu path.
