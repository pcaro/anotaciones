Title: The Story Behind X-Forwarded-For and X-Real-IP
Date: 2015-10-21 23:05
Tags: headers, x-forwarded-for, x-real-ip, proxy, nginx
Lang: en
Category: Networking
Slug: historia-x-forwarded-for-x-real-ip
Summary: Analysis of X-Forwarded-For and X-Real-IP headers, their origins, differences, and how to determine the client's real IP in architectures with multiple proxies

Determining the **client's real IP** in proxy architectures is more complex than it seems. The `X-Forwarded-For` and `X-Real-IP` headers have different purposes and limitations.

## X-Forwarded-For: The Full Chain

### Format and Purpose
```
X-Forwarded-For: client, proxy1, proxy2
```

- **Tracks the original IP** of the client through multiple hops
- **Accumulates IPs** as it passes through proxies
- **Not mandatory** for all proxies

### Critical Limitations
⚠️ **Easily forgeable**: A client can add fake IPs
⚠️ **Potentially unreliable** for determining the real IP

## X-Real-IP: The Direct Approach

### Characteristics
- **Less documentation** officially available
- **Commonly used** alongside X-Forwarded-For
- **Simpler approach** to passing the client IP

### Limitation
> "Not many good info or specs about this one" - No definitive standards

## Recommended Nginx Configuration

To extract the most accurate IP:

```nginx
# Configure known proxies
set_real_ip_from 10.0.0.0/8;
set_real_ip_from 172.16.0.0/12;
set_real_ip_from 192.168.0.0/16;

# Enable recursive processing
real_ip_recursive on;

# Use X-Forwarded-For as source
real_ip_header X-Forwarded-For;
```

## The Real Challenge

**Determining the "real" client IP is inherently complex** due to:

1. **Multiple network hops**
2. **Uncooperative proxies**
3. **Potential IP spoofing**
4. **Lack of uniform standards**

## Best Practices

1. **Validate trusted sources** of headers
2. **Correctly configure** known proxies
3. **Do not blindly trust** client headers
4. **Implement logging** for debugging

**Real reliability** depends more on your network architecture than on the specific headers used.

*Original source*: [Distinct Place](http://distinctplace.com/infrastructure/2014/04/23/story-behind-x-forwarded-for-and-x-real-ip-headers/)
