Date: 2009-01-30 13:44
Guid: http://www.pablocaro.es/?p=49
Title: Formatear de la forma más fácil una tarjeta SD en ubuntu

Otra anotación para recordar en un futuro. La forma más fácil de formatear una
tarjeta SD es:

  1. Identificar el dispositivo (si esta montada la tarjeta lo ves con el comando mount por ejemplo).
  2. Si no lo tienes ya, instalar el paquete dosfstools.
  3. Ejecutar (con el dispositivo desmontado): **sudo mkdosfs DISPOSITIVO**.

