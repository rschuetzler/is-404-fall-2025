# Review Guide: Physical Layer & Encoding

## 1. Main Topics Covered

### A. Rubber Duck Debugging
- Technique where you explain code line by line to a duck (or object/person).
- Helps activate different cognitive processes than silent problem-solving.
- Still useful even with AI tools like ChatGPT.

---

### B. Physical Layer (Networking Model)
- **Role**: Lowest layer of networking; transmits raw bits across physical media.
- **Media**:
  - Copper cables: twisted pair, coaxial.
  - Fiber optic: transmits data using light.
  - Wireless: radio, microwaves, satellites, visible light (Li-Fi).
  - Power line networking: data through household electrical wiring.

---

### C. Bandwidth vs. Latency
- **Bandwidth**: Data capacity per second.
  - Cat5e ~1 Gbps  
  - Cat7 ~100 Gbps  
  - Undersea cables up to ~250 Tbps  
- **Latency**: Time for signal round trip (ping).
  - Increased by distance.
  - Geosynchronous satellites: ~22,000 miles away → higher latency.
  - Example: latency to Mars ≈ 38 minutes.

---

### D. Global Infrastructure
- Undersea fiber optic cables carry nearly all international internet traffic.
- Built and maintained by companies in consortia.
- Vulnerable to breaks or sabotage.
- Redundant connections prevent single failures from cutting off regions.

---

### E. Encoding & Modulation
- **Encoding**:
  - ASCII: 7-bit, English only.
  - Extended ASCII / ISO 8859: added accented characters.
  - Unicode: up to 4 bytes, supports global alphabets, symbols, emoji.
- **Codecs**: Encode/decode media (MP3, JPEG, H.264, etc.).
- **Modulation**:
  - Converts digital signals to analog and back.
  - AM: amplitude modulation.
  - FM: frequency modulation.
  - Used by modems for internet over analog mediums.

---

### F. Networking Hardware
- **Cables**:
  - Twisted pair: shielded/unshielded, reduces interference.
  - Coaxial: single core, uses frequencies.
  - Fiber optic: light-based, very high speed.
- **Devices**:
  - Repeaters: boost weak signals.
  - Hubs: old, broadcast to all devices.
  - Switches: smarter, send only to intended recipient.
  - Patch panels: organize cabling in network racks.

---

### G. Everyday Connections
- Classroom examples: laptops, phones, projectors, cameras, microphones, TVs, thermostats, fire alarms.
- Most surprising facts:
  - Nearly all internet traffic goes through wires.
  - Li-Fi is real but limited.
  - Fiber optic cables can be thinner than a strand of hair yet carry global internet traffic.

---

## 2. Review Questions

### Rubber Duck Debugging
1. What is rubber duck debugging, and why does it work?
2. Why might this still be useful even with AI tools?

---

### Physical Layer Basics
3. What role does the physical layer play in networking?
4. Name three physical media used to transmit data.
5. Why do we say “all data travels through wires” even when using Wi-Fi?

---

### Bandwidth & Latency
6. Define **bandwidth** and **latency**.
7. Give one example where bandwidth matters more than latency, and one where latency matters more.
8. Why is satellite internet often slower than fiber, even though radio waves travel at nearly the speed of light?

---

### Cables & Devices
9. What is the difference between twisted pair, coaxial, and fiber optic cables?
10. What do hubs, switches, and repeaters do? How are they different?
11. What is a patch panel used for?

---

### Encoding & Modulation
12. What are the main differences between ASCII, ISO 8859, and Unicode?
13. Why is Unicode important for emoji and multilingual communication?
14. What is modulation, and what do AM and FM stand for?

---

### Infrastructure & Security
15. What role do undersea cables play in global networking?
16. Why is it harder to tap fiber optic cables compared to copper wires?
17. What risks exist to undersea cables, and how do companies mitigate them?
