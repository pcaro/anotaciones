---
title: `docker-http-https-echo`: An Essential Tool for Network Debugging
date: 2025-12-25 14:15
tags: docker, http, https, debugging, networking, tools, containers
lang: en
category: Tools
slug: docker-http-https-echo
summary: `mendhak/docker-http-https-echo` is a simple Docker container that facilitates debugging network configurations, proxies, and load balancers.
---

In the complex world of distributed applications, debugging network issues, proxies, load balancers, or firewall rules can be an arduous task. We need a simple way to verify what a server is receiving. This is where a tool like `mendhak/docker-http-https-echo` becomes indispensable.

## What is `mendhak/docker-http-https-echo`?

It is an extremely lightweight and simple Docker container that functions as an "echo" HTTP and HTTPS server. Its main function is to **respond to any HTTP or HTTPS request with a detailed description of the request itself**. This includes:

*   Request headers.
*   HTTP method (GET, POST, PUT, etc.).
*   Request URL and parameters.
*   Request body.
*   Remote IP address of the client.
*   TLS/SSL information (if HTTPS).

## Why is it useful?

This type of echo server is invaluable for a variety of debugging scenarios:

*   **Proxy and Load Balancer Debugging**: Verify if a reverse proxy or load balancer is rewriting headers, modifying URLs, or passing the request body as you expect.
*   **Firewall and Security Rules**: Confirm that traffic is reaching the correct destination and is not being blocked or altered.
*   **HTTP/HTTPS Header Inspection**: Useful to see exactly what headers your client or a specific application sends.
*   **Integration Testing**: A predictable target for automated tests of how different services communicate via HTTP/HTTPS.
*   **Mixed Content Diagnosis**: You can use it to verify if HTTP resources are loading correctly in an HTTPS context.

## How to Use It

Using it is straightforward via Docker:

### For HTTP (port 8080)

```bash
docker run -p 8080:8080 mendhak/http-https-echo
```

Then, you can access `http://localhost:8080` with your browser or `curl`:

```bash
curl http://localhost:8080/path?query=value -H "X-Custom-Header: test"
```

### For HTTPS (port 8443)

To use HTTPS, you must map the container's HTTPS port. The image already comes with a self-signed certificate for testing.

```bash
docker run -p 8443:8443 mendhak/http-https-echo
```

Access `https://localhost:8443` (your browser may warn you about the self-signed certificate).

## Conclusion

`mendhak/docker-http-https-echo` is one of those simple but incredibly useful tools that every developer and system operator should have on hand. It facilitates understanding network flows and speeds up debugging connectivity issues in any container-based environment.

*Original repository*: [mendhak/docker-http-https-echo on GitHub](https://github.com/mendhak/docker-http-https-echo)
