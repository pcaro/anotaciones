---
title: Estados de Conexión TCP en GNU/Linux: netstat y ss
date: 2025-12-25 13:30
tags: linux, redes, tcp, netstat, ss, sistemas
lang: es
category: Sistemas
slug: estados-conexion-tcp-netstat-ss
summary: Comprende los diferentes estados de conexión TCP reportados por netstat y ss, desde el establecimiento hasta la terminación, para un mejor diagnóstico de red.
---

En el mundo de GNU/Linux, herramientas como `netstat` y `ss` son indispensables para monitorizar y diagnosticar el estado de las conexiones de red en nuestros sistemas. Para interpretar correctamente su salida, es fundamental entender los diferentes estados por los que atraviesa una conexión TCP. Esta entrada explora esos estados, desde el establecimiento hasta la terminación de una conexión.

## Fases de una Conexión TCP

Una conexión TCP se gestiona a través de tres fases principales:

1.  **Establecimiento de la Conexión**: Un proceso de reconocimiento (handshake) de varios pasos que inicia la conexión.
2.  **Transferencia de Datos**: Una vez establecida, los datos se envían entre los dos puntos finales.
3.  **Terminación de la Conexión**: Cierra la conexión y libera los recursos asociados.

Durante estas fases, el socket de Internet (el punto final local de la comunicación) experimenta una serie de cambios de estado.

## Estados del Socket TCP Explicados

Aquí se detallan los estados más comunes que puedes encontrar al listar conexiones con `netstat` o `ss`:

*   **ESTABLISHED**: La conexión TCP está establecida y lista para transferir datos. Este es el estado deseado para una conexión activa.
*   **SYN_SENT**: El socket local ha enviado un paquete SYN al servidor remoto y está esperando una respuesta SYN-ACK. Indica que se está intentando establecer una conexión.
*   **SYN_RECV**: El servidor ha recibido un paquete SYN de un cliente y ha respondido con un SYN-ACK, esperando ahora un ACK del cliente. Es parte del handshake de tres vías.
*   **FIN_WAIT1**: El socket local ha cerrado su lado de la conexión y ha enviado un paquete FIN, esperando un ACK del par remoto. La conexión se está cerrando activamente.
*   **FIN_WAIT2**: El socket local ha recibido el ACK a su FIN, pero aún está esperando un paquete FIN del par remoto para cerrar completamente la conexión.
*   **TIME_WAIT**: El socket ha esperado después de cerrar la conexión para asegurarse de que todos los paquetes han sido transmitidos y recibidos por ambos lados, y para permitir que los paquetes duplicados se extingan en la red. Es un estado de espera necesario antes de liberar completamente los recursos.
*   **CLOSE**: El socket no está en uso y no hay conexión.
*   **CLOSE_WAIT**: El par remoto ha cerrado su lado de la conexión (ha enviado un FIN y ha sido ACKed), y el socket local está esperando que la aplicación local cierre su propio lado.
*   **LAST_ACK**: El socket local ha enviado su FIN al par remoto, y está esperando el ACK final del par remoto. Esto sucede después de un `CLOSE_WAIT`.
*   **LISTEN**: El socket está a la espera de conexiones entrantes. Solo se ve con las opciones `--listening (-l)` o `--all (-a)` de `netstat`/`ss`.
*   **CLOSING**: Ambos lados de la conexión han intentado cerrarse simultáneamente, y el socket local está en el proceso de enviar/recibir FIN y ACK.
*   **UNKNOWN**: El estado del socket es desconocido o no se puede determinar.

## Herramientas: `netstat` y `ss`

Puedes ver estos estados utilizando comandos como:

```bash
netstat -tn   # Muestra conexiones TCP, sin resolución de nombres (-n)
ss -tn        # Versión moderna y más rápida de netstat
```

La opción `-t` filtra para conexiones TCP y `-n` evita la resolución de nombres, lo que acelera la salida y muestra las IPs directamente.

## Conclusión

Entender los estados de conexión TCP es vital para diagnosticar problemas de red, identificar procesos que no responden o que están atascados, y comprender cómo se comportan las aplicaciones en términos de conectividad. Saber qué significa cada estado te permite depurar problemas de forma más efectiva en tu sistema GNU/Linux.

*Artículo original*: [Tipos de Conexiones en netstat y ss Explicadas](https://www.ochobitshacenunbyte.com/2020/11/07/tipos-de-conexiones-en-netstat-y-ss-explicadas/)
