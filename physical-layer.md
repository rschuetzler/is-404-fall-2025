# IS 404 — Physical Layer (September 25, 2025)

## Overview

This study guide summarizes the Physical Layer session: how raw bits move across media (copper, fiber, radio, light), why latency and bandwidth differ, and what real networking hardware in a closet looks and feels like. Use this packet to focus your exam prep, lab readiness (Ethernet cable making on Tuesday), and practical skills from the demos.

## Outline

1. **What the Physical Layer Is**
   Defines the actual medium and connectors that carry signals; it transmits raw bits (electrical/optical/radio) but does not perform higher‑level functions like encryption or routing.
   - Describe the physical layer as the path for raw bits (electrical pulses, light, radio) between devices
   - Identify devices that operate at or touch the physical layer (NICs, repeaters/hubs, patch panels)
   - Distinguish the physical layer from data link (switches operate at layer 2; patch panels are passive)

2. **Closet hardware and hands‑on items**
   Understand the look and role of real equipment you touched in class (patch panel, RJ‑45, NIC, cables) and how that maps to theory.
   - Inspect a patch panel: note it has no power or logic — it's just punched‑down wires and ports
   - Handle RJ‑45 connectors to map 8 conductors/4 pairs to pinouts and terminations
   - Examine a NIC to see where the host meets the medium and explain how it encodes/decodes signals

3. **Common wired media and cable categories**
   Compare twisted‑pair, fiber, coaxial, and powerline in terms of distance, bandwidth, and use cases.
   - State Cat5e specs: 4 pairs, ≈1 Gbps typical, max run ≈100 m (328 ft)
   - State Cat6A specs: added separator/tighter twists, ≈10 Gbps over typical 100 m; higher categories (Cat7/8) add shielding and short‑range higher throughput
   - Describe fiber optic: light in glass cores, extremely high capacity (undersea cables 250–400 Tbps), repeaters roughly every ~50 miles for long spans
   - Explain coax: single conductor with shielding used for cable TV/internet, multiplexes via frequency bands
   - List powerline networking as a fallback: use household wiring but expect higher attenuation and lower reliability than Ethernet

4. **Wireless, LiFi, satellites, and shared medium behavior**
   Cover Wi‑Fi coordination, line‑of‑sight techs, and satellite tradeoffs between latency and network complexity.
   - Explain that Wi‑Fi APs serialize transmissions (only one client transmits at an instant even if it appears simultaneous)
   - Compare LiFi (visible light, high throughput but room‑level line‑of‑sight) vs Wi‑Fi (radio, better ubiquitous coverage)
   - Compare satellite types: geosynchronous (~22,000 miles, high latency) vs LEO (Starlink ≈300–350 miles, lower latency but needs many moving satellites)
   - Recommend wired backhaul or mesh with wired backbone for consistent throughput where possible

5. **Latency vs Bandwidth — intuition, numbers, and real examples**
   Differentiate time (latency) from capacity (bandwidth); memorize representative numbers and analogies used in class.
   - Define latency as time (commonly RTT) and bandwidth as bits per second (bps); emphasize independence
   - Memorize example numbers: ~193 ms best‑case RTT opposite side of Earth via fiber; ~38.94 minutes RTT to Mars (example), geosync ≈22,000 miles, Starlink LEO ≈300–350 miles
   - Use analogies: pigeon/hard‑drive = high bandwidth by physically moving storage vs low latency small messages; Grace Hopper nanosecond ≈11.8 inches of wire to visualize tiny delays
   - Apply the lesson: for gaming prioritize low latency; for bulk transfers consider physical shipment (sneakily high bandwidth)

6. **Modulation, encoding, numbering systems, and representations**
   Clarify differences between encoding (digital representations), modulation (mapping digital onto analog carriers), and how numbers/bytes are shown.
   - Define encoding: convert human media/text into binary (examples: ASCII, Unicode) and decoding to recover it
   - Define modulation: map digital bits onto analog carriers (modem = modulator/demodulator); give example coax or RF modulation
   - Recall numbering facts: 1 hex digit = 4 bits; 2 hex digits = 1 byte (8 bits); bandwidth normally reported in bits (kbps/Mbps/Gbps) while file sizes often show bytes (KB/MB/GB)
   - Practice conversions: convert 100 MB download → 800 Mb (100 × 8) to check ISP vs UI notation

7. **Security, physical vulnerabilities, and resilience**
   Understand how physical damage or control affects networks and common protections or realities from the undersea cable example.
   - Describe undersea cable risks: anchors/ships can sever cables; repairs need special ships and splicing and can cause regional outages
   - Assess tapping difficulty: tapping fiber is technically possible but disruptive; redundancy and rerouting are primary defenses
   - Plan for redundancy: recommend diverse paths and backups (alternate cables or satellite) for critical links

8. **Demos, study actions, and course reminders**
   Summarize the hands‑on demos, instructor anecdotes, and immediate action items to prepare for labs and assessments.
   - Recreate the hands‑on: practice punching down and crimping RJ‑45s before Tuesday's lab; bring your own cutters/crimper if available
   - Use instructor resources: review AI summaries/recordings and the Kahoot (link to be posted in Slack → General → Bookmarks)
   - Complete administrative tasks: take Exam 1 before next Tuesday to avoid late‑day fee, finish Skill Check 1, and sign up for the data center tour
   - Keep study habits: talk problems aloud (rubber‑duck or ChatGPT), favor wired connections for labs, and review numeric facts and examples for quizzes


## Key Vocabulary

**Physical Layer**: The OSI layer that transmits raw bits over a physical medium (copper, fiber, radio, light) and includes connectors and signaling methods.

**Latency**: Time delay for a signal to travel (commonly round‑trip time, RTT); influenced mainly by physical distance and medium.

**Bandwidth**: Capacity measured in bits per second (bps) describing the maximum data rate a channel can carry.

**Twisted‑pair (Ethernet) / Cat categories**: Copper Ethernet cabling with four twisted pairs; categories (Cat5e, Cat6A, Cat7/8) define construction and usable bandwidth/distance (e.g., Cat5e ≈1 Gbps, Cat6A ≈10 Gbps up to ~100 m).

**Patch Panel**: Passive closet hardware that organizes and connects cables; it has no power or logic—just punched contacts and ports for management.

**NIC (Network Interface Card)**: Host hardware that interfaces the computer to the physical medium; handles electrical/optical signaling to send and receive bits.

**Modulation / Demodulation**: The process of mapping digital bits onto an analog carrier (modulation) and recovering them (demodulation); performed by modems and RF transmitters.

**Encoding (text and media)**: Converting human text or media into machine‑readable binary representations (examples: ASCII, Unicode for text; MP3, JPEG for media).

## Review Questions

1. 1) Define the physical layer and name three physical‑layer devices you handled or observed in class. Explain the role of each.
2. 2) Explain the difference between latency and bandwidth. Give one numeric example for each from lecture (e.g., RTT to opposite side of Earth, a cable category speed).
3. 3) Compare Cat5e and Cat6A cabling: how many conductor pairs do they use, typical maximum run, and typical supported bandwidths? What physical changes enable Cat6A's higher rate?
4. 4) What is modulation and how does it differ from encoding? Give one concrete example where modulation is necessary.
5. 5) Convert and explain: a 500 MB file download is shown in your browser. How many megabits is that, and why does this matter when comparing to an ISP speed advertised in Mbps?
6. 6) Why does Wi‑Fi appear to let many clients talk at once even though only one device transmits to an AP at any instant? How does that affect throughput per device?
7. 7) Describe one real physical vulnerability of network infrastructure discussed in class and one practical mitigation or planning step you would take.
