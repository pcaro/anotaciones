Date: 2009-06-29 03:54
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=104
Title: Listar las bases de datos postgres que tengo instaladas

Para ello:

    
    
    
    pcaro@davinci$ sudo /etc/init.d/postgresql-8.3 start
    pcaro@davinci$ sudo su - postgres
    postgres@davinci:~$ psql -l
    

