Date: 2009-12-17 05:06
Category: Sistemas
Guid: http://www.pablocaro.es/?p=212
Title: Crear base de datos mysql a partir de un backup 

Primero crear la base de datos:

    
    
    
    pcaro@davinci$ mysql --user=root -p
    mysql> show databases;
    mysql> create database piwik;
    mysql> GRANT ALL ON piwik.* TO pcaro@localhost IDENTIFIED BY "piwik"
    mysql> show tables;
    

Luego restaurar el backup:

    
    
    
    mysql --user=root --pass=*** --host=localhost piwik < piwik_Thursday.sql
    

Comprobar todo esta bien

    
    
    
    pcaro@davinci$ mysql --user=root -p
    mysql> show tables;
    

