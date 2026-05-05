Title: Double-sided scanning with the Brother DCP-L3560CDW
Date: 2026-05-03
Tags: brother, impresora, escaner, linux, simple-scan, paperless
Lang: en
Slug: escaneo-doble-cara-brother-dcp-l3560cdw
Featured_image: /images/brother-escaneo-doble-pagina.png
Summary: Workaround for scanning double-sided documents with the Brother DCP-L3560CDW and its simplex document feeder.
Category: Infraestructura

![Brother DCP-L3560CDW and scattered papers](/images/brother-escaneo-doble-pagina.png)

My new [Brother DCP-L3560CDW](https://www.manua.ls/brother/dcp-l3560cdw/manual) multifunction printer doesn't scan both sides from the document feeder. The ADF is simplex-only, even though the printer does support duplex printing.

For single-sided documents, the workflow is seamless: I load the pages into the feeder, press _Scan_ on the 3.7-inch touchscreen, and the document lands directly in Paperless's Samba share. No PC needed.

The issue comes with double-sided documents. Here's the workaround I use:

1. Scan all odd pages through the feeder
2. Flip the stack, place the last page facing up, and scan the even pages
3. In [Document Scanner](https://gitlab.gnome.org/GNOME/simple-scan) (simple-scan): hamburger menu → _Reorder pages_ → _Combine sides (reverse)_
4. Save the PDF
5. Move it to the network folder for Paperless to ingest

I checked KDE alternatives (Skanpage, Skanlite) but none have the manual interleave feature that Document Scanner offers. Skanlite can't even combine multiple pages into a single PDF.

I'll keep looking for a more direct approach. For now, this workflow does the job.
