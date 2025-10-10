# IS 404 — Network Layer (Oct 09, 2025) Study Guide

## Overview

This packet combines the administrative actions you must take now (Exam 2 deadlines, review sessions, AWS signup) with the core network-layer fundamentals illustrated in lecture and the data-center tour. Use the actionable checklist and practice commands to confirm you understand routing, ARP, IPv4 special addresses, and the packet lifecycle before the quiz.

## Outline

1. **Exam 2 logistics & immediate study actions**
   What to do now, how the exam is structured, and the recommended study flow so you meet deadlines and study efficiently.
   - Complete Exam 2 before the testing center closes Monday at 6:00 PM; note a $5 fee applies if you test after 11:00 AM Monday.
   - Expect 30 multiple-choice questions (about ~20 new, ~10 review); use past exams (Slack Bookmarks → Past Exams) for practice.
   - Follow the recommended study flow: read AI summaries (Slack Bookmarks → AI summaries) → rewatch pre-class videos (Network layer, IPv4 Special Addresses) → work review problems → attend or watch the TA review (Zach, 1:00 PM).
   - Confirm AWS Academy signup via your BYU email so you can access upcoming labs.

2. **Network layer purpose & separation of concerns**
   High-level role of IP and how it pairs with lower layers; focus on logical addressing and forwarding across multiple networks.
   - Describe the network layer as responsible for end-to-end logical addressing (IP) and routing packets from source to destination across networks.
   - State that routers are the workhorses: they consult routing tables and choose the next hop toward the destination.
   - Differentiate IP (network layer, global or network scope) from the data-link layer (MAC addresses, link-local scope).
   - Explain that the network layer 'does its best' for delivery (no guarantees); reliability is handled by the transport layer (e.g., TCP).

3. **Routing, routing tables, next hop, and default routes**
   How devices decide where to send packets: routing table fields, metrics, default route behavior, and common routing protocols.
   - Identify routing table fields: destination prefix (network), subnet mask/CIDR, next-hop (gateway) IP, outgoing interface, and metric.
   - Interpret the default route (0.0.0.0/0) as 'send elsewhere' when no specific prefix matches—hosts send off-link packets to this gateway.
   - Compare metrics: use them to prefer routes (simple example: hop count; realistic metrics include bandwidth, delay, and policy).
   - Name typical routing protocol roles: IGPs (OSPF, RIP, EIGRP) inside an AS; BGP for inter-AS reachability on the Internet.
   - Practice: run route print (Windows) or netstat -rn / ip route show (macOS/Linux) and identify your default gateway and interface.

4. **ARP (Address Resolution Protocol) and ARP cache**
   Mechanics and scope of ARP: how a host learns link-layer addresses for a next hop and why ARP is link-local.
   - Explain ARP's job: map a next-hop IP address to a MAC address so frames can be sent on the local link.
   - Describe ARP request/reply behavior: broadcast an ARP request ('Who has IP X? Tell MAC Y') and receive a unicast ARP reply with the MAC.
   - Show how to inspect the ARP cache: arp -a (Windows/macOS/Linux) or ip neigh (Linux); note entries time out and are refreshed on demand.
   - Demonstrate: ping a host on your subnet to force an ARP and then re-run arp -a to see the new mapping.

5. **Packet lifecycle across hops (step-by-step)**
   Concrete sequence from application data down to frames, across routers, and up to the destination transport layer.
   - Trace the encapsulation: Application → Transport (TCP/UDP segment) → Network (IP packet with final destination IP) → Data-link (frame with next-hop MAC).
   - Perform routing lookup: host checks its routing table; if off-link, send to default gateway; if on-link, next hop = destination.
   - Use ARP for the next hop: check ARP cache; if absent, broadcast ARP request, receive reply, cache mapping, then build frame.
   - Observe forwarding: each router decrements TTL, consults its routing table, obtains next-hop MAC via ARP if needed, then forwards with new source/destination MACs while IP addresses remain unchanged.
   - Confirm delivery: destination host accepts the IP packet and hands payload to the transport layer (TCP handles acknowledgements/retransmissions).

6. **IPv4 special addresses & addressing notes**
   Memorize key reserved ranges and their behaviors; know what is routable versus private and common uses.
   - Memorize private ranges: 10.0.0.0/8; 172.16.0.0/12 (172.16.0.0–172.31.255.255); 192.168.0.0/16.
   - Remember loopback: 127.0.0.1 (localhost) — traffic never leaves the host; test with ping 127.0.0.1.
   - Recognize broadcasts: 255.255.255.255 is the limited broadcast; each subnet also has a directed broadcast (e.g., x.y.z.255 for a /24).
   - Understand 0.0.0.0 uses: indicate an unspecified address or represent the default route in routing tables; private addresses are not routable on the public Internet without NAT.

7. **Practical lab commands & exercises**
   Hands-on tasks to verify your understanding using routing and ARP inspection plus packet capture if available.
   - Inspect routing: run route print (Windows) or netstat -rn / ip route show (macOS/Linux); identify the default route and the interface used.
   - Inspect ARP: run arp -a (or ip neigh); then ping an on-subnet host to populate the cache and re-check entries.
   - Test loopback and off-subnet behavior: ping 127.0.0.1 (loopback) and ping an off-subnet IP; note ARP to the default gateway for off-subnet traffic.
   - Capture traffic: use tcpdump or Wireshark to capture ARP requests/replies and to watch source/destination MAC changes at each hop (e.g., tcpdump -i <iface> arp or capture ICMP across a router).

8. **Data-center tour — physical context and design implications**
   How physical infrastructure and operational choices shape network design, redundancy, and routing policies at scale.
   - Relate redundancy to routing: identify redundant power, dual ISPs, and duplicate network links that routing and failover policies must accommodate.
   - Connect physical placement to performance: recognize that cooling choices and high-density racks influence where high-performance network equipment is located.
   - Map logical design to physical constraints: plan IP addressing, segmentation, and routing policies to align with cable tunnels, access-control restrictions, and rack topology.
   - Observe archival and storage systems (tape libraries) as examples of services that require reliable network connectivity and sometimes dedicated storage networking.

9. **Study checklist and next steps**
   Concrete checklist so you don't miss administrative tasks and targeted study before the next class on subnetting.
   - Finish Exam 2 within the testing-center deadline; watch for the $5 fee window if testing late Monday.
   - Read AI class summaries, rewatch the Network Layer and IPv4 Special Addresses videos, and review the Day 8 PDF diagrams.
   - Attend or watch the recorded TA review (Zach, 1:00 PM) and practice the commands listed in the Practical section.
   - Confirm AWS Academy invite on your BYU email and prepare questions about CIDR and prefix math for Tuesday's class on subnetting.


## Key Vocabulary

**Network layer (IP)**: OSI layer responsible for logical addressing and forwarding packets between networks (routing).

**Router**: Device that forwards packets between networks by consulting a routing table and selecting the next hop.

**Routing table**: Local table of destination prefixes, next-hop gateway, outgoing interface, and metrics used to decide packet forwarding.

**Default route (gateway)**: Fallback route (0.0.0.0/0) used when no more specific route matches a destination; directs off-link traffic to a gateway.

**Next hop**: The IP address of the next device (often a router) to which a packet is forwarded on its way to the destination.

**Metric**: Numeric value used to compare and prefer routes (examples: hop count, bandwidth, delay, administrative cost).

**ARP (Address Resolution Protocol)**: Protocol that maps an IP address to a MAC address on the same local link via broadcast requests and unicast replies.

**ARP cache / ARP table**: Local cache of IP→MAC mappings (inspectable with arp -a) that reduces repeated ARP traffic; entries expire over time.

**IP address**: Logical endpoint address used at the network layer; can be public (routable) or private (RFC 1918, not routable on the public Internet).

**MAC address**: Layer-2 hardware address used for frame delivery on a local link; meaningful only within a single broadcast domain.

**Loopback**: Special IPv4 address block (127.0.0.1) used for host-internal communication; traffic to loopback never leaves the host.

**TTL (Time To Live)**: IP header field decremented at each hop to prevent routing loops; packets are dropped when TTL reaches zero.

## Review Questions

1. What exact steps should you take (and in what order) to prepare for Exam 2 according to the session recommendations?
2. Explain how a host sends its first packet to an off-subnet IP: include routing lookup, ARP behavior, frame construction, and what the default route is used for.
3. Using route print (or netstat -rn / ip route show), how do you identify the default gateway and which interface will carry off-link traffic? Give a concrete example command and what to look for in the output.
4. Describe the ARP request/reply exchange. What is broadcasted, what replies, and how can you view the result on your machine?
5. List the three RFC 1918 private IPv4 ranges and explain why a private address cannot be routed on the public Internet without NAT.
6. As a packet traverses multiple routers from your laptop to a remote server, which addresses change at each hop and which remain constant? Explain why.
7. From the data-center tour context: name two physical or operational realities that influence network design and describe how they affect routing or redundancy decisions.
