Title: Escaneo a doble cara con la Brother DCP-L3560CDW
Date: 2026-05-03
Tags: brother, impresora, escaner, linux, simple-scan, paperless
Slug: escaneo-doble-cara-brother-dcp-l3560cdw
Lang: es
Featured_image: /images/brother-escaneo-doble-pagina.png
Summary: Workaround para escanear documentos a doble cara con la Brother DCP-L3560CDW y su alimentador simplex.
Category: Infraestructura

![Brother DCP-L3560CDW y papeles desordenados](/images/brother-escaneo-doble-pagina.png)

Mi nueva multifunción [Brother DCP-L3560CDW](https://www.manua.ls/brother/dcp-l3560cdw/manual) no escanea a doble cara desde el alimentador. El ADF es solo simple cara, aunque la impresora sí imprime a dúplex.

Para documentos a una cara, el flujo es perfecto: meto las hojas en el alimentador, pulso _Scan_ en la pantalla táctil de 3.7 pulgadas y el documento aparece directamente en la carpeta Samba de Paperless. Sin tocar el PC.

El problema llega con documentos a doble cara. La solución que uso:

1. Escaneo todas las páginas impares con el alimentador
2. Doy la vuelta al taco, pongo la última página boca arriba y escaneo las pares
3. En [Document Scanner](https://gitlab.gnome.org/GNOME/simple-scan) (simple-scan): menú hamburguesa → _Reorder pages_ → _Combine sides (reverse)_
4. Guardo el PDF
5. Lo muevo a la carpeta de red para que Paperless lo ingiera

He mirado alternativas en KDE (Skanpage, Skanlite) pero ninguna tiene la función de intercalado manual que ofrece Document Scanner. Skanlite ni siquiera permite juntar varias páginas en un mismo PDF.

Seguiré investigando si hay alguna forma más directa. De momento, este flujo funciona.
