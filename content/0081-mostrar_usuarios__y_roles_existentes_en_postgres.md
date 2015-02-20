Date: 2012-10-24 02:13
Guid: http://www.pablocaro.es/?p=348
Tags: 
Categories: Yaco, Sistemas
Title: Mostrar Usuarios  y roles existentes en postgres

Se utiliza **\du**

    
    
    $ sudo su - postgres
    $ psql 
    postgres=# \du
                               List of roles
     Role name |                   Attributes                   | Member of 
    -----------+------------------------------------------------+-----------
     openerp   | Superuser, Create role, Create DB, Replication | {}
     postgres  | Superuser, Create role, Create DB, Replication | {}
    
    postgres=#

