Title: Rust eBooks Nightly — libros de Rust en EPUB, AZW3, MOBI y PDF
Date: 2026-04-21 22:00
Category: Programación
Tags: Rust, eBooks, EPUB, Calibre, GitHub Actions
Slug: rust-ebooks-nightly
Lang: es
featured_image: /images/rust-ebooks-nightly.png
Summary: Un proyecto de Artur Sulej que publica automáticamente las versiones más recientes de los mejores libros de Rust en formatos eBook. Se actualiza daily.
Status: published

[Rust eBooks Nightly](https://artur-sulej.github.io/rust-ebooks/) es un proyecto de Artur Sulej que automáticamente construye y publica la última versión de los libros de Rust más importantes en EPUB, AZW3, MOBI y PDF. Se actualiza diariamente via GitHub Actions.

Los libros disponibles ahora mismo:

1. **The Rust Programming Language** (el libro oficial de rust-lang.org)
2. **Rust By Example**
3. **The Rust Reference**
4. **The Rustonomicon** — todo sobre código unsafe en Rust
5. **The Cargo Book**
6. **Rust Cookbook**
7. **Asynchronous Programming in Rust**
8. **Learning Rust With Entirely Too Many Linked Lists** — mi favorito para aprender alienist patterns
9. **Rust Unsafe Code Guidelines**
10. **The Embedded Rust Book**
11. **The wasm-bindgen Guide**
12. **Real-Time Interrupt-driven Concurrency** (RTIC)
13. **The Rust and WebAssembly Book**

La gracia del proyecto es que es nightly — cada día clona el repositorio de cada libro, lo construye con mdBook, lo convierte a los distintos formatos con Calibre, y lo sube a GitHub Pages. Si un libro falla en construirse, se salta y crea un issue automáticamente. Los demás siguen adelante.

Llevo tiempo usando un Likebook Muses y tener los libros de Rust siempre a mano es bastante útil.

Estos libros cubren la documentación oficial, así que están bien complementados con otros de pago y gran calidad como *Programming Rust* (O'Reilly), *Rust for Rustaceans* de Jon Gjengset o *Black Hat Rust* de Sylvain Kerkour.

Enlace: [https://artur-sulej.github.io/rust-ebooks/](https://artur-sulej.github.io/rust-ebooks/)
Repo: [https://github.com/Artur-Sulej/rust-ebooks](https://github.com/Artur-Sulej/rust-ebooks)
