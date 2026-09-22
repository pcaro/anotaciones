---
title: Optimización con IA
slug: optimizacion-con-ia
lang: es
date: 2026-09-22
category: ia
tags: ia, optimización, rendimiento, open-source, librerías
featured_image: /images/optimizacion-con-ia.png
Summary: Mientras solo se habla de lo malo de la IA, en el software maduro está bajando el coste de optimización. Daniel Lemire documenta cómo seis librerías open source se volvieron hasta 2,4x más rápidas en un verano.
---

Solo se habla de lo malo de la IA. Del desempleo, del slop, de las alucinaciones, del coste energético. Y casi nunca de lo que está haciendo bien. En la producción de software la revolución es real y va en una dirección muy concreta: está abaratando todo tipo de costes.

Se habla mucho de lo fácil que es ahora hacer prototipos y crear software nuevo. De acuerdo. Pero el caso interesante es el software **estable**, el que ya está optimizado y donde cada mejora costaba días de trabajo. Ahí es donde el cambio se nota más.

Daniel Lemire lo ha documentado este verano. Mantiene varias librerías open source que usa medio internet: `ada` (parseo de URLs en Node.js), `simdjson` (JSON en Node.js), `simdutf` (Unicode en Node.js), `fast_float` (números en la libc de GCC y Chromium) o las librerías Roaring (bitmaps comprimidos dentro de motores de bases de datos).

![ada: velocidad de parseo de URLs a lo largo del tiempo](/images/optimizacion-con-ia.png)

Estas librerías llevaban años con el rendimiento plano. No porque a nadie le importara, sino porque cada mejora restante exigía días de trabajo fino y nadie tenía esos días. En 2026, seis de ellas se volvieron mucho más rápidas, casi todo en unas semanas de verano.

Los números:

- **ada**: de 0,54 GB/s a 1,28 GB/s en seis semanas (2,4x). Unos 15 millones de URLs por segundo por núcleo.
- **simdutf**: la validación ASCII pasó de 83 GB/s a 160 GB/s.
- **roaring** (Go): la unión `FastOr` 3,1x más rápida y el iterador de múltiples valores entre 4,5x y 5,9x.
- **CRoaring** (C): el cardinal de bitmaps de 64 bits 4,9x más rápido.
- **fast_float**: +43% y +70% en dos ficheros de prueba.
- **simdjson**: serialización 1,6x–2,1x más rápida con reflexión de C++26.

Lemire es honesto: no sabe cuánta IA hubo en cada caso concreto. No pregunta cómo llegó cada uno a su código; solo pide que sea bueno. Él mismo programa con Claude (Opus 5), Grok y DeepSeek (V4 Pro).

Su explicación de por qué pasó es la clave del asunto: **las técnicas son conocidas desde hace años. Lo que cambió es que ahora es barato probar ideas.** Antes cada intento de optimización costaba días; ahora puedes lanzar veinte experimentos en el tiempo que antes dedicabas a uno, descartar los diecinueve que no funcionan y quedarte con el bueno. Eso es todo.

Hay un sesgo muy humano aquí, el de la apuesta unilateral (*one-sided bet fallacy*): cuando vemos los perjuicios de algo, ignoramos los beneficios. Los coches matan, pero las ambulancias salvan. Con la IA estamos en esa fase: solo miramos el lado malo.

En este caso el beneficio es concreto y medible. Millones de personas ejecutan estas librerías, y este verano van más rápido. Gratis. Sin cambiar nada de su lado.

El software nuevo y los prototipos molan, pero la caída del coste de optimización en software maduro quizá sea el efecto más infravalorado de todo esto.

*Fuente original*: [A summer of AI optimization](https://lemire.me/blog/2026/09/22/a-summer-of-ai-optimization/) — Daniel Lemire.
