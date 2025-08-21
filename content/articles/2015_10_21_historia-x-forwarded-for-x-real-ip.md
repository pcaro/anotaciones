Title: La historia detrás de X-Forwarded-For y X-Real-IP
Date: 2015-10-21 23:05
Tags: headers, x-forwarded-for, x-real-ip, proxy, nginx
Lang: es
Category: Redes
Slug: historia-x-forwarded-for-x-real-ip
Summary: Análisis de los headers X-Forwarded-For y X-Real-IP, sus orígenes, diferencias y cómo determinar la IP real del cliente en arquitecturas con múltiples proxies

Determinar la **IP real del cliente** en arquitecturas con proxies es más complejo de lo que parece. Los headers `X-Forwarded-For` y `X-Real-IP` tienen diferentes propósitos y limitaciones.

## X-Forwarded-For: La cadena completa

### Formato y propósito
```
X-Forwarded-For: client, proxy1, proxy2
```

- **Rastrea la IP original** del cliente a través de múltiples saltos
- **Acumula IPs** conforme pasa por proxies
- **No es obligatorio** para todos los proxies

### Limitaciones críticas
⚠️ **Fácilmente falsificable**: Un cliente puede añadir IPs falsas  
⚠️ **Potencialmente no confiable** para determinar la IP real

## X-Real-IP: El enfoque directo

### Características
- **Menos documentación** oficial disponible
- **Comúnmente usado** junto con X-Forwarded-For
- **Enfoque más simple** para pasar la IP del cliente

### Limitación
> "Not many good info or specs about this one" - No hay estándares definitivos

## Configuración Nginx recomendada

Para extraer la IP más precisa:

```nginx
# Configurar proxies conocidos
set_real_ip_from 10.0.0.0/8;
set_real_ip_from 172.16.0.0/12;
set_real_ip_from 192.168.0.0/16;

# Activar procesamiento recursivo
real_ip_recursive on;

# Usar X-Forwarded-For como fuente
real_ip_header X-Forwarded-For;
```

## El desafío real

**Determinar la IP "real" del cliente es inherentemente complejo** debido a:

1. **Múltiples saltos de red**
2. **Proxies no cooperativos**
3. **Potencial spoofing de IP**
4. **Lack de estándares uniformes**

## Buenas prácticas

1. **Validar fuentes confiables** de headers
2. **Configurar correctamente** proxies conocidos
3. **No confiar ciegamente** en headers de cliente
4. **Implementar logging** para debugging

La **confiabilidad real** depende más de tu arquitectura de red que de los headers específicos utilizados.

*Fuente original*: [Distinct Place](http://distinctplace.com/infrastructure/2014/04/23/story-behind-x-forwarded-for-and-x-real-ip-headers/)