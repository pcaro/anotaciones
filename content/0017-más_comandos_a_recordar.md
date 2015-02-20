Date: 2008-04-09 11:54
Category: Sistemas
Guid: http://www.pablocaro.es/mas-comandos-a-recordar/
Title: Más comandos a recordar

Otra nota para que no se me vuelvan a olvidar algunos de los super-mini-
comandos unix.

  * Para desconectar un programa de la consola desde la que se está ejecutando y no pare por ejemplo si muere la conexión ssh, hay que usar `disown`.  Es una de esas [herramientas para control de trabajos](http://www.faqs.org/docs/bashman/bashref_79.html) como fg. Los pasos son:
      1. Ejecutar la tarea en segudo plano "ejecutable.sh &", en la consola te saldrá el número de trabajo [1]
      2. luego disown %1
  * `[watch`](http://www.linuxmanpages.com/man1/watch.1.php): para ejecutar un programa periódicamente, mostrando su salida a pantalla completa y pudiendo señalar las diferencias. Lo uso con un ls -l por ejemplo para ver como va cambiando el tamaño de un fichero, etc.
PD: Gracias a mis compañeros de Yaco por enseñarme un poco todos los días.
Nota post-post: Me comentan que es muy útil
[nohup](http://www.linuxmanpages.com/man1/nohup.1.php).

