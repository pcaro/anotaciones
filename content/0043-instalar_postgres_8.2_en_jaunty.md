Date: 2009-06-30 10:52
Guid: http://www.pablocaro.es/?p=107
Title: Instalar postgres 8.2 en jaunty

Postgres 8.3 no me permitía crear una base de datos con un encoding distinto a
los instalados en mi maquina, y yo debía recuperar una copia de seguridad de
una base de datos para la ampliación de unos trabajos que vienen de antiguo.
Si intentaba importar los datos fallaba por el encoding:

    
    
    # createdb base_datos  -O owner ; 
    # pg_restore -F c -d base_datos   viernes-27-feb-2009.dump
    pg_restore: [archiver (db)] COPY failed: ERROR:  secuencia de bytes no válida para codificación «UTF8»: 0xa2
    

Y además no me dejaba crear la base de datos con el encoding correcto:

    
    
    postgres@davinci$ createdb  base_datos -E latin1
    createdb: falló la creación de la base de datos:
    ERROR:  la codificación LATIN1 no coincide con la configuración regional del servidor es_ES.UTF-8
    DETAIL:  La configuración regional LC_CTYPE del servidor requiere la codificación UTF8.
    

Para poder seguir adelante dos alternativas:[ cambiar el encoding de mi base
de datos](http://softwarelibre.org.bo/wiki/postgresqlutf8tolatin1) (no podía
porque tengo otras bases de datos) o instalar postgres 8.2 (debian y derivados
permiten tener varios postgres a la vez por paquetería) De esta forma que me
dispuse a descargar los paquetes de haunty: [postgresql-8.2](http://packages.u
buntu.com/hardy/i386/postgresql-8.2/download) y[ postgresql-
client-8.2](http://packages.ubuntu.com/hardy/i386/postgresql-
client-8.2/download) Una vez descargados los paquetes bastó:

    
    
    pcaro@davinci$ sudo dpkg -i postgresql-client-8.2_8.2.7-1_i386.deb
    pcaro@davinci$ sudo dpkg -i postgresql-8.2_8.2.7-1_i386.deb
    sudo aptitude hold postgresql-client-8.2
    sudo aptitude hold postgresql-8.2
    

Luego puedes configurar los postgres para que escuchen en distintos puertos o,
si solo lo necesitas de forma temporal como yo, simplemente parar el 8.3 y
levantar el 8.2 cuando sea necesario. PD: Gracias a Antonio por la ayuda.

