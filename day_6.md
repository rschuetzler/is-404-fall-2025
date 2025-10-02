# Data Link Layer, Ethernet, and Switching – Review Guide

## 1. Data Link Layer Basics
- **Role**: Manages access to the physical medium (wires, radio waves).  
- **Scope**: Concerned only with **device-to-device delivery** on the same physical link (my computer → my router, router → next router, etc.).  
- **Encapsulation**: Adds a **data link header** containing source and destination **MAC addresses** to packets.  
- **Terminology**:  
  - **Frame** = a packet at the data link layer.  
  - **Packet** = generic term across layers.  

---

## 2. Packets and Encapsulation
- Every communication on a network is broken into **packets** (webpages, images, video streams).  
- As data moves down the stack:  
  - Application data (e.g., HTTP request)  
  - + Transport header (TCP/UDP)  
  - + Network header (IP)  
  - + Data link header (MAC addresses) → sent as bits on the physical layer.  
- On arrival: headers are removed in reverse order.  

---

## 3. MAC Addresses
- **Definition**: Media Access Control addresses, 48 bits (6 bytes), written in hexadecimal.  
- **Assignment**: Burned into each network interface card (NIC) at manufacture.  
- **Uniqueness**: The first 3 bytes = manufacturer (organization ID); last 3 bytes = device-specific.  
- **Devices**: Phones, laptops, routers, Bluetooth devices all have one (or multiple).  
- **Use**: Identify devices within a local network; change at each hop as the packet travels.  

---

## 4. Ethernet and CSMA/CD
- **Ethernet**: The dominant data link protocol.  
- **Access Method**: **CSMA/CD** (Carrier Sense Multiple Access with Collision Detection).  
  - **Carrier Sense**: Listen first before sending.  
  - **Multiple Access**: Many devices share the medium.  
  - **Collision Detection**: If two talk at once, stop, wait a random time, retry.  
- **Today**: Collisions are rare with **full duplex Ethernet** and switches, but the logic is still in the standard.  

---

## 5. Ethernet Frames
- **Structure**:  
  - **Preamble**: synchronization (alternating 1s and 0s).  
  - **Destination MAC address**  
  - **Source MAC address**  
  - **Length/Type field** (IPv4, IPv6, etc.)  
  - **Payload** (IP header, TCP header, application data)  
  - **Pad** (if needed to reach minimum length)  
  - **CRC (Cyclic Redundancy Check)**: error detection (if error found, frame discarded).  

---

## 6. Network Topologies
- **Bus**: All devices share one cable; a single break can disable the network.  
- **Ring**: Each device connected in a loop; one break = failure.  
- **Star**: All devices connect to a central device (hub or switch).  
- **Mesh**: Devices connected to many others; reliable but expensive.  

---

## 7. Hubs vs. Switches
- **Hub**:  
  - Physical layer device (no intelligence).  
  - Forwards every incoming signal to all ports.  
  - Creates one large **collision domain**.  
- **Switch**:  
  - Data link layer device.  
  - Uses MAC address table to forward frames only to the correct port.  
  - Each port is its own **collision domain**, reducing collisions.  
  - Still part of the same **broadcast domain**.  
- **Switch Features**: Managed vs. unmanaged, backplane speed, quality of service (QoS), power over Ethernet (PoE).  

---

# Review Questions

### Data Link Layer & Packets
1. What is the main responsibility of the data link layer?  
2. How does the data link layer differ from the network layer in scope of delivery?  
3. What is a frame, and how does it relate to a packet?  
4. In what order are headers added and then removed from a packet?  

### MAC Addresses
5. What is a MAC address, and how is it assigned?  
6. Why might a single laptop have more than one MAC address?  
7. What are the two parts of a MAC address, and what do they represent?  

### Ethernet & CSMA/CD
8. What does CSMA/CD stand for, and how does it work?  
9. Why are collisions less common in modern switched networks?  
10. What is the difference between half-duplex and full-duplex Ethernet communication?  

### Ethernet Frames
11. What is the purpose of the preamble in an Ethernet frame?  
12. Which fields in the Ethernet frame hold addressing information?  
13. How does the cyclic redundancy check (CRC) help detect errors?  

### Topologies & Devices
14. Compare bus, ring, star, and mesh topologies. Which are most common today?  
15. How does a hub differ from a switch in terms of collision domains and broadcast domains?  
16. What does a switch’s MAC address table do?  
17. What is the difference between a managed and an unmanaged switch?  
18. Why is “backplane speed” important when evaluating switches?  
19. What is Power over Ethernet (PoE), and why is it useful?  
