# IS 404 — Ethernet (2025-09-30) — Study Guide

## Overview

This packet combines the session’s conceptual review of Ethernet (data link layer behavior, CSMA/CD, MACs, ARP, switches) with the hands-on RJ-45 cable lab (stripping, ordering, crimping, testing). Use this guide to review what you must know for quizzes and to practice the concrete cable-making and troubleshooting steps demonstrated in class.

## Outline

1. **Media access methods & network topologies (CSMA/CD vs. control/token)**
   Understand how Ethernet uses contention (CSMA/CD) to share a medium, how control/token approaches differ, and how topology (bus, star, ring, mesh) affects collisions and reliability.
   - Explain CSMA/CD with the phone-conversation analogy: listen first, transmit if idle, detect collision, back off and retry.
   - Identify when collisions are likely (hubs, bus topology) and why modern switched/full-duplex Ethernet minimizes collisions.
   - Compare contention (Ethernet) vs. control/token approaches (token ring/token bus) and list one advantage and one disadvantage of each.
   - Given a topology diagram, label which links are single collision domains (hub/bus) and which break collision domains (switch/star).

2. **Data link layer responsibilities, frames, and encapsulation**
   Be able to name frame components, explain per-hop behavior, and show how headers are added/removed as packets move down/up the stack.
   - Label the parts of an Ethernet frame (preamble, MAC header, payload, FCS) and state the purpose of the preamble (synchronization).
   - Demonstrate encapsulation order: Application → Transport (TCP) → Network (IP) → Data link (Ethernet) and where 'frame' vs 'packet' terminology applies.
   - Explain per-hop header replacement: the IP header stays end-to-end while the Ethernet source/destination MAC is removed and re-created at every hop (use the class AABB → CCDD → EEFF example).
   - State the typical Ethernet MTU (~1500 bytes) and the role of fragmentation when payloads exceed the MTU.

3. **MAC addresses, ARP, and next-hop resolution**
   Know MAC address format and allocation, how ARP resolves IP → MAC for the next hop, and the router's role in re-encapsulating frames.
   - Describe a MAC as a 6-byte (48-bit) hardware address and parse it into OUI (first 3 bytes) and device identifier (last 3 bytes).
   - Explain MAC spoofing and MAC randomization on Wi‑Fi as privacy/security behaviors.
   - Use ARP: given an IP next-hop, show how the sender obtains the destination MAC and builds the Ethernet header.
   - Trace a packet’s journey: sender constructs frame for next-hop MAC → router strips frame and looks up next hop → router adds new frame with new MACs and forwards.

4. **Switches, hubs, and patch panels — where forwarding happens**
   Differentiate passive wiring (patch panel/hub) from active switching logic, and understand how switches reduce collisions and forward frames using MAC tables.
   - Define a patch panel as passive wiring (no forwarding logic) and a switch as an active device with MAC learning/forwarding tables.
   - Describe how a switch breaks collision domains and forwards frames only to the port matching the destination MAC (except broadcasts).
   - Given a small network example, predict whether a frame will be forwarded to one port, flooded, or blocked (based on switch learning state).
   - Inspect physical hardware examples: identify the patch panel ports vs. switch ports and explain why the switch is the "brainy" device.

5. **Physical media, limits, and PoE**
   Remember practical constraints (cable categories, maximum lengths, fiber differences) and when to choose each medium.
   - Default to Cat5e for classroom cables (supports 1 Gbps); choose Cat6/Cat6A when 10 Gbps is required and distances are appropriate.
   - Observe the ~100 meter maximum for copper Ethernet runs; explain why fiber is used for longer runs or higher speeds.
   - List pros/cons of fiber: much higher bandwidth/longer distance but higher cost and fragility (don't crimp fiber in the same way).
   - Note PoE capability: copper Ethernet can provide power plus data if both ends support PoE standards.

6. **Hands-on RJ-45 cable lab: materials, wiring order, crimping, testing, and troubleshooting**
   Follow the exact step sequence and wiring standard used in class (T568B); use testers and simple troubleshooting flows to produce a working cable.
   - Gather materials: Cat5e (recommended), RJ-45 plugs, 8P crimper, wire stripper/snips, cable tester, trash can for trimmings, and safety glasses if desired.
   - Cut cable to length (<100 m), strip outer sheath carefully (do not nick inner conductors), untwist pairs only as much as needed (~½"–1"), and straighten wires.
   - Arrange wires in T568B left→right with clip away: 1 white/orange, 2 orange, 3 white/green, 4 blue, 5 white/blue, 6 green, 7 white/brown, 8 brown — confirm order before inserting.
   - Trim ends even, insert fully into RJ-45 (clip away, light orange left), ensure conductors reach the connector tip, then crimp firmly in the 8-pin slot.
   - Repeat on the other end using the same T568B ordering, then plug both ends into the cable tester and expect LEDs to light 1→8 in order on both displays.
   - Troubleshoot: if LEDs are out of order or missing, re-crimp firmly; if still wrong, cut off the connector and redo. If conductors were nicked, cut back and restart.
   - Safety & practice: keep blades away from hands, discard small clippings immediately, conserve cable stock, and keep the same wiring standard on both ends.

7. **Administrative follow-ups & next steps**
   Act on required logistics and recommended prework for upcoming material; use provided resources to reinforce learning.
   - Sign up for the mandatory data center tour via the Slack/Sign-up Genius link and provide netID/phone as instructed.
   - Watch the recommended Wi‑Fi videos before the next class to prepare for wireless medium access discussion.
   - Expect a Wireshark/packet capture demo after more layering is covered; review session slides and recordings available on Slack.
   - If desired, request the printable RJ-45 checklist or encapsulation diagram offered by the instructor for quick reference.


## Key Vocabulary

**CSMA/CD**: Carrier Sense Multiple Access with Collision Detection — a contention-based media access method: listen before transmitting, detect collisions, back off, and retry.

**MAC address**: Media Access Control address — a 6-byte (48-bit) hardware identifier for a network interface; first 3 bytes are the vendor OUI, last 3 bytes identify the device.

**Frame**: The data link layer unit of transmission (Ethernet frame) containing the data link header (MAC addresses, preamble), payload, and trailer (FCS).

**ARP**: Address Resolution Protocol — the method for translating an IP next-hop address into the MAC address required to build an Ethernet frame for that link.

**Switch**: An active networking device that learns MAC-to-port mappings and forwards frames only to the destination port, thereby breaking up collision domains.

**Patch panel**: A passive wiring panel that simply provides physical terminations and cable organization; it does not perform frame forwarding or any switching logic.

**MTU**: Maximum Transmission Unit — the largest payload size (commonly ~1500 bytes for Ethernet) that can be carried in a single frame without fragmentation.

**Preamble**: A synchronization pattern at the start of an Ethernet frame (e.g., alternating bits ending with 10101011) used to align sender and receiver clocks before the frame.

## Review Questions

1. Explain CSMA/CD using the phone-conversation analogy and describe why modern switched, full-duplex Ethernet rarely experiences collisions.
2. Draw or describe the encapsulation steps (Application → Transport → Network → Data link). Explain which headers change at each hop and why the Ethernet header must be recreated by routers.
3. List the T568B wiring order left-to-right (clip away) and write the exact step-by-step procedure you would follow to make and test a 1-meter cable.
4. Given a network with a hub, a switch, and three hosts, predict how a broadcast frame and a unicast frame are handled differently by the hub versus the switch.
5. Describe how ARP works: when a host needs to send an IP packet to a next-hop, what steps occur to get the MAC address and transmit the frame?
6. Compare Cat5e, Cat6, and fiber in terms of typical use cases, bandwidth, and distance limits. When would you choose fiber over copper?
7. A cable tester shows LED sequence 1,2,3,4,5,6,8,7. Identify the likely mistake and outline the quickest corrective action(s).
8. What is the purpose of the Ethernet preamble and how does MTU size relate to fragmentation and performance?
