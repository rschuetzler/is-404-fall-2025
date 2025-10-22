# IS 404 — DNS and an AWS Outage (October 21, 2025) Study Guide

## Overview

This packet reviews core DNS concepts through the October 20–21, 2025 AWS outage case study: how resolution works, why caching/TTLs delay fixes, and how DNS failures can make healthy backends appear unreachable. It combines conceptual definitions, operational mitigations, hands‑on troubleshooting steps, and concrete commands you should be able to use on quiz day.

## Outline

1. **What DNS is and why it matters**
   DNS maps human‑friendly names to network endpoints and metadata; almost every client and control plane depends on it. A DNS problem can make otherwise healthy services unreachable because clients use names, not raw IPs.
   - Define DNS as a distributed, hierarchical name → address database (root → TLD → zone).
   - Recall the two memorable quotes: “It was DNS.” and “Nobody uses IP addresses.”
   - Give an example: resolving example.com returns an A/AAAA record that clients use to open TCP/HTTP connections.

2. **Resolution flow (end‑to‑end)**
   Understand the stepwise lookup path, where caching occurs, and the difference between recursive and iterative resolution.
   - Follow the typical path: Client (app/OS) → local resolver/forwarder → recursive resolver → root → TLD → authoritative nameserver → answer returned and cached back up the chain.
   - Distinguish recursive resolvers (do full work) from stub resolvers (forward only).
   - Use dig +trace to observe the delegation chain and dig @<authns> to query authoritative servers directly (e.g., dig +trace example.com; dig @ns1.example.net example.com A).
   - Recognize that resolvers perform iterative queries and may return referrals (NS) or glue records when needed.

3. **DNS record types and delegation rules**
   Know common record types, how delegation works, and important operational restrictions (CNAME behavior, apex rules, glue).
   - Memorize common types: A (IPv4), AAAA (IPv6), CNAME (alias), NS (delegation), MX (mail), TXT (SPF/DKIM), SOA (zone metadata).
   - Explain delegation: the parent zone's NS records (and glue when child nameservers live in the child zone) point to authoritative name servers.
   - Avoid putting a CNAME at the zone apex; expect an extra lookup for CNAMEs and watch for long chains.
   - When troubleshooting, identify NS records for a zone and then query those authoritative servers directly to confirm the actual data.

4. **Caching, TTLs, and propagation behavior**
   Multiple caching layers store answers for their TTL. TTL strategy balances propagation speed vs query load and stability.
   - List caching layers: OS/browser, local forwarder (systemd‑resolved/router), recursive resolver (ISP/public), CDN DNS edges.
   - Set TTL guidance: lower TTLs to 60–300s well before planned changes to speed cutovers; expect propagation from minutes up to 48 hours in extreme cases.
   - Demonstrate the laminated‑sign analogy: change authoritative record — caches hold old answers until TTL expires unless you clear them or use short TTLs.
   - When making a change: lower TTL, wait for previous TTL to expire (so caches honor the new short TTL), perform change, validate, then restore longer TTLs.

5. **How DNS failures cascade (AWS outage example)**
   DNS problems can cascade because many services and control planes rely on name resolution; concentration risk and shared control‑plane dependencies widen blast radius.
   - Summarize the outage: DynamoDB endpoints in us‑east‑1 became effectively unreachable due to resolution failures despite backends working.
   - Identify contributing factors: high concentration in us‑east‑1, shared control‑plane components, and cached/incorrect endpoint information across resolvers.
   - Understand that DNS outages can manifest as SERVFAIL or NXDOMAIN spikes and produce broad, confusing symptoms across services.

6. **Operational mitigations and design patterns**
   Design and operational practices reduce DNS-related risk: multi‑region deployments, multi‑authoritative DNS, health checks, and disciplined change management.
   - Adopt multiple authoritative DNS providers (primary + secondary) and pre‑authorize provider APIs for emergency changes.
   - Deploy multi‑region and/or multi‑cloud replicas for critical state and control‑plane components to avoid regional concentration risk.
   - Configure DNS‑based failover with health checks where appropriate (e.g., Route 53 health checks + failover policies).
   - Use anycast or geographically distributed resolvers for resolution resilience and synthetic multi‑region DNS checks for monitoring.

7. **Troubleshooting heuristics & emergency runbook**
   Follow a concise, repeatable sequence when diagnosing name resolution problems; use the hosts file and alternate resolvers as temporary mitigations.
   - Step 1 — Test by IP vs hostname: curl http://<IP>/ (if IP works and name fails ⇒ DNS implicated).
   - Step 2 — Inspect local overrides: check /etc/hosts (Unix) or C:\Windows\System32\drivers\etc\hosts (Windows).
   - Step 3 — Query resolvers: dig example.com +short; dig @8.8.8.8 example.com; dig +trace example.com; dig example.com SOA +noall +answer.
   - Step 4 — Query authoritative NS: find NS records and dig @<authns> example.com A to confirm authoritative data.
   - Emergency tactics: apply hosts file edits on critical machines for an immediate local workaround; switch critical machines to alternate resolvers (1.1.1.1 or 8.8.8.8); use DNS provider API to push fixes if available and pre‑authorized.
   - Document every step and record timestamps; after fix, restore original TTLs and run post‑mortem.

8. **Monitoring, pre‑change checklist, and runbook items**
   Proactively monitor DNS health and follow a pre‑change checklist to reduce surprise and speed recovery during incidents.
   - Implement synthetic DNS queries from multiple geographic locations and resolvers; alert on increases in SERVFAIL/NXDOMAIN or timeouts.
   - Pre‑change checklist: lower TTLs (60–300s) well before change, verify authoritative NS and SOA serial, prepare rollback records and automation, notify stakeholders.
   - Runbook emergency steps: verify scope via Downdetector/public reports, follow troubleshooting heuristics above, update authoritative records via provider API, apply temporary hosts edits if propagation is slow.

9. **Hands‑on exercise recap and practical commands**
   Practice by creating records, changing them, and observing propagation across resolvers and caches — use the listed commands to collect evidence.
   - Create an A or CNAME record for a lab server, set TTL to 60–300s, and record the times you make changes.
   - Verify from multiple vantage points: local (dig example.org), public (dig @8.8.8.8 example.org), authoritative (dig @ns1.provider.example example.org).
   - Useful commands: dig example.com A +noall +answer; dig @8.8.8.8 example.com +short; dig +trace example.com; dig example.com SOA +noall +answer; curl http://93.184.216.34/ to test by IP.
   - Experiment with hosts file entries to see immediate local effect and weigh pros/cons of manual overrides.

10. **Final takeaways**
   Treat DNS as first‑class infrastructure: design for diversity, monitor actively, and rehearse runbooks so that caching behavior and TTLs are expected during incidents.
   - Remember: DNS fragility can make healthy servers unreachable — plan TTLs and staged rollouts around that reality.
   - Practice the core heuristics (IP vs name, check hosts, query multiple resolvers, query authoritative NS) until they are second nature.
   - After incidents, restore TTLs, update runbooks with observed propagation times, and document lessons learned to reduce blast radius next time.


## Key Vocabulary

**DNS (Domain Name System)**: The distributed hierarchical system that maps human‑readable domain names to IP addresses and other resource records.

**Resolver**: Software that queries DNS on behalf of clients; can be a stub resolver (forwards) or a recursive resolver (performs full resolution).

**Recursive resolver**: A DNS server that performs the entire resolution process (root → TLD → authoritative) for a client and returns the final answer.

**Authoritative nameserver**: A server that holds the definitive DNS records for a zone and responds with the canonical answers for that zone.

**A record**: DNS record that maps a hostname to an IPv4 address.

**AAAA record**: DNS record that maps a hostname to an IPv6 address.

**CNAME record**: Canonical name record that aliases one domain name to another; causes an additional lookup for the target name.

**NS record**: Nameserver record used by a parent zone to delegate authority for a child zone to specified authoritative name servers.

**SOA (Start of Authority)**: Zone metadata record containing serial, refresh, retry, expire, and minimum TTL values for the zone.

**TTL (Time To Live)**: A value (in seconds) that indicates how long a DNS answer may be cached by resolvers and clients.

**Glue record**: An IP address record provided in the parent zone to allow resolution of child nameservers that live inside the child zone.

**SERVFAIL / NXDOMAIN**: DNS response codes: SERVFAIL indicates a server failure; NXDOMAIN indicates the queried name does not exist.

**Hosts file**: A local OS file (/etc/hosts or Windows hosts file) that overrides DNS on a single host and can be used for testing or emergency overrides.

**Anycast**: A routing technique that advertises the same IP address from multiple locations to provide geographically distributed, resilient service (commonly used by public DNS providers).

## Review Questions

1. Explain the end‑to‑end DNS resolution flow starting from a browser request to the final authoritative answer. Which components may cache answers?
2. During a planned DNS cutover, what TTL strategy should you follow before, during, and after the change? Give example TTL values and explain propagation implications.
3. You can curl the service IP successfully but curl http://example.com/ fails. List the step‑by‑step checks you should perform to confirm and fix a DNS‑related outage.
4. Describe how the October 2025 AWS outage illustrated DNS as a systemic risk. What design and operational mitigations would reduce the blast radius of a similar event?
5. Give three concrete troubleshooting commands (with arguments) you would run to determine whether authoritative DNS records are correct and whether public resolvers have propagated a change.
6. What are the tradeoffs between short and long DNS TTLs? Provide at least two operational consequences for each choice.
7. When is it appropriate to edit a hosts file during an outage? Describe the benefits and the risks of that approach.
8. Explain what a glue record is and why it's needed when delegating a zone whose nameservers are inside the same child zone.
