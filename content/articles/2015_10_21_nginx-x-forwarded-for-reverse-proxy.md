Title: Nginx: Configurar X-Forwarded-For en reverse proxy
Date: 2015-10-21 23:05
Tags: nginx, reverse-proxy, x-forwarded-for, ip-real, configuración
Lang: es
Category: DevOps
Slug: nginx-x-forwarded-for-reverse-proxy
Summary: Cómo configurar Nginx para pasar la IP real del cliente a servidores backend usando el header X-Forwarded-For en configuraciones de reverse proxy

Cuando usas **Nginx como reverse proxy**, necesitas que el servidor backend vea la **IP real del cliente**, no la IP del proxy. El header `X-Forwarded-For` resuelve este problema.

## El problema

Sin configuración, el servidor backend solo ve la IP del proxy Nginx, perdiendo información crucial sobre el cliente real para:
- **Logs de acceso** precisos
- **Geolocalización** correcta  
- **Rate limiting** por IP real
- **Análisis de tráfico** fidedignos

## Solución 1: IP simple

```nginx
proxy_set_header X-Forwarded-For $remote_addr;
```

**Uso**: Cuando Nginx es el único proxy en la cadena.  
**Resultado**: Header contiene solo la IP del cliente original.

## Solución 2: Cadena de IPs

```nginx
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

**Uso**: Cuando hay múltiples proxies en la cadena.  
**Resultado**: Conserva IPs existentes y añade la actual.

## Configuración práctica

```nginx
server {
    listen 80;
    server_name example.com;
    
    location / {
        proxy_pass http://backend-server;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## Headers relacionados

- **X-Real-IP**: IP del cliente más reciente
- **X-Forwarded-For**: Cadena completa de IPs
- **X-Forwarded-Proto**: Protocolo original (http/https)
- **Host**: Hostname original

## Verificación

```bash
# En el servidor backend, verifica los headers
tail -f /var/log/apache2/access.log
# O en tu aplicación
echo $_SERVER['HTTP_X_FORWARDED_FOR'];
```

## Consideraciones de seguridad

⚠️ **Importante**: Los headers X-Forwarded-* pueden ser falsificados por clientes. En entornos de producción, asegúrate de que solo tu proxy los establezca.

Esta configuración es esencial para mantener **trazabilidad completa** en arquitecturas con reverse proxy.

*Fuente original*: [Networking How To's](http://www.networkinghowtos.com/howto/set-the-x-forwarded-for-header-on-a-nginx-reverse-proxy-setup/)