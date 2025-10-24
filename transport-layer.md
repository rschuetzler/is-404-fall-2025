# IS 404 — Transport Layer (October 23, 2025)

## Overview

This packet summarizes how the transport layer delivers network packets to the correct application using ports, the practical differences between TCP and UDP, and how transport addressing ties to lower-layer addresses (MAC/IP). It also collects deployment/security guidance (firewalls, NAT) and a hands-on troubleshooting checklist with concrete commands and examples (Nginx, SSH, DNS, streaming, QUIC).

## Outline

1. **Role of the Transport Layer & Demultiplexing**
   Explain how the transport layer hands delivered IP packets to the correct process on a host (demultiplexing) and how multiple application streams are combined for outbound traffic (multiplexing). Introduces the kernel socket mappings and the 5-tuple that identifies flows.
   - Define demultiplexing: use the destination port (and protocol) in the TCP/UDP header to select the receiving process.
   - Remember the 5-tuple: (source IP, source port, destination IP, destination port, protocol) uniquely identifies a transport flow.
   - OS kernel maintains socket table mapping (local IP, local port, protocol) to processes — only one listener per tuple unless special socket options are used.
   - Example: Nginx listens on TCP port 80 → kernel forwards incoming TCP segments for that port to the Nginx process.
   - Action: When designing a service, choose a stable server port and ensure clients target that port (explicit port in URL e.g., http://host:8080/ if nonstandard).

2. **Layered Addressing Recap**
   Contrast addressing at each layer so you can reason about where a problem lives (physical, data link, network, transport).
   - Physical layer: raw signals, no addressing — check cables/radio when physical faults are suspected.
   - Data link layer: MAC addresses used for link-local frames; routers swap MACs each hop, so MACs are only meaningful on the local link.
   - Network layer: IP addresses used for end-to-end host routing; NAT can rewrite IP/port pairs.
   - Transport layer: ports (16-bit) select application endpoints; same numeric port values exist separately for TCP and UDP.

3. **Ports, Binding Behavior, and Port Space**
   Cover the 16-bit port field, common ranges, binding semantics (bind/listen), interface scope (0.0.0.0 vs specific IP vs 127.0.0.1), and binding conflicts.
   - Port ranges and semantics: well-known 0–1023 (e.g., 22 SSH, 80 HTTP, 443 HTTPS), registered 1024–49151, ephemeral/dynamic 49152–65535 (OS-dependent).
   - Binding: servers call bind(); TCP servers then call listen() and accept(); UDP servers bind() and use recvfrom()/sendto().
   - Interface binding: bind to 0.0.0.0 to listen on all interfaces, to a specific IP to restrict to that interface, or to 127.0.0.1 to restrict to loopback (no external access).
   - Port conflict: two processes cannot bind the same (IP, port, protocol) tuple; check for 'address already in use' and identify conflicting process.
   - Actionable checks: run ss -tulwn | grep PORT or netstat -tulnp or lsof -i :PORT to find which process is listening.

4. **TCP vs UDP — Tradeoffs and Use Cases**
   Contrast the features, overhead, and common use cases of TCP and UDP so you can choose the right transport for a service or troubleshoot behavior (latency, loss, ordering).
   - TCP: connection-oriented, 3-way handshake (SYN, SYN-ACK, ACK), sequence numbers, ACKs, retransmissions, flow control (window), congestion control. Use for web (HTTP/HTTPS), SSH, databases, file transfer.
   - UDP: connectionless, best-effort, minimal header (source/dest ports, length, checksum), no ordering/retransmission/flow control at transport layer. Use for DNS queries, real-time media (RTP/VoIP), gaming, and as a substrate for QUIC/HTTP/3.
   - Header sizes: UDP header ~64 bits (minimal); TCP header ~160 bits (more overhead for reliability features).
   - When to choose: prefer TCP when in-order, reliable delivery is required; choose UDP when low latency and application-level handling of loss/ordering is acceptable.
   - Modern example: QUIC runs on UDP to get faster connection setup and implements reliability/congestion control in user space (used by HTTP/3).

5. **Practical Deployment, Security, and NAT**
   Operational guidance for opening ports, configuring firewalls/security groups, NAT/port-forwarding, and minimizing exposure of management services.
   - Always specify protocol in firewall rules — opening TCP/80 does not open UDP/80. Configure rules for the exact (protocol, port) pair.
   - Stateful vs stateless rules: TCP connections can be tracked by stateful firewalls; UDP is often stateless and may require connection tracking timeouts or explicit rules for return traffic.
   - NAT and port forwarding: configure external→internal mapping including protocol and internal port; verify the NAT device rewrites both IP and port as needed.
   - Minimize exposure: restrict SSH (TCP/22) to admin IP ranges or VPNs, enable strong auth rather than relying on obscure ports.
   - Action: Document nonstandard ports and update client configs; include protocol in cloud security group entries (e.g., allow inbound TCP 443 from 0.0.0.0/0).

6. **Troubleshooting Checklist & Tools**
   Step-by-step operational checklist and commands to diagnose unreachable or misbehaving services, for both TCP and UDP trouble cases.
   - Step 1 — Is the process bound/listening? Run ss -tulwn | grep PORT, netstat -tulnp, or lsof -i :PORT and inspect application logs for 'address already in use'.
   - Step 2 — Is it bound to the expected interface? Confirm 0.0.0.0 vs specific IP vs 127.0.0.1 using ss/netstat; adjust bind config if needed.
   - Step 3 — Are firewall/security-group rules permitting the (protocol, port) from your client network? Check host firewalls (ufw, iptables, firewalld) and cloud security groups.
   - Step 4 — NAT / port forwarding correct? Verify external port maps to correct internal IP/port and protocol on the router/NAT device.
   - Step 5 (TCP) — Is the TCP handshake completing? Capture packets with tcpdump/tshark/wireshark and look for SYN→SYN-ACK→ACK or RSTs.
   - Step 5 (UDP) — Are datagrams arriving? Use packet capture to confirm arrival and check intermediate devices that might drop stateless UDP.
   - Tools and commands: tcpdump -i iface port 80, wireshark for GUI captures, ss/netstat/lsof to inspect sockets, check app logs for binding errors.

7. **Socket API & Implementation Notes**
   Practical socket calls and consumer/producer behavior developers and operators should know (bind, listen, accept, connect, send/recv, sendto/recvfrom) and ephemeral port behavior.
   - Server TCP flow: socket(), bind(), listen(), accept() → per-connection sockets used to send/recv.
   - Client TCP flow: socket(), connect(), then send()/recv(); OS assigns ephemeral source port for the client side.
   - UDP: socket(), bind() optional for a client; servers typically bind() and use recvfrom()/sendto().
   - Ephemeral ports: clients use ephemeral ports chosen by the OS (e.g., 49152–65535) so multiple outbound connections can coexist.
   - Action: When writing or debugging code, log the local bind address/port and check that client-side ephemeral ports are not being blocked by firewall/NAT rules.

8. **Concrete Examples & Application-specific Notes**
   Pull together recurring in-lecture examples (Nginx, SSH, DNS, streaming, QUIC) with common failure modes and concrete mitigations.
   - Nginx: default binds TCP 80/443. If Nginx won't start, run ss -tulwn | grep :80 to find conflicts; check firewall for TCP/80 blocking even when Nginx is running.
   - SSH: default TCP 22. If unreachable, confirm sshd is running and bound to the right interface; restrict via firewall rules or move behind VPN for admin access.
   - DNS: usually UDP port 53 (fast, single-datagram); large responses or zone transfers fall back to TCP port 53.
   - UDP-based streaming: expect packet loss and reordering; implement buffering, forward error correction (FEC), or adaptive bitrate to smooth playback.
   - QUIC/HTTP3: runs over UDP to reduce handshake RTTs; be prepared to implement reliability and congestion control at the application layer.
   - Action: When documenting deployments, include protocol, port, binding interface, and firewall rule examples so operations and developers align.


## Key Vocabulary

**Transport layer**: The layer that delivers data between applications on end hosts using ports and transport protocols (e.g., TCP, UDP).

**Port**: A 16-bit numeric identifier in TCP/UDP headers that selects the receiving application endpoint on a host (range 0–65535).

**Socket**: OS abstraction that ties together an IP address, port, and protocol so an application can send and receive network traffic.

**Bind**: An operation where a process tells the OS to associate a socket with a specific (IP, port, protocol) so it can receive traffic for that tuple.

**Demultiplexing**: The transport-layer process of delivering incoming segments/datagrams to the correct application/process based on port and protocol.

**TCP (Transmission Control Protocol)**: A connection-oriented transport protocol providing reliable, in-order delivery with flow control and congestion control (uses 3-way handshake).

**UDP (User Datagram Protocol)**: A connectionless, best-effort transport protocol with minimal header overhead and no built-in retransmission, ordering, or flow control.

**Well-known ports**: Port numbers 0–1023 typically assigned to standard services (e.g., 22 SSH, 80 HTTP, 443 HTTPS).

**Ephemeral ports**: Temporary client-side source ports assigned by the OS (commonly in 49152–65535) for outbound connections.

**5-tuple**: The combination (source IP, source port, destination IP, destination port, protocol) that uniquely identifies a transport flow.

**NAT (Network Address Translation)**: A mechanism that rewrites IP addresses and ports on packets, often used to map private hosts to public IPs and requiring correct port forwarding for inbound services.

**Firewall / Security group**: Host or network rule sets that allow or block traffic based on protocol, port, and source/destination; must specify protocol (TCP vs UDP) and port.

**Three-way handshake**: TCP connection setup sequence: SYN (client) → SYN-ACK (server) → ACK (client) to establish a reliable session.

**QUIC**: A modern transport protocol that runs over UDP and implements connection setup, reliability, and congestion control in user space (used by HTTP/3).

## Review Questions

1. Explain demultiplexing at the transport layer: which header fields and OS mappings are used to deliver a packet to the correct process?
2. How does binding to 0.0.0.0 differ from binding to 127.0.0.1, and how can that affect access from remote clients?
3. Compare TCP and UDP: list three features that TCP provides that UDP does not, and give one concrete application example for each protocol.
4. Why must firewall/security-group rules specify both protocol and port? Give a real example that demonstrates a protocol mismatch causing a service outage.
5. You cannot reach a web server on TCP/80 though the process is running. List a concise troubleshooting sequence (commands and checks) you would perform.
6. What is an ephemeral port and why do clients use ephemeral ports when initiating outbound connections?
7. Describe how QUIC (HTTP/3) uses UDP differently than RTP/VoIP and what responsibilities the application takes on when using UDP-based transports.
