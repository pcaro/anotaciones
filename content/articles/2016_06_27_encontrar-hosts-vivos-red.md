Title: Cómo encontrar hosts vivos en tu red local
Date: 2016-06-27 07:59
Tags: nmap, network-discovery, arp-scan, netdiscover, seguridad
Lang: es
Category: Seguridad
Slug: encontrar-hosts-vivos-red
Summary: Métodos y herramientas para descubrir dispositivos activos en redes locales usando nmap, arp-scan, netdiscover y otras técnicas de reconocimiento

Descubrir **qué dispositivos están activos** en tu red local es una tarea fundamental para administradores de red y profesionales de seguridad. Estas son las técnicas más efectivas.

## Nmap: La herramienta principal

### Escaneo básico de hosts
```bash
# Ping scan simple
nmap -sn 192.168.1.1/24

# Escaneo con puertos TCP específicos
nmap -sP -PS22,3389 192.168.1.1/24

# Escaneo UDP para dispositivos especiales
nmap -sP -PU161 192.168.1.1/24
```

**-sn**: Solo descubrimiento de hosts, sin escaneo de puertos  
**-PS**: TCP SYN discovery en puertos específicos  
**-PU**: UDP discovery (útil para dispositivos embebidos)

### Escaneos más exhaustivos
```bash
# Escaneo completo con detección de OS
nmap -A 192.168.1.1/24

# Escaneo TCP Connect (menos intrusivo)
nmap -sT 192.168.1.1/24

# Bypass de firewall con fragmentación
nmap -f -sS 192.168.1.1/24
```

## Herramientas alternativas

### arp-scan: Basado en ARP
```bash
# Escaneo de subred local
arp-scan 192.168.12.0/24

# Con interfaz específica
arp-scan -I eth0 172.16.17.0/24

# Scan local simplificado
arp-scan -l
```

**Ventaja**: Funciona incluso con firewalls estrictos

### netdiscover: Descubrimiento pasivo/activo
```bash
# Descubrimiento activo
netdiscover -r 172.16.17.0/24

# Modo pasivo (solo escucha)
netdiscover -p

# Fast mode
netdiscover -f -r 192.168.1.0/24
```

### fing: Scanner móvil
```bash
# Escaneo rápido
fing -r 1

# Con detalles del fabricante
fing -o table,csv
```

## Verificación post-escaneo

### Revisar tabla ARP
```bash
# Ver tabla ARP actual
arp -a -n

# En sistemas modernos
ip neigh show

# Limpiar y reescanear
sudo arp -d -a
ping -c 1 192.168.1.{1..254}
arp -a
```

## Técnicas avanzadas

### Wireshark para análisis pasivo
1. Capturar tráfico en la interfaz de red
2. Filtrar por ARP: `arp`
3. Analizar broadcast traffic
4. Identificar dispositivos por patrones de tráfico

### Scripts de automatización
```bash
#!/bin/bash
# Scan completo de red local
echo "Escaneando red..."
nmap -sn $(ip route | grep -E "^192|^10|^172" | awk '{print $1}' | head -1)
echo "Verificando ARP..."
arp -a -n | grep -v "incomplete"
```

## Consideraciones importantes

### Limitaciones por firewall
- **Algunos dispositivos** bloquean ping/ICMP
- **Firewalls corporativos** pueden filtrar escaneos
- **Diferentes puertos** pueden revelar dispositivos "ocultos"

### Consideraciones legales
⚠️ **Autorización necesaria**: Solo escanea redes propias  
⚠️ **Políticas corporativas**: Verifica antes de escanear en entornos empresariales

### Optimización por tipo de red
```bash
# Red doméstica (routers, IoT)
nmap -sn --min-rate 1000 192.168.1.1/24

# Red corporativa (servidores, estaciones)
nmap -sP -PS80,443,22,3389 10.0.0.0/8

# Red industrial (dispositivos embebidos)
nmap -sP -PU161,502 172.16.0.0/12
```

La **combinación de múltiples técnicas** proporciona el panorama más completo de dispositivos activos en tu red.

*Fuente original*: [Information Security Stack Exchange](http://security.stackexchange.com/questions/36198/how-to-find-live-hosts-on-my-network)