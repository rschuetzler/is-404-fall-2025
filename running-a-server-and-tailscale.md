# IS 404 — Servers at Home (2025-11-04)

## Overview

This study packet summarizes the practical checklist, networking fundamentals, NAT/port‑forwarding vs NAT‑bypass options (Tailscale/WireGuard, reverse tunnels), hardware/virtualization decisions, and security/maintenance practices covered in class. It also condenses the Wireshark packet‑capture demos into diagnostic steps so you can reproduce and debug home‑server reachability problems.

## Outline

1. **Hosting checklist — what you must arrange to expose a home service**
   A compact checklist of minimum requirements and concrete setup actions to make a service reachable from the Internet.
   - Confirm your router has a public, routable IP on the WAN; if the WAN IP is private (CG‑NAT), ordinary inbound port‑forwarding will not work.
   - Reserve a stable internal IP for your host: set a DHCP reservation (map device MAC → fixed IP in your router) or choose a static IP outside the DHCP pool.
   - Configure router port forwarding: map publicIP:port → internalIP:port (example: forward TCP/UDP 25565 → 192.168.1.25:25565 for a Minecraft server).
   - Publish a hostname: use dynamic DNS to update a DNS A/AAAA record when your public IP changes (or request a paid static IP from your ISP if available).
   - Choose always‑on hardware: Raspberry Pi (lightweight), mini‑PC/repurposed desktop (more CPU/RAM), or virtualized host (Proxmox) for many services.
   - Produce a security & maintenance plan: schedule OS/package updates, use SSH keys, configure host/network firewalls, enable backups and monitoring, and plan a UPS for critical devices.

2. **Core networking primitives — the sequence behind "visiting a website"**
   Understand the layered events (DHCP → ARP → DNS → TCP → NAT → HTTP/HTTPS) so you can map symptoms to root causes when troubleshooting.
   - Run DHCP to obtain IP, gateway, and DNS servers when a device joins the LAN.
   - Use ARP to resolve the MAC address of the next hop (your gateway) on the local link.
   - Perform DNS to convert a hostname (e.g., www.is404.net) into an A/AAAA record IP.
   - Observe TCP's three‑way handshake (SYN → SYN‑ACK → ACK) before application data flows.
   - Recognize NAT translates private IPs to the router’s public IP for outbound traffic; inbound flows require port maps or NAT‑traversal.
   - Distinguish HTTP (unencrypted; payload visible in captures) from HTTPS (encrypted; flow metadata visible).

3. **NAT, port forwarding, and CG‑NAT — traditional hosting path**
   How typical home NAT works, how to create port mappings, and why ISP‑level CG‑NAT blocks inbound access.
   - Explain NAT: map an external public IP to internal private IPs so many hosts share one public address.
   - Create port‑forwarding rules on your router to send incoming service ports to a chosen internal host and port.
   - Test port forwarding with an external client (or an online port‑check tool) and verify the internal host receives traffic.
   - Detect CG‑NAT: if your router's WAN IP is in a private range or differs from the IP shown by an external 'what is my IP' service, you are likely behind CG‑NAT.
   - If behind CG‑NAT, use NAT traversal alternatives (next section) or request a public IP from the ISP.

4. **NAT‑traversal alternatives — modern practical workarounds**
   Options when you cannot (or do not want to) rely on router port forwarding or when behind CG‑NAT.
   - Install Tailscale (WireGuard‑based mesh) on your home host and clients to achieve automatic NAT traversal and per‑device identity without router changes.
   - Set up reverse SSH tunnels or services like ngrok to create an outbound tunnel from the internal host to a public relay, then connect through that relay.
   - Request a public/static IP from your ISP (if available/affordable) to restore ordinary port‑forwarding behavior.
   - Weigh tradeoffs: tunnels/coordination services ease connectivity but introduce a trust and bandwidth decision (the relay/exit operator can see unencrypted exit traffic).

5. **VPN fundamentals and trust tradeoffs**
   How VPNs change packet paths and the differences between full‑tunnel and split‑tunnel modes.
   - Describe how a VPN client encrypts and forwards traffic to an endpoint; the endpoint's public IP is seen by external services.
   - Use full‑tunnel to route all traffic through the VPN exit node (good for privacy on untrusted networks; shifts trust to the VPN operator).
   - Use split‑tunnel to route only selected traffic through the VPN (useful for corporate resources while keeping general Internet traffic direct).
   - Consider operator trust: end‑to‑end encryption (HTTPS, SSH) protects payloads from the VPN operator, but they still see destination metadata for unencrypted traffic.

6. **Tailscale practical recipe and operational tips**
   Step‑by‑step Tailscale setup and important configuration and reliability considerations demonstrated in class.
   - Quick setup: sign up for Tailscale → install client on laptop and on home device (Pi/mini‑PC) → authenticate both to the same team → mark home device as an exit node if needed.
   - For headless/unattended nodes, disable key expiry so the device remains online without periodic reauthentication.
   - Use Tailscale device ACLs and per‑node identity to restrict access; designate exit nodes only when you trust their bandwidth and logging behavior.
   - Remember the caveat: Tailscale relies on coordination/bootstrap services for peer discovery; exit‑node traffic flows through the node you select (trust/bandwidth implications).

7. **Hardware, virtualization, and operational patterns**
   Selecting and operating always‑on devices, virtualization for many services, and power/network reliability best practices.
   - Choose hardware by workload: Raspberry Pi (lightweight services), mini‑PC or repurposed desktop (higher CPU/RAM), Proxmox for multiple VMs/containers and snapshots.
   - Prefer wired Ethernet for servers to reduce latency and avoid Wi‑Fi reliability issues.
   - Use Wake‑on‑LAN if you want to conserve power while still remotely starting a machine; test it before relying on it.
   - Deploy a UPS for critical always‑on hosts and ensure adequate cooling; schedule periodic snapshots and backups (local + offsite).

8. **Security, maintenance, and operations checklist**
   Concrete operational actions to keep a home server secure, available, and recoverable.
   - Apply OS and package updates regularly and automate where safe (e.g., unattended security updates for some Linux distros).
   - Harden access: use SSH key authentication, restrict SSH to specific users and ports, and close unused services/ports with host and router firewalls.
   - Monitor uptime and logs: set simple alerts for service downtime and centralize logs or forward critical alerts to your phone or email.
   - Implement backups and test restores: keep at least one offsite copy (cloud or remote) and verify recovery procedures periodically.
   - Avoid exposing admin interfaces to the public Internet; require VPN/Tailscale or IP‑restricted access for management endpoints.

9. **Packet capture & troubleshooting — practice with Wireshark**
   How to use packet captures to diagnose name resolution, connection establishment, and application behavior — reproduce the in‑class demos.
   - Capture name resolution: filter for DNS to see queries and A/AAAA responses and confirm the resolved IP matches expectations.
   - Observe TCP handshake: filter 'tcp.flags.syn == 1 && tcp.flags.ack == 0' to find SYNs, then track the SYN → SYN‑ACK → ACK sequence before application data.
   - Inspect HTTP flows: in unencrypted HTTP, use 'http' display filter to read GET/response contents; for HTTPS, inspect TLS ClientHello and SNI but not payload.
   - Use packet captures to distinguish causes: DNS failure vs TCP blocked by firewall vs application error (e.g., server not listening).
   - Practice: run Wireshark on a lab VM, visit a site, and step through DHCP (if applicable), ARP, DNS, TCP handshake, and HTTP to build intuition that 'it's all packets.'


## Key Vocabulary

**Public IP**: An IP address routable on the public Internet assigned to your router’s WAN interface; required for ordinary inbound connections.

**Private IP**: RFC 1918 addresses (10.x.x.x, 172.16–31.x.x, 192.168.x.x) used inside LANs and not routed on the public Internet.

**DHCP (Dynamic Host Configuration Protocol)**: Protocol that assigns IP configuration (IP address, gateway, DNS servers) to a host when it joins a network.

**ARP (Address Resolution Protocol)**: Protocol to resolve an IP address to a MAC address on the local Ethernet segment so frames reach the next hop.

**DNS (Domain Name System)**: Service that resolves human‑readable domain names to IP addresses (A/AAAA records) so clients can connect by address.

**Dynamic DNS**: A technique/service that updates a DNS record automatically when your public IP changes so a hostname keeps pointing to your home.

**NAT (Network Address Translation)**: Translates private internal IP addresses to a public IP (and vice versa) so many hosts can share one public address.

**CG‑NAT (Carrier‑Grade NAT)**: ISP‑level NAT that assigns private WAN addresses to customer routers and prevents customers from having unique public IPv4 addresses.

**Port forwarding**: Router rule that maps an incoming public port to a specified internal IP and port, enabling hosting services behind NAT.

**VPN (Virtual Private Network)**: An encrypted tunnel that sends client traffic to a remote endpoint; the endpoint’s public IP becomes the visible source for outbound connections.

**Full‑tunnel**: VPN mode that routes all client traffic through the VPN endpoint (useful for privacy on untrusted networks).

**Split‑tunnel**: VPN mode that routes only selected traffic through the VPN endpoint while other traffic goes directly to the Internet.

**WireGuard**: A modern, lightweight VPN protocol used as the transport for Tailscale and other VPN solutions.

**Tailscale**: A coordination service built on WireGuard that provides easy device discovery and automatic NAT traversal for peer‑to‑peer connections.

**Exit node**: A device configured to forward outbound traffic for other devices (used to create a full‑tunnel from the node to the Internet).

## Review Questions

1. List the minimum items in the hosting checklist you must complete to make a home service reachable from the Internet. Give a concrete example (ports and IPs) using Minecraft as the service.
2. Explain the sequence DHCP → ARP → DNS → TCP handshake → HTTP and describe what you would expect to see for each step in a packet capture when visiting a website.
3. How can you detect that your ISP has placed you behind CG‑NAT, and what are three practical alternatives to ordinary port‑forwarding when that happens?
4. Describe step‑by‑step how to set up Tailscale for an always‑on Raspberry Pi so you can reach it remotely, and name two operational caveats you should consider.
5. Compare full‑tunnel and split‑tunnel VPN modes: when would you choose each and what trust implications does each choice introduce?
6. Walk through the practical steps you would take to troubleshoot an external client failing to connect to your home Minecraft server (assume port forwarding is configured). Which packet filters/inspections would you run in Wireshark?
7. Name five security and maintenance practices you should adopt before exposing any home service to the Internet and explain why each is important.
