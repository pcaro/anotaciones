Date: 2008-04-13 14:00
Category: Sin Categoría
Guid: http://www.pablocaro.es/%c2%bfque-ejecutas-tu-desde-la-consola/
Title: ¿Qué ejecutas tu desde la consola?

Un meme para ver que ejecutas desde la consola: pcaro@davinci$ history|awk
'{a[$2]++} END{for(i in a){printf "%5d\t%s\n",a[i],i}}'|sort -rn|head 95
sudo 71   ls 67   cd 33   svn 29   dentro 24   clear 18   ssh 15   i2e-cli 14
ps 13   man A notar que dentro es un script que tengo para hacer un grep -r
filtrando algunos resultados.i2e-cli es un diccionario.

