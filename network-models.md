# IS 404 — Network Models (Session: September 23, 2025)

## Overview

This session introduced core networking concepts centered on the five‑layer TCP/IP teaching model and followed a concrete packet walkthrough (HTTP → TCP → IP → data‑link → physical). It also covered real infrastructure and devices (NICs, switches, routers, fiber), routing basics (next‑hop, BGP), related services (DNS, CDN, VPN, Starlink), and practical course and troubleshooting guidance (exam/skillcheck, VM/NGINX, Slack help etiquette).

## Outline

1. **Instructor demo & the productivity lesson about AI**
   Instructor demonstrated a small private web app built quickly with AI to illustrate how modern tools accelerate targeted developer tasks without replacing core coding skills.
   - Describe the demo: a keyboard‑driven app to find student videos and match orphaned uploads to records.
   - Note the meta‑point: use AI to speed repetitive coding tasks; still verify and understand generated code.
   - Apply the lesson: break small automation tasks into concrete goals before prompting an AI tool.

2. **Help etiquette and writing good troubleshooting requests**
   Follow a reproducible format when asking for help on Slack, in office hours, or with ChatGPT to get faster, accurate assistance.
   - Always paste the exact error message and relevant command or code lines (copy/paste, not a phone photo).
   - Report the environment: VM vs host OS, service name (e.g., NGINX), and steps taken before the error.
   - List what you already tried and include screenshots using native OS tools (e.g., Snipping Tool or Shift+Cmd+4).
   - Be responsive to follow‑up questions; when using ChatGPT mirror the same structure: context, goal, attempts, errors.

3. **Immediate course logistics and action items**
   Keep track of Exam 1, SkillCheck 1 (NGINX on your VM), upcoming physical labs, and the data‑center tour signups — act now to avoid late penalties or VM issues.
   - Prepare for Exam 1: covers material through Thursday; 30 questions; no hard time limit but expect ~20–30 minutes to finish.
   - Set up and keep your VM: install and configure NGINX as the SkillCheck due next weekend; use lab machines if your laptop cannot run a VM.
   - Sign up for the data‑center tour (Oct 7–8) when Slack signups open and bring questions for the cable/cabinet activities.
   - Keep screenshots, recordings, and Slack bookmarks for study and TA review sessions (TA review Friday 1 p.m.).

4. **Layered networking model and packet flow (concrete walkthrough)**
   Understand the five teaching layers (Application → Transport → Network → Data‑link → Physical) and follow an HTTP request as it is wrapped and unwrapped through each layer.
   - Map layers to examples: Application=HTTP, Transport=TCP/UDP, Network=IP, Data‑link=Ethernet/Wi‑Fi framing, Physical=electrical/fiber/radio.
   - Walk through a request: browser builds HTTP request → TCP adds ports/seq → IP adds addresses/next‑hop → Ethernet/Wi‑Fi frames → NIC transmits bits on the wire or radio.
   - Use traceroute to observe hop‑by‑hop forwarding and note that routers choose the next hop locally (paths can change per packet).
   - Recognize the 'narrow waist': many apps use TCP/UDP and IP sits in the center, enabling diverse upper and lower layers to interoperate.

5. **Protocols, standards, and real‑world analogies**
   Differentiate a protocol (a set of communication rules) from a standard (a widely adopted protocol) and use analogies to remember their role and limitations.
   - Define and compare: protocol = instructions (how to talk); standard = a protocol adopted broadly so different systems interoperate.
   - Recall analogies used in class: church disaster checklist for protocols; USB‑C and road signs for physical standards.
   - Understand inertia: widely adopted standards (e.g., TCP/IP) provide stability but are hard to change—this constrains future design choices.

6. **Infrastructure and devices: NICs, switches, routers, patch panels, fiber, and Wi‑Fi APs**
   Identify the physical components that form a network, their responsibilities, and how they connect in a typical building wiring closet or data center.
   - Explain device roles: NICs convert frames to signals; switches aggregate ports and forward Ethernet frames at layer 2; routers forward packets between networks using IP at layer 3.
   - Describe wiring closets: patch panels terminate cables, which connect to switches; fiber provides uplinks to campus backbone or the Internet.
   - Recognize Wi‑Fi APs as the last wireless hop with a wired uplink to the switch/fiber backbone.
   - Inspect examples from class: open a wiring closet and identify floor patch panels, the switch, and fiber uplinks.

7. **Routing, addressing, and DNS**
   Know how IP addressing and routing work locally and globally, including how addresses change across networks and how DNS resolves names to addresses.
   - Explain IP addressing: devices obtain addresses scoped to a network (addresses change when you move between networks); static IPs are special cases tied to an ISP or admin assignment.
   - Describe routing: routers consult routing tables and run routing protocols (e.g., BGP between domains) to decide the next hop for a packet.
   - Use DNS before sending packets: name resolution converts hostnames (www.example.com) to IP addresses that the IP layer uses.
   - Be aware of routing security: BGP hijacks show how route advertisements can be misused and why routing security matters.

8. **Upper‑level services: VPNs, CDNs, Starlink, and encryption**
   Understand how value‑added services change traffic path, privacy, and performance characteristics on top of the basic network model.
   - Explain VPNs: they encrypt traffic between your device and a VPN endpoint, altering source appearance and routing beyond the VPN endpoint.
   - Use CDNs: know that CDNs cache content closer to users to reduce latency and long‑haul traffic (example: many websites use CDNs for images and scripts).
   - Note satellite services: Starlink acts like a moving Wi‑Fi layer and can change latency and IP addressing compared with fiber.
   - Always prefer HTTPS for web traffic: encryption prevents eavesdropping even on open Wi‑Fi; recognize where firewalls or middleboxes might still inspect or block traffic.

9. **Practical debugging tools and developer notes**
   Use browser dev tools, traceroute, and packet capture tools for diagnosis; follow basic system and permission practices when working on the VM or server.
   - Inspect HTTP with browser dev tools: open Network tab to view requests, sizes, and timing for page assets.
   - Run traceroute to identify hops and measure per‑hop latency; use Wireshark for deeper packet captures when allowed.
   - Check NGINX status on your VM and common commands (example workflow): install NGINX, start the service, view /var/log/nginx/error.log, and check firewall rules if unreachable.
   - Respect file permissions: use appropriate privilege escalation (sudo) only when necessary and keep your VM until grading is complete.


## Key Vocabulary

**Layered (TCP/IP) model**: A hierarchy of five teaching layers (Application, Transport, Network, Data‑link, Physical) that divides networking responsibilities and enables interoperability.

**Protocol**: A defined set of rules for communication (how endpoints exchange messages) such as HTTP or TCP.

**Standard**: A protocol that has been widely adopted so different systems interoperate (e.g., Ethernet, IPv4).

**IP (Internet Protocol) address**: A network‑layer identifier for a device on a particular network (IPv4 or IPv6) used as the destination for routing packets.

**TCP (Transmission Control Protocol)**: A transport‑layer protocol that provides reliable, ordered, connection‑oriented delivery of a byte stream between endpoints.

**UDP (User Datagram Protocol)**: A lightweight transport‑layer protocol that provides connectionless, best‑effort delivery without guaranteed ordering or reliability.

**Router**: A layer‑3 network device that forwards IP packets between different networks by choosing the next hop using routing tables and protocols.

**Switch**: A layer‑2 device that forwards Ethernet frames between ports based on MAC addresses and often aggregates endpoints within a LAN.

**BGP (Border Gateway Protocol)**: The interdomain routing protocol used by autonomous systems on the Internet to advertise and select routes for IP prefixes.

**CDN (Content Delivery Network)**: A distributed system of cache servers that store content closer to users to reduce latency and offload origin servers.

## Review Questions

1. Trace an HTTP GET request from your browser to a web server using the five teaching layers; list what headers/addresses or encapsulation change at each step (Application → Transport → Network → Data‑link → Physical).
2. Explain the difference between a protocol and a standard and give one real‑world analogy used in class that helps you remember each concept.
3. When asking for help about a failing NGINX instance on your VM in Slack, list exactly what information you should include to make it easy for a TA to reproduce and diagnose the problem.
4. Compare TCP and UDP: describe one scenario where TCP is needed and one where UDP is preferable, and explain why.
5. How does a router decide where to forward a packet? Include the role of IP destination addresses, routing tables, and routing protocols.
6. Describe three components you would inspect in a building wiring closet and what each component does (patch panel, switch, fiber uplink).
7. What does a CDN do to improve performance, and how can traceroute or a browser's Network tab help you confirm content is being served from a CDN?
