Title: Powerful Command Line Tools for Developers
Date: 2016-06-07 11:36
Tags: cli, tools, development, networking, testing
Lang: en
Category: Tools
Slug: herramientas-desarrolladores-linea-comandos
Summary: Collection of essential command line tools for developers: curl, ngrep, netcat, sshuttle, siege, and mitmproxy

The **command line remains the most powerful environment** for developers. These specialized tools dramatically expand your debugging, testing, and analysis capabilities.

## Curl: The HTTP Swiss Army Knife

```bash
# Get your public IP
curl ifconfig.me

# Inspect response headers
curl -I https://example.com

# POST with JSON data
curl -X POST -H "Content-Type: application/json" \
     -d '{"key":"value"}' https://api.example.com
```

**Main usage**: Network data transfer, API testing, HTTP inspection.

## Ngrep: Grep for Network Traffic

```bash
# Filter HTTP traffic by keyword
ngrep -i "password" port 80

# Capture by specific IP
ngrep host 192.168.1.100

# Monitor traffic on specific port
ngrep port 443
```

**Main usage**: Network packet analysis, protocol debugging, traffic monitoring.

## Netcat (nc): The Networking Swiss Army Knife

```bash
# Port scanning
nc -zv example.com 1-1000

# Transfer file between servers
# Receiver: nc -l 1234 > received_file
# Sender: nc destination_server 1234 < file_to_send

# Create simple HTTP server
echo "HTTP/1.1 200 OK\n\nHello world" | nc -l 8080
```

**Main usage**: Port scanning, file transfer, connectivity testing.

## Sshuttle: Easy VPN with SSH

```bash
# Tunnel all traffic
sshuttle -r user@server 0.0.0.0/0

# Tunnel only a subnet
sshuttle -r user@server 192.168.1.0/24

# Bypass geo-blocking
sshuttle -r remote_server 0.0.0.0/0 --dns
```

**Main usage**: Secure tunneling, geo-restriction bypass, protection on public WiFi.

## Siege: HTTP Load Bombardment

```bash
# Simple load test
siege -c 25 -t 60s https://example.com

# Test with multiple URLs
siege -c 50 -t 30s -f urls.txt

# Specific benchmark
siege -c 100 -r 10 https://api.example.com/endpoint
```

**Main usage**: Performance testing, HTTP benchmarking, load simulation.

## Mitmproxy: Spy on HTTP/S Traffic

```bash
# Basic proxy
mitmproxy -p 8080

# Transparent mode
mitmproxy --mode transparent

# Save traffic to file
mitmdump -w capture.flow
```

**Main usage**: Web application debugging, HTTPS traffic inspection, API analysis.

## Typical Workflow

```bash
# 1. Scan connectivity
nc -zv api.example.com 443

# 2. Analyze response
curl -I https://api.example.com

# 3. Monitor traffic
ngrep -i "api" port 443

# 4. Load test
siege -c 20 -t 30s https://api.example.com

# 5. Detailed debugging
mitmproxy -p 8080
```

## Why Command Line?

- **Speed**: No GUI overhead
- **Scriptability**: Complete automation
- **Flexibility**: Combination with pipes and redirects
- **Universality**: Available on any server

These tools turn your terminal into a **complete networking and testing laboratory**.

*Original source*: [Somos Apañados](http://www.xn--apaados-6za.es/tenemos-que-apanar/internet-tutoriales-y-trucos/317-potentes-herramientas-desarrolladores-linea-comandos.html)
