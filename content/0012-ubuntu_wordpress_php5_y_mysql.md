Date: 2007-11-25 06:03
Guid: http://www.pablocaro.es/?p=17
Tags: 
Categories: Sin categoría
Title: ubuntu, wordpress, php5 y mysql

Configurando un wordpress local para pruebas (con lighttpd), me encuentro con
el siguiente error: `Your PHP installation appears to be missing the MySQL
which is required for WordPress.` Sabía que php5 no tiene incluido el soporte
para mysql pero para mi sorpresa en mi ubuntu yo sí tenía instalado el paquete
adecuado. El problema es que no estaba activado. Por si les pasa a otros y
para recordarlo en un futuro, la cosa se arregló con: `sudo dpkg-reconfigure
php5-mysql` y el pertinente reinicio del servidor: ` ` `sudo
/etc/init.d/lighttpd restart`

