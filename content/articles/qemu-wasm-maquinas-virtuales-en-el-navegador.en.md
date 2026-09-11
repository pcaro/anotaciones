Title: qemu-wasm: full virtual machines inside your browser
Date: 2026-09-11
Tags: webassembly, qemu, browser, nix, virtual-machines, github-actions
Slug: qemu-wasm-maquinas-virtuales-en-el-navegador
Lang: en
Featured_image: /images/trynix-qemu-wasm.png
Summary: qemu-wasm ports QEMU to WebAssembly to boot a full x86_64 virtual machine inside the browser. trynix.dev runs any nixpkgs package from the last 13 years, and a GitHub Action boots a PR's build from a single link.
Category: Tools

![trynix.dev running a virtual machine in the browser](/images/trynix-qemu-wasm.png)

Every once in a while something reminds me how far browsers have come. Today: a full x86_64 virtual machine, booting inside a tab, with no server behind it.

[qemu-wasm](https://github.com/ktock/qemu-wasm) is a patched QEMU that runs in the browser. It's not a reimplementation or a toy: it's QEMU compiled to WebAssembly, with JIT binary translation (TCG) and multi-threading support. The same QEMU you use on your machine, running in a tab.

## How it works

QEMU has several backends for running guest code. The fastest is TCG, which translates the guest binary to native machine code. Here the "host" is WebAssembly, so the project adds a TCG backend that translates QEMU's IR to Wasm.

WebAssembly doesn't let you jump to code generated in memory, so instead they lean on browser APIs (`WebAssembly.Module` and `WebAssembly.Instance`). Each translation block (TB) is compiled as a standalone Wasm module that imports memory and helper functions from the main QEMU module.

The problem: compiling every block to Wasm is expensive, and browsers can't handle creating thousands of modules. So the solution is hybrid. Cold blocks are interpreted (TCI, the slow interpreter) and only blocks that run many times (~1000) get compiled to Wasm.

It's experimental software, but it works. There's a [demo](https://ktock.github.io/qemu-wasm-demo/) with x86_64, aarch64 (it even emulates a Raspberry Pi), and riscv64 guests. And part of this is being upstreamed into QEMU: the interpreter mode (TCI) for 32-bit guests already landed in QEMU 10.1, and the rest is still under discussion.

## The use case that blew my mind: trynix.dev

Knowing the engine is fine, but the part I find brutal is the use [Farid Zakaria](https://fzakaria.com/) gave it: [trynix.dev](https://trynix.dev).

The idea: boot an x86_64 Linux VM in your tab and give it a Nix store as its filesystem. The result is that you can run **any nixpkgs package from the last 13 years** — over 310,000 versions — without installing anything on your machine.

And they're URL-addressable. Try this:

```text
https://trynix.dev/?pkg=python3%403.6.2
```

Click **Boot** and you get an interactive shell against a virtual machine running Python 3.6.2 from 2017. Nothing runs on a server: the page is static, the kernel is WebAssembly, and the package closure downloads from cache.nixos.org (which serves `access-control-allow-origin: *`, the thing that makes all this possible).

You can even boot two versions of `hello` at once without them clashing, because in Nix each binary references its dependencies by absolute path:

```text
https://trynix.dev/?pkg=hello@2.10&pkg=hello@2.12.2
```

To make it feel instant, the site pre-fetches the engine and a VM snapshot in the background, and never boots from scratch: it resumes a machine that was booted once with the native QEMU and paused right before mounting the store.

## The GitHub Action: review a PR by booting it

The most practical part is [trynix-preview](https://github.com/marketplace/actions/trynix-preview), a GitHub Action that comments on every pull request with a link to boot the PR's build in the browser. No servers, no SSH, no cloning, no building. Just a link.

```yaml
# Set up Cachix as our Nix cache.
- uses: cachix/cachix-action@v17
  with:
    name: sqlelf
    authToken: ${{ secrets.CACHIX_AUTH_TOKEN }}
# Build the PR's code and push it to the cache.
- run: nix build .#default
- uses: fzakaria/trynix@v1
  with:
    cache: https://sqlelf.cachix.org
    publicKey: sqlelf.cachix.org-1:MLnjolA9AsKscTOJKDSA+ZAcgIK8BwZA574j4+Cs2bg=
    attrs: .#default
```

Two caveats: the action builds and caches nothing — you need to have filled the cache yourself — and since the workflow runs on fork PRs, use a segregated cache and `allow-unsafe-pr-checkout: true`.

## Limitations

It's not all magic:

- Large binaries are slow: they can take 1-2 minutes to run. There's a [benchmark page](https://trynix.dev/bench/) with data.
- The whole closure has to fit in tab memory (~1.5 GiB cap, and WebAssembly limits it to 4 GiB since it's a 32-bit address space).
- The first run of a binary is slow because it has to translate from x86_64 to Wasm; subsequent runs are faster because it's cached in memory.

Still, as a workflow for small and medium binaries it's impressive. "Does this fix the bug?" stops being a thought experiment.

*Original source*: [Simon Willison - Any Nix package, live in your browser](https://simonwillison.net/2026/Sep/10/trynix/)
