Date: 2008-07-23 05:07
Guid: http://www.pablocaro.es/grabar-cd-de-800mb-en-linux/
Tags: 
Categories: Sistemas
Title: Grabar CD de 800MB en linux

Tenía que grabar unos datos. Eran 730MB aproximadamente, con un CD habitual
(700MB) iba a ser imposible, pero tenía por ahí un CD philips de 90 minutos
(800MB). Y teniendo ese CD ¿por qué usar un DVD que son más caros? Mi sorpresa
llega cuando el k3b (que uso habitualmente) se niega a grabar, ¡por falta de
espacio! a pesar de que le indico (graicias google) que use el modo DAO en la
interfaz. Total que a grabar desde la consola :-D Aquí dejo el comandito como
anotación para tenerlo de cerca la próxima vez:

    
    
    cdrecord -dev=/dev/scd0 -v -overburn -dao -speed=4 -data -eject /tmp/LaBodademiNovia.iso

La opción necesaria además de "DAO" es "overburn". Podéis ver como cdrecord sí
reconoce todo el tamaño del disco como indica la línea:

    
    
    Total size:      810 MB (80:18.14) = 361361 sectors

_ACTUALIZACIÓN: _Ahora veo una opción en las preferencias de k3b para pervitir
el sobregrabado. Si es que k3b no me podía fallar :-D

