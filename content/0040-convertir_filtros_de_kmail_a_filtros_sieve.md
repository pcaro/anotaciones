Date: 2009-06-06 14:13
Guid: http://www.pablocaro.es/?p=86
Tags: 
Categories: Python, Linux, Yaco, Sistemas
Title: Convertir filtros de kmail a filtros sieve

No hace mucho que dejé de usar
[POP](http://en.wikipedia.org/wiki/Post_Office_Protocol) en mis correos para
pasarme al [IMAP](http://en.wikipedia.org/wiki/IMAP) desconectado de kmail con
toda las ventaja que ello supone. Pero todavía seguía utilizando los mismos
filtros en kmail que me ordenan los correos por carpeta. Con este sistema el
filtrado se realiza una vez descargado el correo, de forma que, ahora con
imap, el kmail tiene que pasar los filtros y actualizar las carpetas en el
servidor tras el moviento de correos. Desde luego no es lo más conveniente. Lo
más util que el filtrado del correo se realice en el servidor. De esta forma
nuestro correo ya se encuentra organizado accedas con el cliente que accedas
al correo (webmail, móviles de última generación, etc). Para ello existen los
filtros
[sieve](http://en.wikipedia.org/wiki/Sieve_\(mail_filtering_language\)). Pero
yo ya tenía mis filtros en kmail, de forma que me hice un pequeño programita
python que convirtiera mis filtros de kmail en un fichero con los filtros
sieve. No discrimina entre cuentas y solo esta probado (y funciona) con mis
filtros simples de moviento de correo, pero lo dejo aquí por si a alguien
pudiera resultarle de utilidad. Para usarlo:

  1. Guardar los filtros de kmail (Preferencias -> Configurar filtros -> Exportar) en un fichero (por ejemplo filtros_pcaro.ini)
  2. Ejecutar _python kmail_to_sieve.py  filtros_pcaro.ini > filtros.sieve_ Por la salida de error indicará que no ha podido convertir.
  3. Examinar filtros
  4. Subir y activar desde el mismo kmail (Preferencias -> Gestionar guiones de Sieve.
Podeís descargarlo desde aquí: [kmail_to_sieve](http://www.pablocaro.es/wp-
content/uploads/2009/06/kmail_to_sieve.py) PD: Arreglado el enlace. Gracias
Helder por avisar.

