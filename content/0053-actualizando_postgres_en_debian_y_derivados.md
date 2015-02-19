Date: 2009-11-26 05:19
Guid: http://www.pablocaro.es/?p=186
Title: Actualizando postgres en debian y derivados

Siempre que se habla de debian, se alaba su paquetería. Y yo estoy de acuerdo
de que es uno de los puntos fuertes de la distribución. Hoy me refiero a la
facilidad de tener instaladas y conviviendo felices varias versiones de la
base de datos [postgres](http://www.postgresql.org/). Ya comenté esto en su
momento en [Instalar postgres 8.2 en jaunty](/instalar-postgres-82-en-
jaunty/). Pues el tener dos servidores instalados a la vez, permite la fácil[
migración de un versión a otra del motor de base de
datos](http://www.postgresql.org/docs/8.4/interactive/migration.html). En este
caso detallo como migré las bases de datos de mi equipo ubuntu
[karmic](http://releases.ubuntu.com/karmic/) de postgres 8.3 a 8.4.

  1. Primero tener instalados los dos paquetes: postgresql-8.3 y postgresql-8.4.
  2. Determinar en que puerto se ejecuta cada instancia. Esto lo podemos hacer mirando los ficheros _/etc/postgresql/8.X/main/postgresql.conf _(variable _port_). En mi caso 5482 y 5433 respectivamente. Lo puedes comprobar con: 
    
        $ sudo netstat -putan | grep postgres

  3. Después lanzar los dos servidores: 
    
        $ sudo /etc/init.d/postgresql-8.3 start
    $ sudo /etc/init.d/postgresql-8.4 start

  4. Finalmente copiar los datos de una versión a otra 
    
        $ sudo su - postgres
    $ pg_dumpall -p 5432 | psql -d postgres -p 5433

  5. Probar que todo ha ido correctamente

