Title: How to Find Live Hosts on Your Local Network
Date: 2016-06-27 07:59
Tags: nmap, network-discovery, arp-scan, netdiscover, security
Lang: en
Category: Security
Slug: encontrar-hosts-vivos-red
Summary: Methods and tools to discover active devices on local networks using nmap, arp-scan, netdiscover, and other reconnaissance techniques

Discovering **which devices are active** on your local network is a fundamental task for network administrators and security professionals. Here are the most effective techniques.

## Nmap: The Main Tool

### Basic Host Scan
```bash
# Simple Ping scan
nmap -sn 192.168.1.1/24

# Scan with specific TCP ports
nmap -sP -PS22,3389 192.168.1.1/24

# UDP scan for special devices
nmap -sP -PU161 192.168.1.1/24
```

**-sn**: Host discovery only, no port scan
**-PS**: TCP SYN discovery on specific ports
**-PU**: UDP discovery (useful for embedded devices)

### More Exhaustive Scans
```bash
# Full scan with OS detection
nmap -A 192.168.1.1/24

# TCP Connect Scan (less intrusive)
nmap -sT 192.168.1.1/24

# Firewall bypass with fragmentation
nmap -f -sS 192.168.1.1/24
```

## Alternative Tools

### arp-scan: ARP Based
```bash
# Local subnet scan
arp-scan 192.168.12.0/24

# With specific interface
arp-scan -I eth0 172.16.17.0/24

# Simplified local scan
arp-scan -l
```

**Advantage**: Works even with strict firewalls

### netdiscover: Passive/Active Discovery
```bash
# Active discovery
netdiscover -r 172.16.17.0/24

# Passive mode (listen only)
netdiscover -p

# Fast mode
netdiscover -f -r 192.168.1.0/24
```

### fing: Mobile Scanner
```bash
# Fast scan
fing -r 1

# With manufacturer details
fing -o table,csv
```

## Post-Scan Verification

### Check ARP Table
```bash
# View current ARP table
arp -a -n

# On modern systems
ip neigh show

# Clear and rescan
sudo arp -d -a
ping -c 1 192.168.1.{1..254}
arp -a
```

## Advanced Techniques

### Wireshark for Passive Analysis
1. Capture traffic on the network interface
2. Filter by ARP: `arp`
3. Analyze broadcast traffic
4. Identify devices by traffic patterns

### Automation Scripts
```bash
#!/bin/bash
# Full local network scan
echo "Scanning network..."
nmap -sn $(ip route | grep -E "^192|^10|^172" | awk '{print $1}' | head -1)
echo "Verifying ARP..."
arp -a -n | grep -v "incomplete"
```

## Important Considerations

### Firewall Limitations
- **Some devices** block ping/ICMP
- **Corporate firewalls** may filter scans
- **Different ports** may reveal "hidden" devices

### Legal Considerations
⚠️ **Authorization needed**: Only scan your own networks
⚠️ **Corporate policies**: Verify before scanning in enterprise environments

### Optimization by Network Type
```bash
# Home network (routers, IoT)
nmap -sn --min-rate 1000 192.168.1.1/24

# Corporate network (servers, stations)
nmap -sP -PS80,443,22,3389 10.0.0.0/8

# Industrial network (embedded devices)
nmap -sP -PU161,502 172.16.0.0/12
```

The **combination of multiple techniques** provides the most complete picture of active devices on your network.

*Original source*: [Information Security Stack Exchange](http://security.stackexchange.com/questions/36198/how-to-find-live-hosts-on-my-network)
