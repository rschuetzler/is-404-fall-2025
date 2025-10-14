# IS 404 — IP Addressing (Session: October 14, 2025)

## Overview

This study guide summarizes IPv4 addressing fundamentals, how to compute network/broadcast addresses and host counts (with decimal shortcuts and the binary bitwise AND), how IPs are used for forwarding (routing, ARP, default route) and NAT, and the hands‑on AWS EC2 workflow demonstrated in class. Use this to practice the required /8, /16, /24 calculations, follow the AWS lab steps, and prepare for next topics (DHCP and IPv6).

## Outline

1. **Notation & basic IPv4 concepts**
   Understand how addresses and masks are written and the common prefixes you must know for exams. Know special prefixes and what they represent.
   - Read IP addresses as 32‑bit values shown in dotted‑decimal (four octets) or in CIDR form: IP/prefix (e.g., 192.168.3.55/24).
   - Memorize common masks and their dotted forms: /8 = 255.0.0.0, /16 = 255.255.0.0, /24 = 255.255.255.0.
   - Recognize special prefixes: /0 (default route), /32 (single host), /30 (2 usable hosts); only /8,/16,/24 must be computed by hand on exams.
   - Practice converting between CIDR prefix length and dotted‑decimal mask for the three required prefixes.

2. **Decimal shortcut for network, broadcast, and host counts**
   Use the quick decimal method for /8, /16, /24 to compute network and broadcast addresses and the usable host count. The formula generalizes to any prefix.
   - Compute network address: for each octet, if mask octet = 255 → copy IP octet; if mask octet = 0 → network octet = 0.
   - Compute broadcast address: set all host octets (those mask octets = 0) to 255.
   - Compute usable hosts: hosts = 2^(32 − prefix) − 2 (examples: /8 → 2^24 − 2, /16 → 2^16 − 2, /24 → 2^8 − 2).
   - Work through examples until fluent: 11.59.33.0/8 → network 11.0.0.0, broadcast 11.255.255.255; 159.26.99.253/16 → network 159.26.0.0, broadcast 159.26.255.255; 192.168.3.55/24 → network 192.168.3.0, broadcast 192.168.3.255.

3. **Binary method: bitwise AND (how machines compute it)**
   Understand the 32‑bit binary view: the network address = IP AND mask. Binary thinking explains why the decimal shortcut works and how hosts decide on‑link vs off‑link.
   - Convert each octet to 8‑bit binary and AND it with the mask octet: e.g., 192.168.3.55 & 255.255.255.0 → 192.168.3.0.
   - Practice performing a bitwise AND on one /24 example to connect the decimal shortcut to the binary operation.
   - Remember: every outbound packet triggers this network/mask check to choose whether the destination is on‑link or must go to a gateway.

4. **Routing, longest‑prefix match, ARP, and packet flow**
   Know how hosts and routers use routing tables and ARP to forward packets, and when the default route is used.
   - Explain routing table entries as prefix → next hop/interface and apply longest‑prefix (most specific) match to pick the route.
   - If destination matches a local prefix → send directly on the link; otherwise send to the default gateway (0.0.0.0/0).
   - Use ARP to map IPv4 → MAC on the local broadcast domain: send ARP request (broadcast), receive ARP reply (unicast), and cache the mapping.
   - Describe packet flow: compute network (AND) → determine next hop → ARP to resolve next‑hop MAC → transmit frame; routers do not forward link‑layer broadcasts.

5. **Public vs private addressing and NAT**
   Distinguish private (non‑routable) blocks from public addresses and understand how NAT allows private hosts to communicate on the Internet.
   - Memorize private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 and know these are not routable on the public Internet.
   - Describe NAT behavior: rewrite source (and possibly port) at the edge, maintain NAT table mappings, and demultiplex return traffic to internal hosts.
   - Apply the classroom implication: EC2 instances can have public or Elastic IPs; typical home devices use private IPs behind NAT.

6. **AWS Academy Learner Lab — EC2 hands‑on workflow & commands**
   Follow the step‑by‑step lab workflow shown in the demo to launch an Ubuntu EC2, secure keys, SSH in, and install nginx. Note lab-specific constraints.
   - Start the Learner Lab early (first start may take 5–15 minutes) and use Chrome or Firefox (Safari is unreliable).
   - Launch an Ubuntu instance (t3.micro or as instructed), download the provided key pair (.pem), move it to ~/.ssh and secure it: chmod 400 keyfile.pem.
   - (Optional) Allocate and associate an Elastic IP to keep a stable public IP across stops/starts.
   - SSH into the instance: ssh -i ~/path/to/keyfile.pem ubuntu@<public-ip>, then run sudo apt update; sudo apt install nginx -y; sudo systemctl start nginx and verify http://<public-ip> in a browser.
   - Work within the ~4 hour auto‑shutdown window, save work often, and keep the keyfile safe (lost key requires new key/image).

7. **Study & exam guidance; connections and next topics**
   Focus study on what will be tested (/8,/16,/24 calculations) and reinforce both decimal and binary methods; prepare for DHCP and IPv6 next.
   - Practice the three required manual calculations until both decimal shortcut and binary AND feel natural.
   - On exams you may present host counts as powers of two (e.g., 2^24 − 2) — that is acceptable.
   - Preview DHCP (dynamic addressing) and IPv6 (128‑bit addressing, /64 conventions, neighbor discovery) before the next class.


## Key Vocabulary

**IPv4**: Internet Protocol version 4 — a 32‑bit addressing system for IP networks.

**CIDR (Classless Inter‑Domain Routing)**: Notation IP/prefix-length that indicates the network prefix (e.g., 192.0.2.1/24).

**Prefix length**: The number of contiguous 1 bits in the subnet mask (for example, 24 in /24).

**Dotted‑decimal subnet mask**: A 32‑bit mask expressed as four octets (e.g., 255.255.255.0 for /24) that separates network and host bits.

**Network address**: The address representing the network portion of an IP where host bits are zeroed (e.g., 192.168.3.0 for a /24).

**Broadcast address**: The address with all host bits set to 1 on a subnet; used to reach all hosts on that subnet (e.g., 192.168.3.255 for /24).

**Bitwise AND**: A binary operation (IP & mask) used by hosts/routers to compute the network address from an IP and mask.

**ARP (Address Resolution Protocol)**: Protocol that maps an IPv4 address to a link‑layer MAC address on the local broadcast domain.

**NAT (Network Address Translation)**: Edge device function that rewrites private source addresses (and ports) to a public IP, allowing many private hosts to share one public address.

**Elastic IP**: An AWS static public IP you can allocate to your account and associate with an EC2 instance so the public IP persists across stops/starts.

**SSH key pair**: Cryptographic key pair (private .pem file + public key) used for key‑based authentication to Linux instances (e.g., ssh -i key.pem ubuntu@IP).

**Default route (0.0.0.0/0)**: A routing table entry used to forward packets when no more specific route matches; typically points to the default gateway.

## Review Questions

1. Using the decimal shortcut, compute the network address, broadcast address, and number of usable hosts for 203.0.113.45/24. Show your steps.
2. Repeat the same calculations for 198.51.100.7/16 and for 11.59.33.0/8. Explain why 11.190.255.39/8 is on the same network as 11.59.33.0/8.
3. Explain how a host uses bitwise AND to decide whether a destination IP is on‑link or off‑link. Demonstrate with the binary representation for 192.168.3.55/24.
4. Describe the sequence of actions (routing table lookup, ARP) a host performs when sending a packet to an off‑link destination. What is the role of the default route?
5. List the private IPv4 ranges covered in class and explain how NAT lets hosts in those ranges reach the public internet.
6. What prefixes are you required to compute by hand on exams, and how should you present host counts if you prefer not to compute the full decimal number?
