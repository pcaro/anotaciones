Date: 2009-05-21 10:41
Guid: http://www.pablocaro.es/?p=62
Tags: 
Categories: Web
Title: Contenedor de Floats: How to IE & FF

Espero no olvidar esto más así que dejo la notita. Si tienes un elemento (por
ejemplo un div#padre), que contiene sólo flotantes (otros divs por ejemplo),
no será capaz IE de calcular bien su tamaño (se ve muy claro con un
background). Para que funcione con explorer y firefox la regla es ponerle al
elemento contenedor las reglas css:

    
    
    div#padre {
      overflow: hidden;
      zoom:1;
    }
    

la regla del zoom es para aplicar el hasLayout en el ie6. No es estándar y es
mejor ponerla en un condicional para este navegador. Nota personal: Pablo
olvida el div con el clear:both que en este caso no es solución.

