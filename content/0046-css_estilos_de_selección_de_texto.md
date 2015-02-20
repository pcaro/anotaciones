Date: 2009-07-09 03:57
Guid: http://www.pablocaro.es/?p=133
Tags: 
Categories: Programación, Web
Title: CSS: Estilos de selección de texto

Una de esas declaraciones de CSS3 que ya aceptan muchos navegadores actuales
es **::selection**. Se puede utilizar así:

    
    
    p::selection {
    	background: #ccaacc; /* Safari */
    	}
    p::-moz-selection {
    	background: #ccaacc; /* Firefox */
    }
    

