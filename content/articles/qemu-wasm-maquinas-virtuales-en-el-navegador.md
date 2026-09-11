Title: qemu-wasm: máquinas virtuales completas dentro del navegador
Date: 2026-09-11
Tags: webassembly, qemu, navegador, nix, maquinas-virtuales, github-actions
Slug: qemu-wasm-maquinas-virtuales-en-el-navegador
Lang: es
Featured_image: /images/trynix-qemu-wasm.png
Summary: qemu-wasm porta QEMU a WebAssembly para arrancar una máquina virtual x86_64 entera dentro del navegador. trynix.dev lo lleva al límite ejecutando cualquier paquete de nixpkgs de los últimos 13 años, y una GitHub Action arranca la build de un PR con un solo enlace.
Category: Herramientas

![trynix.dev ejecutando una máquina virtual en el navegador](/images/trynix-qemu-wasm.png)

Cada cierto tiempo algo me recuerda lo lejos que han llegado los navegadores. Hoy toca: una máquina virtual x86_64 completa, arrancando dentro de una pestaña, sin servidor detrás.

[qemu-wasm](https://github.com/ktock/qemu-wasm) es un QEMU parcheado para que corra en el navegador. No es una reimplementación ni un juguete: es QEMU compilado a WebAssembly, con traducción binaria JIT (TCG) y soporte de múltiples hilos. El mismo QEMU que usas en tu máquina, corriendo en una pestaña.

## Cómo funciona

QEMU tiene varios backends para ejecutar código de invitado. El más rápido es TCG, que traduce el binario del invitado a código nativo de la máquina host. Aquí el "host" es WebAssembly, así que el proyecto añade un backend de TCG que traduce el IR de QEMU a Wasm.

WebAssembly no permite saltar a código generado en memoria, así que en su lugar se apoyan en las APIs del navegador (`WebAssembly.Module` y `WebAssembly.Instance`). Cada bloque de traducción (TB) se compila como un módulo Wasm independiente que importa la memoria y las funciones helper del módulo principal de QEMU.

El problema: compilar todos los bloques a Wasm es caro, y los navegadores no aguantan crear miles de módulos. La solución es híbrida. Los bloques fríos se interpretan (TCI, el intérprete lento) y solo los bloques que se ejecutan muchas veces (~1000) se compilan a Wasm.

Es software experimental, pero funciona. Hay una [demo](https://ktock.github.io/qemu-wasm-demo/) con invitados x86_64, aarch64 (emula hasta una Raspberry Pi) y riscv64. Y parte de esto se está subiendo a QEMU upstream: el modo intérprete (TCI) para invitados de 32 bits ya entró en QEMU 10.1, y el resto sigue en discusión.

## El caso de uso que me ha volado la cabeza: trynix.dev

Conocer el motor está bien, pero lo que me parece brutal es el uso que le ha dado [Farid Zakaria](https://fzakaria.com/): [trynix.dev](https://trynix.dev).

La idea: arrancar una VM Linux x86_64 en tu pestaña y darle un store de Nix como sistema de archivos. El resultado es que puedes ejecutar **cualquier paquete de nixpkgs de los últimos 13 años** — más de 310.000 versiones — sin instalar nada en tu máquina.

Y son URL-addressable. Prueba esto:

```text
https://trynix.dev/?pkg=python3%403.6.2
```

Pulsa **Boot** y tienes una shell interactiva contra una máquina virtual que ejecuta Python 3.6.2 de 2017. Nada corre en un servidor: la página es estática, el kernel es WebAssembly y la closure del paquete se descarga de cache.nixos.org (que sirve `access-control-allow-origin: *`, cosa que hace posible todo esto).

Incluso puedes arrancar dos versiones de `hello` a la vez sin que choquen, porque en Nix cada binario referencia sus dependencias por ruta absoluta:

```text
https://trynix.dev/?pkg=hello@2.10&pkg=hello@2.12.2
```

Para que se sienta instantáneo, el sitio pre-carga el motor y un snapshot de la VM en segundo plano, y nunca arranca desde cero: reanuda una máquina que ya fue arrancada una vez con el QEMU nativo y pausada justo antes de montar el store.

## La acción de GitHub: revisar un PR arrancándolo

La parte más aplicada es [trynix-preview](https://github.com/marketplace/actions/trynix-preview), una GitHub Action que comenta en cada pull request un enlace para arrancar la build del PR en el navegador. Sin servidores, sin SSH, sin clonar, sin compilar. Solo un enlace.

```yaml
# Setup Cachix como caché de Nix.
- uses: cachix/cachix-action@v17
  with:
    name: sqlelf
    authToken: ${{ secrets.CACHIX_AUTH_TOKEN }}
# Construimos el código del PR y lo subimos a la caché.
- run: nix build .#default
- uses: fzakaria/trynix@v1
  with:
    cache: https://sqlelf.cachix.org
    publicKey: sqlelf.cachix.org-1:MLnjolA9AsKscTOJKDSA+ZAcgIK8BwZA574j4+Cs2bg=
    attrs: .#default
```

Ojo a dos detalles: la acción no construye ni cachea nada — tú ya tienes que haber llenado la caché — y como el workflow corre sobre PRs de forks, conviene usar una caché segregada y `allow-unsafe-pr-checkout: true`.

## Limitaciones

No todo es magia:

- Los binarios grandes son lentos: pueden tardar 1-2 minutos en ejecutarse. Hay una [página de benchmarks](https://trynix.dev/bench/) con datos.
- La closure entera tiene que caber en la memoria de la pestaña (~1.5 GiB de tope, y WebAssembly limita a 4 GiB por ser de 32 bits).
- La primera ejecución de un binario es lenta porque hay que traducir de x86_64 a Wasm; las siguientes van más rápido porque se cachea en memoria.

Aun así, como flujo de trabajo para binarios pequeños y medianos es impresionante. "¿Esto arregla el bug?" deja de ser un experimento mental.

*Fuente original*: [Simon Willison - Any Nix package, live in your browser](https://simonwillison.net/2026/Sep/10/trynix/)
