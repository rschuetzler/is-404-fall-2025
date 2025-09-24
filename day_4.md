# Networking Models & Interlayer Communication – Review Guide

## 1. Outline of Main Topics

### A. Purpose of Networks
- Networks allow computers/devices to communicate and share information.
- Internetworks (like the Internet) connect multiple networks together.

### B. Why Networking Models Exist
- Provide a **framework** for understanding how networks work.
- Define a **division of responsibilities** between layers.
- Enable **interoperability** by standardizing functions, making protocols interchangeable.

### C. Major Networking Models
1. **OSI Model**
   - 7 layers: Physical, Data Link, Network, Transport, Session, Presentation, Application.
   - More detailed, but often considered overly complex.

2. **TCP/IP Models**
   - **4-layer model**: Application, Transport, Internet, Network Access.
   - **5-layer model**: Application, Transport, Internet, Data Link, Physical.
   - Commonly used today; simplifies OSI by combining some upper layers.

### D. Functions of the Layers (TCP/IP 5-Layer Model)
1. **Physical Layer** – Moves bits across a medium (cables, Wi-Fi, radio, fiber).  
2. **Data Link Layer** – Handles local network communication, MAC addresses, error detection, media access control. Examples: Ethernet, Wi-Fi.  
3. **Internet Layer** – Handles addressing and routing across networks (IP, ICMP).  
4. **Transport Layer** – Provides reliability and application-to-application delivery (TCP, UDP). Uses **ports** to identify applications.  
5. **Application Layer** – Provides application-specific protocols (HTTP, SMTP, DNS, etc.).

### E. Encapsulation and Interlayer Communication
- Each layer adds its own header (like nested envelopes) when sending data.
- On receipt, layers remove (decapsulate) their headers in reverse order.
- Within a device: each layer communicates with the one above and below.  
- Across devices: communication is **peer-to-peer at the same layer** (e.g., transport ↔ transport).

### F. Routing and Network Devices
- Routers operate at the **Internet layer (Layer 3)** – forward packets between networks.
- Switches operate at the **Data Link layer (Layer 2)** – connect devices within a local network.
- NICs and wires form the **Physical/Data Link layers**.

### G. Importance of Protocols and Standards
- **Protocols = instructions** for how data is transmitted.  
- Standards ensure interoperability (e.g., TCP/IP, Ethernet, HTTP).
- Analogy: Like road signs or building codes, standards make systems predictable and compatible.

### H. Life Cycle of a Network Request (Slide examples)
- Application creates request (e.g., HTTP GET to Instagram).  
- Transport (TCP) splits data into packets.  
- Internet (IP) finds the next hop.  
- Data Link + Physical send across the medium.  
- Routers pass packets across multiple hops.  
- Web server receives, processes, and sends back a response.

---

## 2. Review Questions

### Networking Basics
1. What is the fundamental purpose of a network?  
2. What is the difference between a network and an internetwork (like the Internet)?  

### Networking Models
3. Why do networking models exist? List at least two reasons.  
4. How many layers are in the OSI model, and what are their names?  
5. What are the layers of the 5-layer TCP/IP model?  
6. How do the 4-layer and 5-layer TCP/IP models differ?  

### Layer Responsibilities
7. What is the role of the **physical layer**? Give two examples of technologies at this layer.  
8. What addressing system is handled at the **data link layer**?  
9. What addressing system is handled at the **internet layer**?  
10. What is the difference between a MAC address and an IP address?  
11. What is the main role of the **transport layer**, and how do ports help achieve this?  
12. What is the main function of the **application layer**? Give two examples of application protocols.  

### Encapsulation and Communication
13. What is encapsulation, and how is it like envelopes inside envelopes?  
14. How does data move within a device (up and down the stack)?  
15. How does data move across devices (peer-to-peer communication at the same layer)?  
16. Which layers directly communicate with the transport layer within a single device?  
17. Which layers are involved in routing messages across a network?  

### Protocols and Standards
18. Why are protocols important in networking?  
19. Give one example of how standards outside of networking (e.g., roads, accounting, construction) make life easier.  
20. What might be a downside of standards? Give an example.  

### Applied Understanding
21. Walk through the **life cycle of a network request** (e.g., visiting Instagram). Which layer is responsible at each stage?  
22. If TCP decides to split a large message into packets, which layer is responsible for determining the best path for those packets?  
23. When a router forwards a packet, which layers does it operate at?  
