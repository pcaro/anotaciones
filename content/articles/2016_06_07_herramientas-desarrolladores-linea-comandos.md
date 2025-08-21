Title: Potentes herramientas para desarrolladores desde línea de comandos
Date: 2016-06-07 11:36
Tags: cli, herramientas, desarrollo, networking, testing
Lang: es
Category: Herramientas
Slug: herramientas-desarrolladores-linea-comandos
Summary: Colección de herramientas de línea de comandos esenciales para desarrolladores: curl, ngrep, netcat, sshuttle, siege y mitmproxy

La **línea de comandos sigue siendo el entorno más poderoso** para desarrolladores. Estas herramientas especializadas amplían dramáticamente tus capacidades de debugging, testing y análisis.

## Curl: El navajero suizo del HTTP

```bash
# Obtener tu IP pública
curl ifconfig.me

# Inspeccionar headers de respuesta
curl -I https://ejemplo.com

# POST con datos JSON
curl -X POST -H "Content-Type: application/json" \
     -d '{"key":"value"}' https://api.ejemplo.com
```

**Uso principal**: Transferencia de datos de red, testing de APIs, inspección HTTP.

## Ngrep: Grep para tráfico de red

```bash
# Filtrar tráfico HTTP por palabra clave
ngrep -i "password" port 80

# Capturar por IP específica
ngrep host 192.168.1.100

# Monitorear tráfico en puerto específico
ngrep port 443
```

**Uso principal**: Análisis de paquetes de red, debugging de protocolos, monitoreo de tráfico.

## Netcat (nc): La navaja suiza del networking

```bash
# Escaneo de puertos
nc -zv ejemplo.com 1-1000

# Transferir archivo entre servidores
# Receptor: nc -l 1234 > archivo_recibido
# Emisor: nc servidor_destino 1234 < archivo_enviar

# Crear servidor HTTP simple
echo "HTTP/1.1 200 OK\n\nHola mundo" | nc -l 8080
```

**Uso principal**: Escaneo de puertos, transferencia de archivos, testing de conectividad.

## Sshuttle: VPN fácil con SSH

```bash
# Tunelar todo el tráfico
sshuttle -r usuario@servidor 0.0.0.0/0

# Tunelar solo una subred
sshuttle -r usuario@servidor 192.168.1.0/24

# Evitar geobloqueos
sshuttle -r servidor_remoto 0.0.0.0/0 --dns
```

**Uso principal**: Tunneling seguro, bypass de geo-restricciones, protección en WiFi público.

## Siege: Bombardeo de carga HTTP

```bash
# Test de carga simple
siege -c 25 -t 60s https://ejemplo.com

# Test con múltiples URLs
siege -c 50 -t 30s -f urls.txt

# Benchmark específico
siege -c 100 -r 10 https://api.ejemplo.com/endpoint
```

**Uso principal**: Testing de rendimiento, benchmarking HTTP, simulación de carga.

## Mitmproxy: Espía del tráfico HTTP/S

```bash
# Proxy básico
mitmproxy -p 8080

# Modo transparent
mitmproxy --mode transparent

# Guardar tráfico en archivo
mitmdump -w captura.flow
```

**Uso principal**: Debugging de aplicaciones web, inspección de tráfico HTTPS, análisis de APIs.

## Flujo de trabajo típico

```bash
# 1. Escanear conectividad
nc -zv api.ejemplo.com 443

# 2. Analizar respuesta
curl -I https://api.ejemplo.com

# 3. Monitorear tráfico
ngrep -i "api" port 443

# 4. Test de carga
siege -c 20 -t 30s https://api.ejemplo.com

# 5. Debugging detallado
mitmproxy -p 8080
```

## ¿Por qué línea de comandos?

- **Velocidad**: Sin overhead de GUI
- **Scriptabilidad**: Automatización completa
- **Flexibilidad**: Combinación con pipes y redirects
- **Universalidad**: Disponible en cualquier servidor

Estas herramientas convierten tu terminal en un **laboratorio completo de networking y testing**.

*Fuente original*: [Somos Apañados](http://www.xn--apaados-6za.es/tenemos-que-apanar/internet-tutoriales-y-trucos/317-potentes-herramientas-desarrolladores-linea-comandos.html)