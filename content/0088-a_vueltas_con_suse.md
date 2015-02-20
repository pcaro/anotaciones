Date: 2013-03-25 11:01
Category: Sin Categoría
Guid: http://www.pablocaro.es/?p=374
Title: A vueltas con suse

Algunos comandos de zypper para recordar: Para borrar un paquete y también las
dependencias:

    
    
    
    zypper remove  --clean-deps packate
    

Listar paquetes huérfanos:

    
    
    
    LC_ALL=C zypper se -s | fgrep '(System Packages)'
    

