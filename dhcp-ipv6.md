# IS 404 — DHCP, IPv6, and Servers (Oct 16, 2025) — Study Guide

## Overview

This session connected DHCP (how hosts get addressing), IPv6 (addressing changes and deployment choices), and server/addressing practices (how services are hosted and reached). The recorded DHCP and IPv6 videos are the canonical technical walkthroughs — re-watch them, bring targeted questions to section/office hours, and use the practical tasks below to prepare for upcoming DNS and transport modules.

## Outline

1. **Canonical materials and session purpose**
   Know that the recorded DHCP and IPv6 videos contain the packet-level walkthroughs; live section time clarified operational choices and hosting mental models. Your immediate goal is to re-watch those recordings, extract timelines, and use live time for targeted questions.
   - Re-watch the assigned DHCP and IPv6 videos first — they are the authoritative technical walkthroughs.
   - Use section/office hours for clarification and operational context after reviewing recordings.
   - Prepare specific questions (e.g., how giaddr is set, SLAAC vs DHCPv6 tradeoffs) before attending live help.

2. **DHCP: purpose, DORA flow, leases, options, and relay**
   DHCP dynamically supplies hosts with IP configuration. Understand the DORA handshake, lease lifecycle, common options and reservations, how relays enable multi-subnet deployments, and basic operational/security traps.
   - Describe the DORA exchange: broadcast DHCPDISCOVER → server DHCPOFFER → client DHCPREQUEST → server DHCPACK (or DHCPNAK).
   - Explain lease lifecycle: clients RENEW before expiry, REBIND if renew fails, and RELEASE when leaving; administrators set lease durations to match environment (short for guest networks, long for stable servers).
   - List and configure common DHCP options: router (default gateway), DNS servers, subnet mask (IPv4), hostname, NTP, and vendor options.
   - Create DHCP reservations (static mappings) by linking a device MAC to a fixed IP for servers or devices that need predictable addresses.
   - Use DHCP relay agents to forward client broadcasts across subnets; verify giaddr is populated so the server can allocate addresses for the correct subnet.
   - Mitigate risks: scan for rogue DHCP servers, avoid misconfigured gateway/DNS options, and combine DHCP with switch port security or 802.1X where authentication is needed.

3. **DHCPv6 and IPv6 autoconfiguration: SLAAC vs stateful DHCP**
   IPv6 supports multiple configuration models: SLAAC (stateless) and DHCPv6 (stateful). Router Advertisements (RAs) control which method hosts use; operations choose the model that fits control, privacy, and management goals.
   - Identify SLAAC behavior: host derives an address from router-advertised prefix and its interface identifier (or generates privacy addresses) without contacting a DHCP server for the address itself.
   - Identify DHCPv6 (stateful): server assigns addresses and options (DNS, etc.) similar to IPv4 DHCP when centralized control is desired.
   - Read RA flags on the network: use the M and O bits (or equivalent router settings) to decide whether hosts should use DHCPv6, SLAAC, or both (e.g., SLAAC for addresses + DHCPv6 for DNS).
   - Choose operational models: pick SLAAC for lightweight autoconfiguration, DHCPv6 when you need central address state or reservations (note DHCPv6 supports reservations differently than IPv4 DHCP).
   - Practice: configure a test host to prefer SLAAC vs DHCPv6 and observe the resulting addresses and DNS configuration.

4. **IPv6 fundamentals: format, common prefixes, notation, privacy, and transition**
   IPv6 uses 128-bit addresses written in colon-hex form with compression rules. Know link-local, global unicast, ULA, and multicast prefixes; understand privacy address options and coexistence/transition strategies with IPv4.
   - Write and compress IPv6 addresses: eight 16-bit hex fields separated by colons (example: 2001:0db8:85a3::8a2e:0370:7334); omit leading zeros and use :: once for contiguous zeros.
   - Memorize common prefixes and uses: link-local fe80::/10 for on-link functions, global unicast 2000::/3 for public routing, ULA fc00::/7 for internal-only addressing, and multicast ff00::/8.
   - Explain privacy vs EUI-64 identifiers: configure temporary (privacy) addresses to reduce tracking; understand tradeoffs for server stability vs client privacy.
   - Plan for coexistence: use dual-stack (IPv4+IPv6) commonly; be familiar with tunneling (6in4, 6to4, Teredo historically) and translation (NAT64/DNS64) where needed.

5. **Servers, addressing, hosting mental models, and DNS link**
   Decide how services are addressed and made reachable: static addresses or DHCP reservations for stability; public vs private addressing impacts reachability; DNS maps names to addresses and is the next topic to study.
   - Assign stable addresses to servers with manual static config or DHCP reservations so services remain reachable.
   - Choose public/global addresses for Internet-reachable services (cloud VMs often use provider-assigned global unicast addresses) and private/ULA or RFC1918 addresses for internal services behind firewalls or NAT.
   - Relate hosting choices to addressing: cloud-hosted web services often live behind provider load balancers and use global addresses; internal databases use private addressing and access controls.
   - Prepare for DNS: use DNS to decouple service names from underlying address changes (e.g., update A/AAAA records when changing IPs), which reduces direct dependence on static addressing.

6. **Study checklist, hands-on practice, and references**
   Follow a focused study plan: re-watch recordings, create event timelines, perform hands-on packet captures and configuration, and consult RFCs and slides for deeper detail.
   - Re-watch the assigned DHCP and IPv6 videos and pause to create short timelines of the DORA exchange and IPv6 autoconfiguration events (RA → SLAAC or DHCPv6).
   - Use tcpdump or Wireshark to observe DHCP (DISCOVER/OFFER/REQUEST/ACK) on IPv4 networks and to capture Router Advertisements and SLAAC or DHCPv6 exchanges on IPv6 networks.
   - Create and verify a DHCP reservation for a VM or container; confirm address consistency across reboots.
   - Enable IPv6 on a test host, observe RAs, verify whether SLAAC creates addresses, and try configuring DHCPv6 for controlled addressing.
   - Read RFC 2131 (DHCP), RFC 8415 (DHCPv6), and RFC 8200 (IPv6) selectively for protocol details; review the course Day 10 slides and the assigned videos as primary resources.


## Key Vocabulary

**DHCP (Dynamic Host Configuration Protocol)**: A protocol that automatically assigns network configuration (IP address, subnet mask/gateway, DNS servers, and options) to hosts so they can join networks without manual setup.

**DORA**: Abbreviation for the common DHCPv4 handshake sequence: DHCPDISCOVER → DHCPOFFER → DHCPREQUEST → DHCPACK (the client-server message flow for address assignment).

**Lease**: A time-limited allocation of an IP address to a client by a DHCP server; leases must be renewed before expiry and may be rebound or released by the client.

**DHCP reservation (static mapping)**: A DHCP server configuration that binds a specific client hardware address (MAC) to a particular IP address so the client receives the same address reliably.

**DHCP relay (giaddr)**: A network device that forwards DHCP broadcast messages between clients and centralized DHCP servers across subnets; it sets the giaddr field so the server knows the client's subnet.

**SLAAC (Stateless Address Autoconfiguration)**: An IPv6 mechanism where hosts self-configure IP addresses from router-advertised prefixes and local interface identifiers (or privacy-generated IDs) without contacting a DHCP server for an address.

**DHCPv6**: The DHCP protocol designed for IPv6 that can provide stateful address assignment and configuration options (DNS, etc.), used when centralized control is required.

**Link-local address**: An IPv6 address in the fe80::/10 range usable only on the local link for neighbor discovery, router communication, and on-link functions.

**Global unicast address**: An IPv6 address in the 2000::/3 range intended to be globally routable on the public Internet (analogous to public IPv4 addresses).

**ULA (Unique Local Address)**: IPv6 addresses in fc00::/7 intended for local/private use within an organization (analogous to RFC1918 private IPv4 space).

**Router Advertisement (RA)**: ICMPv6 messages sent by routers to advertise network prefixes and flags that control SLAAC/DHCPv6 behavior on hosts.

**Privacy address**: Temporary IPv6 addresses generated by hosts to avoid long-term tracking of devices; they change over time and trade address stability for privacy.

**Dual-stack**: An operational model where hosts and networks run both IPv4 and IPv6 simultaneously to ensure compatibility during the transition period.

**Prefix delegation**: A mechanism (often used by ISPs) to assign IPv6 subnet prefixes to customers or downstream routers so they can create multiple subnets internally.

## Review Questions

1. Describe the DHCP DORA exchange (DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, DHCPACK) and explain what each message accomplishes.
2. Compare and contrast SLAAC and DHCPv6: how do they assign addresses and when would you prefer one over the other in an operational environment?
3. Explain the differences and typical uses of IPv6 link-local (fe80::/10), global unicast (2000::/3), and ULA (fc00::/7) addresses.
4. How does a DHCP relay enable a centralized DHCP server to serve clients on different subnets, and what is the role of the giaddr field?
5. Given a hosting scenario (cloud web server vs internal database), decide whether to use static IP, DHCP reservation, public/global address, or private addressing and justify your choice.
6. Show how to observe DHCP and IPv6 autoconfiguration in a lab: what tools and captures would you run to verify DHCP DORA and Router Advertisements leading to SLAAC or DHCPv6?
7. Describe two transition strategies for IPv6/IPv4 coexistence (one tunneling approach and one translation approach) and the typical operational reasons to use each.
