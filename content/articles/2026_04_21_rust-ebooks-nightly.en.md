Title: Rust eBooks Nightly — Rust books in EPUB, AZW3, MOBI, and PDF
Date: 2026-04-21 22:00
Category: Programming
Tags: Rust, eBooks, EPUB, Calibre, GitHub Actions
Slug: rust-ebooks-nightly
Lang: en
featured_image: /images/rust-ebooks-nightly.png
Summary: Artur Sulej's project that automatically builds and publishes the latest versions of top Rust books as eBooks. Updated daily.
Status: published

[Rust eBooks Nightly](https://artur-sulej.github.io/rust-ebooks/) is a project by Artur Sulej that automatically builds and publishes the latest versions of the most important Rust books in EPUB, AZW3, MOBI and PDF formats. Updated daily via GitHub Actions.

Available books right now:

1. **The Rust Programming Language** (the official book from rust-lang.org)
2. **Rust By Example**
3. **The Rust Reference**
4. **The Rustonomicon** — all about unsafe code in Rust
5. **The Cargo Book**
6. **Rust Cookbook**
7. **Asynchronous Programming in Rust**
8. **Learning Rust With Entirely Too Many Linked Lists** — my favorite for learning alienist patterns
9. **Rust Unsafe Code Guidelines**
10. **The Embedded Rust Book**
11. **The wasm-bindgen Guide**
12. **Real-Time Interrupt-driven Concurrency** (RTIC)
13. **The Rust and WebAssembly Book**

The nice thing about this project is that it's nightly — every day it clones each book's repository, builds the content with mdBook, converts it to different formats with Calibre, and uploads to GitHub Pages. If a book fails to build, it's skipped and an issue is created automatically. The others keep going.

I've been using a Likebook Muses for a while now, and having Rust books always at hand is quite useful.

These books cover the official documentation, so they're nicely complemented by paid titles like *Programming Rust* (O'Reilly), *Rust for Rustaceans* by Jon Gjengset, or *Black Hat Rust* by Sylvain Kerkour.

Link: [https://artur-sulej.github.io/rust-ebooks/](https://artur-sulej.github.io/rust-ebooks/)
Repo: [https://github.com/Artur-Sulej/rust-ebooks](https://github.com/Artur-Sulej/rust-ebooks)
