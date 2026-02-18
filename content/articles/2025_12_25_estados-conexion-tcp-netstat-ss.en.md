---
title: TCP Connection States in GNU/Linux: netstat and ss
date: 2025-12-25 13:30
tags: linux, networking, tcp, netstat, ss, systems
lang: en
category: Systems
slug: estados-conexion-tcp-netstat-ss
summary: Understand the different TCP connection states reported by netstat and ss, from establishment to termination, for better network diagnosis.
---

In the GNU/Linux world, tools like `netstat` and `ss` are indispensable for monitoring and diagnosing the state of network connections on our systems. To correctly interpret their output, it is fundamental to understand the different states a TCP connection goes through. This post explores those states, from establishment to termination of a connection.

## Phases of a TCP Connection

A TCP connection is managed through three main phases:

1.  **Connection Establishment**: A multi-step handshake process that initiates the connection.
2.  **Data Transfer**: Once established, data is sent between the two endpoints.
3.  **Connection Termination**: Closes the connection and releases associated resources.

During these phases, the Internet socket (the local endpoint of the communication) experiences a series of state changes.

## TCP Socket States Explained

Here are the most common states you might encounter when listing connections with `netstat` or `ss`:

*   **ESTABLISHED**: The TCP connection is established and ready to transfer data. This is the desired state for an active connection.
*   **SYN_SENT**: The local socket has sent a SYN packet to the remote server and is waiting for a SYN-ACK response. Indicates that a connection attempt is being made.
*   **SYN_RECV**: The server has received a SYN packet from a client and has responded with a SYN-ACK, now waiting for an ACK from the client. It is part of the three-way handshake.
*   **FIN_WAIT1**: The local socket has closed its side of the connection and has sent a FIN packet, waiting for an ACK from the remote peer. The connection is closing actively.
*   **FIN_WAIT2**: The local socket has received the ACK to its FIN, but is still waiting for a FIN packet from the remote peer to fully close the connection.
*   **TIME_WAIT**: The socket has waited after closing the connection to ensure that all packets have been transmitted and received by both sides, and to allow duplicate packets to die out in the network. It is a necessary wait state before fully releasing resources.
*   **CLOSE**: The socket is not in use and there is no connection.
*   **CLOSE_WAIT**: The remote peer has closed its side of the connection (sent a FIN and been ACKed), and the local socket is waiting for the local application to close its own side.
*   **LAST_ACK**: The local socket has sent its FIN to the remote peer, and is waiting for the final ACK from the remote peer. This happens after a `CLOSE_WAIT`.
*   **LISTEN**: The socket is waiting for incoming connections. Only seen with the `--listening (-l)` or `--all (-a)` options of `netstat`/`ss`.
*   **CLOSING**: Both sides of the connection have tried to close simultaneously, and the local socket is in the process of sending/receiving FIN and ACK.
*   **UNKNOWN**: The socket state is unknown or cannot be determined.

## Tools: `netstat` and `ss`

You can see these states using commands like:

```bash
netstat -tn   # Shows TCP connections, without name resolution (-n)
ss -tn        # Modern and faster version of netstat
```

The `-t` option filters for TCP connections and `-n` avoids name resolution, which speeds up the output and shows IPs directly.

## Conclusion

Understanding TCP connection states is vital for diagnosing network issues, identifying unresponsive or stuck processes, and understanding how applications behave in terms of connectivity. Knowing what each state means allows you to debug problems more effectively on your GNU/Linux system.

*Original article*: [Tipos de Conexiones en netstat y ss Explicadas](https://www.ochobitshacenunbyte.com/2020/11/07/tipos-de-conexiones-en-netstat-y-ss-explicadas/)
