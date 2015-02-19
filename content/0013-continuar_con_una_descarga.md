Date: 2008-01-27 08:37
Guid: http://www.pablocaro.es/continuar-con-una-descarga/
Title: Continuar con una descarga

`scp` no permite continuar con copias que se cortan, pero lo permite rsync. El
comando para recordar es: `alias scpresume="rsync --partial --progress
--rsh=ssh"`Eso claro, siempre que tengas `rsync`

