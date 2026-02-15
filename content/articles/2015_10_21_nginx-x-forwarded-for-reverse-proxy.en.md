Title: Nginx: Configuring X-Forwarded-For in Reverse Proxy
Date: 2015-10-21 23:05
Tags: nginx, reverse-proxy, x-forwarded-for, real-ip, configuration
Lang: en
Category: DevOps
Slug: nginx-x-forwarded-for-reverse-proxy
Summary: How to configure Nginx to pass the client's real IP to backend servers using the X-Forwarded-For header in reverse proxy configurations

When you use **Nginx as a reverse proxy**, you need the backend server to see the **client's real IP**, not the proxy's IP. The `X-Forwarded-For` header solves this problem.

## The Problem

Without configuration, the backend server only sees the Nginx proxy IP, losing crucial information about the real client for:
- Accurate **access logs**
- Correct **geolocation**
- **Rate limiting** by real IP
- Reliable **traffic analysis**

## Solution 1: Simple IP

```nginx
proxy_set_header X-Forwarded-For $remote_addr;
```

**Usage**: When Nginx is the only proxy in the chain.
**Result**: Header contains only the original client IP.

## Solution 2: IP Chain

```nginx
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
```

**Usage**: When there are multiple proxies in the chain.
**Result**: Preserves existing IPs and adds the current one.

## Practical Configuration

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

## Related Headers

- **X-Real-IP**: Most recent client IP
- **X-Forwarded-For**: Complete chain of IPs
- **X-Forwarded-Proto**: Original protocol (http/https)
- **Host**: Original hostname

## Verification

```bash
# On the backend server, check the headers
tail -f /var/log/apache2/access.log
# Or in your application
echo $_SERVER['HTTP_X_FORWARDED_FOR'];
```

## Security Considerations

⚠️ **Important**: X-Forwarded-* headers can be forged by clients. In production environments, ensure that only your proxy sets them.

This configuration is essential to maintain **full traceability** in reverse proxy architectures.

*Original source*: [Networking How To's](http://www.networkinghowtos.com/howto/set-the-x-forwarded-for-header-on-a-nginx-reverse-proxy-setup/)
