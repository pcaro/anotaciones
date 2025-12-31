---
title: `docker-http-https-echo`: Una herramienta esencial para depuración de red
date: 2025-12-25 14:15
tags: docker, http, https, depuracion, redes, herramientas, contenedores
lang: es
category: Herramientas
slug: docker-http-https-echo
summary: `mendhak/docker-http-https-echo` es un contenedor Docker simple que facilita la depuración de configuraciones de red, proxies y balanceadores de carga.
---

En el complejo mundo de las aplicaciones distribuidas, la depuración de problemas de red, proxies, balanceadores de carga o reglas de firewall puede ser una tarea ardua. Necesitamos una forma simple de verificar qué está recibiendo un servidor. Aquí es donde una herramienta como `mendhak/docker-http-https-echo` se vuelve indispensable.

## ¿Qué es `mendhak/docker-http-https-echo`?

Es un contenedor Docker extremadamente ligero y simple que funciona como un servidor HTTP y HTTPS de "eco". Su función principal es **responder a cualquier solicitud HTTP o HTTPS con una descripción detallada de la propia solicitud**. Esto incluye:

*   Cabeceras de la solicitud (headers).
*   Método HTTP (GET, POST, PUT, etc.).
*   URL y parámetros de la solicitud.
*   Cuerpo de la solicitud (body).
*   Dirección IP remota del cliente.
*   Información del TLS/SSL (si es HTTPS).

## ¿Por qué es útil?

Este tipo de servidor de eco es invaluable para una variedad de escenarios de depuración:

*   **Depuración de Proxies y Balanceadores de Carga**: Verifica si un proxy inverso o un balanceador de carga está reescribiendo cabeceras, modificando URLs o pasando el cuerpo de la solicitud como esperas.
*   **Reglas de Firewall y Seguridad**: Confirma que el tráfico está llegando al destino correcto y que no está siendo bloqueado o alterado.
*   **Inspección de Cabeceras HTTP/HTTPS**: Útil para ver exactamente qué cabeceras envía tu cliente o una aplicación específica.
*   **Pruebas de Integración**: Un objetivo predecible para pruebas automáticas de cómo diferentes servicios se comunican a través de HTTP/HTTPS.
*   **Diagnóstico de Contenido Mixto**: Puedes usarlo para verificar si los recursos HTTP se están cargando correctamente en un contexto HTTPS.

## Cómo Usarlo

Su uso es directo a través de Docker:

### Para HTTP (puerto 8080)

```bash
docker run -p 8080:8080 mendhak/http-https-echo
```

Luego, puedes acceder a `http://localhost:8080` con tu navegador o `curl`:

```bash
curl http://localhost:8080/path?query=value -H "X-Custom-Header: test"
```

### Para HTTPS (puerto 8443)

Para usar HTTPS, debes mapear el puerto HTTPS del contenedor. La imagen ya viene con un certificado autofirmado para pruebas.

```bash
docker run -p 8443:8443 mendhak/http-https-echo
```

Accede a `https://localhost:8443` (es posible que tu navegador te advierta sobre el certificado autofirmado).

## Conclusión

`mendhak/docker-http-https-echo` es una de esas herramientas simples pero increíblemente útiles que todo desarrollador y operador de sistemas debería tener a mano. Facilita la comprensión de los flujos de red y acelera la depuración de problemas de conectividad en cualquier entorno basado en contenedores.

*Repositorio original*: [mendhak/docker-http-https-echo en GitHub](https://github.com/mendhak/docker-http-https-echo)
