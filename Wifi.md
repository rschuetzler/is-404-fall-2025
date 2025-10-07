# IS 404 — Wi‑Fi (Oct 02, 2025) Study Guide

## Overview

This session examined Wi‑Fi from technical, planning, and career perspectives: how wireless works, how networks are designed and measured, and how to translate hands‑on work into career momentum. Use this guide to review core concepts (bands, attenuation, surveys, security), follow the actionable lab steps (Skill Check 1, site survey), and adopt the networking habits the guest speaker recommended.

## Outline

1. **Wi‑Fi fundamentals: spectrum, bands, channels, and interference**
   Understand the difference between radio frequency bands (2.4 / 5 / 6 GHz) and Wi‑Fi protocol standards (Wi‑Fi 5/6/7/8 / 802.11 family), how channels and congestion affect performance, and the common sources of interference.
   - Explain frequency vs protocol: name a band (2.4 GHz) and a protocol (Wi‑Fi 6 / 802.11ax) and state how they differ.
   - List common interference sources: microwaves, baby monitors, garage door openers, thick walls, metal, and people (the “sack of water” effect).
   - Demonstrate channel reasoning: pick a less‑crowded channel in 5 GHz or 6 GHz when possible; avoid 2.4 GHz for congested environments.
   - Describe the effects of congestion: show how overlapping channels cause collisions and reduce throughput (analogy: FM stations overlapping).

2. **Security: open vs WEP vs WPA2 vs WPA3 and enterprise authentication**
   Know which wireless encryption to use, why WEP is unsafe, what WPA2 and WPA3 offer, and how enterprise authentication (802.1X + RADIUS / EdgeRoam) works on campus.
   - State the recommendation: use WPA2 for current compatibility; adopt WPA3 when client and AP support it.
   - Avoid WEP and open networks for private or institutional use; explain risks to unencrypted traffic (except for end‑to‑end encrypted apps like HTTPS).
   - Describe enterprise auth: outline 802.1X + RADIUS flow and identify EdgeRoam as the campus federated solution for username/password management.
   - Verify device support: check client OS/AP capabilities before enabling 6 GHz or WPA3-only features.

3. **Site surveys and tools: planning coverage and AP placement**
   Learn how to run a site survey to map signal strength to a floorplan, choose AP density and antenna types, and use recommended tools while noting platform limits.
   - Run a basic NetSpot survey: import a floorplan, walk to sample points, pause to scan, and generate a heatmap to decide AP locations.
   - Use alternatives: install Wi‑Fi Analyzer on Android for quick scans; avoid iPhone for low‑level radio captures (iOS limits).
   - Collect actionable outputs: export heatmap images, list visible APs and RSSI values, and recommend AP count/type for weak zones.
   - Plan for attenuation: record walls and likely crowd areas (e.g., auditoriums) and adjust AP power/placement accordingly.

4. **High‑density deployments and AP behavior (stadiums, roaming, MU‑MIMO)**
   Study the LaVell Edwards Stadium example to see why low transmit power, dense AP placement, directional antennas, roaming thresholds, and MU‑MIMO matter in crowded venues.
   - Analyze the stadium case: note ~1,100 APs in the bowl — add many low‑power APs rather than increasing single AP power.
   - Describe AP placement: use overhead APs with directional down‑tilt in seating sections and tune power to limit interference between adjacent APs.
   - Explain roaming behavior: show how clients switch APs when RSSI crosses thresholds and why enterprise settings aim for seamless handoff.
   - Summarize MU‑MIMO: explain that modern APs use multiple antennas to talk to multiple clients simultaneously, improving throughput in dense areas.

5. **Operational notes and tools: PoE, device mix, and limitations**
   Remember practical constraints like power, backwards compatibility, and the limitations of consumer devices when designing or surveying Wi‑Fi.
   - Verify PoE: assume enterprise APs are PoE for power and remote management; confirm switch capabilities before deployment.
   - Plan for mixed clients: allow WPA2 fallbacks for legacy devices and know that not all clients support 6 GHz or WPA3 yet.
   - Check platform limitations: use laptops or Android for surveys; NetSpot works well on Windows/Mac for floorplan heatmaps.
   - Measure and adjust: collect RSSI samples across device types and retune channel/power or add APs where needed.

6. **Hands‑on labs & deliverables: Skill Check 1, site survey assignment, and VM tips**
   Follow concrete steps for Skill Check 1 and the field site‑survey assignment; install VM helpers and organize deliverables clearly to help TAs validate your work.
   - Complete Skill Check 1: install a web server on your VM, host a simple site, open it in the VM browser (Firefox), and capture screenshots tied to each rubric item.
   - Organize the deliverable: label screenshots per rubric step and submit files in the order the rubric expects (make it very obvious).
   - Enable VM convenience: install VirtualBox Guest Additions if you need shared clipboard or drag‑and‑drop between host and VM.
   - Perform the field survey: use NetSpot on a laptop or Wi‑Fi Analyzer on Android to walk Tanner Building, record APs/RSSI, and submit heatmap/images.

7. **Career & networking habits from the guest speaker (Derek Bowen, Pariveda)**
   Adopt repeatable networking habits and project strategies: have a point of view, demonstrate delivery with side projects, and maintain a short, active contact list.
   - Follow the three pillars: develop something interesting to say, build demonstrable skills, and connect with people who need those skills.
   - Practice simple networking: keep a contact list, spend ~5 minutes weekly (or 50 minutes monthly) touching base, and record context with LinkedIn notes.
   - Build memorable side projects: create small POCs (example: Alexa skill or SageMaker forecasting POC) to show initiative and provide interview stories.
   - Give value first: share useful articles, make introductions, and aim to be helpful before asking for favors to build advocates.

8. **Examples & consulting cadence to remember**
   Recall concrete stories shown in class as templates for technical and career work: stadium Wi‑Fi, NetSpot surveys, AWS/SageMaker consulting flow, and candidate side projects.
   - Use the stadium design as a template for high‑density reasoning: low power + many APs + directional antennas.
   - Follow the consulting flow: architecture doc → short POC (2 weeks) → seek funding (AWS) → production plan (Derek's energy forecasting project).
   - Frame side projects as interview assets: deliver a small, working demo and a one‑page summary of what you learned and measured.
   - Apply networking funnel thinking: move people from acquaintances → known contacts → trusted advocates through consistent, helpful interactions.


## Key Vocabulary

**Attenuation**: The reduction of radio signal strength as it passes through materials (walls, glass, metal) or is absorbed by people and objects; large crowds can dramatically attenuate signals.

**Unlicensed band**: A portion of the radio spectrum (e.g., parts of 2.4 GHz, 5 GHz, and 6 GHz) that the FCC allows anyone to use without a license, resulting in higher device density and potential interference.

**Channel**: A narrower frequency slice inside a band that devices and APs occupy; overlapping channels cause interference and reduce throughput.

**WPA2 / WPA3**: Wi‑Fi Protected Access versions: WPA2 is the widely used encryption standard today; WPA3 is the newer standard with improved security features but not yet ubiquitous on all devices.

**WEP**: Wired Equivalent Privacy — an outdated and insecure Wi‑Fi encryption method that should not be used for protecting networks.

**MU‑MIMO**: Multi‑User Multiple Input Multiple Output — an AP antenna/radio capability that lets the AP serve multiple clients simultaneously, improving efficiency in dense environments.

**Site survey**: A systematic walk through a building while collecting signal strength (RSSI) at sample points, then mapping those measurements onto a floorplan to create a heatmap for AP planning.

**RADIUS / 802.1X / EdgeRoam**: RADIUS is a centralized authentication protocol used with 802.1X for enterprise Wi‑Fi; EdgeRoam is an example of a campus federated solution that integrates identity providers for visitor authentication.

## Review Questions

1. Explain the difference between a frequency band (e.g., 5 GHz) and a Wi‑Fi protocol version (e.g., Wi‑Fi 6). Give one concrete implication of that difference when choosing equipment.
2. List four common sources of Wi‑Fi interference and describe one practical mitigation for each.
3. Describe the steps to perform a basic NetSpot site survey and what deliverables you should produce for the class assignment.
4. Compare open, WEP, WPA2, and WPA3 networks: which should you use for campus devices today and why? How does HTTPS affect the risk on open networks?
5. Using the stadium example (~1,100 APs), explain why a design uses many low‑power APs instead of fewer high‑power APs and how MU‑MIMO and roaming interact in that environment.
6. What is RADIUS/802.1X used for in enterprise Wi‑Fi, and how does a federated system like EdgeRoam benefit campus visitors?
7. Summarize Derek Bowen’s three pillars of career momentum and name two repeatable networking habits he recommended.
8. For Skill Check 1, list the exact deliverable actions you must complete on your VM and two tips to make TA verification easy.
