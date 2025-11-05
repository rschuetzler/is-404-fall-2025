# IS 404 — HTTP 1 (Oct 28, 2025) Study Guide

## Overview

This guide distills the lecture, demos, and supplemental readings on how HTTP behaves today, how to observe it, and how to configure servers for real-world sites. Use the actionable checklist and review questions to prepare for quizzes and the lab tasks (MySQL on EC2, nginx virtual hosts, and Let’s Encrypt TLS).

## Outline

1. **HTTP fundamentals: request–response model & statelessness**
   Understand the minimal request structure, the stateless nature of HTTP, and how browsers expand a single HTML response into many subsequent resource requests.
   - Identify the minimal request line: method + request-target (path/URL) + HTTP version (e.g., GET /index.html HTTP/1.1).
   - Explain statelessness and list application-level mechanisms for continuity (cookies, Authorization header, bearer tokens).
   - Demonstrate how a single HTML document triggers many GETs for CSS, JS, fonts, images and possibly dozens–hundreds of requests across multiple hostnames.

2. **Using browser Developer Tools to inspect HTTP**
   Practice the concrete DevTools steps and habits you saw in class to capture headers, statuses, timing, and redirect chains.
   - Open DevTools: Cmd+Opt+I (macOS) or Ctrl+Shift+I (Windows/Linux) → Network tab → reload page to capture the waterfall.
   - Inspect request line, method, HTTP version, response status, request/response headers (Accept, Cache-Control, Set-Cookie, ETag), Content-Type and sizes.
   - Read timing breakdowns (DNS, TCP/TLS handshake, TTFB, download) and identify resources fetched from third-party hostnames or CDNs.
   - Use practical toggles: Disable cache while DevTools is open; use hard refresh (Cmd+Shift+R / Ctrl+F5) to bypass cache; check redirect chains and blocked requests.

3. **HTTP methods, routing, and correct status codes**
   Map verbs to semantics in server code and return the appropriate numeric status codes for clear API behavior and client expectations.
   - Match methods to actions: GET (safe, idempotent read), POST (submit/create), PUT (full replace), PATCH (partial update), DELETE (remove).
   - Implement server routes accordingly (example: Express app.get/app.post/app.put/app.patch/app.delete) and return semantically correct codes (201 on resource creation).
   - Differentiate 401 (unauthenticated) vs 403 (authenticated but forbidden), and use 301 for permanent redirects and 307 when you must preserve method on redirect.

4. **Headers, cookies, and protecting sensitive state**
   Know the key request/response headers that control content negotiation, caching, and authentication, and harden cookies used for sessions.
   - Inspect common headers: Accept, Accept-Encoding, Accept-Language, User-Agent, Referer, Authorization, Cookie, Cache-Control, ETag, Set-Cookie.
   - Set cookies securely: include Secure (HTTPS only), HttpOnly (no JS access), and SameSite (mitigate CSRF) flags for session cookies.
   - Remember that IPs and ports are transport-layer attributes — reduce latency impact by minimizing distinct hostnames where practical.

5. **Caching: Cache-Control, ETag, Last-Modified, and 304 responses**
   Understand how servers signal caching policies and how browsers reuse resources to save bandwidth and improve performance.
   - Read Cache-Control directives (max-age, no-cache, no-store, must-revalidate) and observe ETag / Last-Modified headers in responses.
   - Recognize a 304 Not Modified response as permission to reuse the cached copy and as a bandwidth-saving signal.
   - When debugging, disable cache in DevTools or perform a hard refresh to ensure you're seeing current server content.

6. **Redirects vs DNS aliases and real-world redirect use**
   Differentiate HTTP-level redirects from DNS CNAMEs and understand why permanent redirects are used for domain transitions.
   - Explain that HTTP redirects (3xx) instruct the browser to request a new URL and update the address bar, while DNS CNAMEs only map names during resolution.
   - Use 301 Moved Permanently to preserve links and search indexing when migrating domains (example chain: lds.org → churchofjesuschrist.org).
   - Inspect redirect chains in DevTools to spot multiple 3xx hops and ensure final destination uses correct method semantics.

7. **HTTPS/TLS basics and certificate management (Let’s Encrypt)**
   Know what HTTPS/TLS protects, how certificates establish domain authentication, and how to obtain and renew certs for lab sites.
   - State that HTTPS = HTTP over TLS, providing confidentiality, integrity, and domain authentication via X.509 certificates.
   - Describe ACME (Let’s Encrypt) issuance methods (HTTP-01, DNS-01) and use certbot to automate issuance and renewal for nginx.
   - Configure nginx to listen on 443 with certificate files and redirect port 80 → 443 (301) to enforce HTTPS for lab sites.

8. **Lower-layer network impacts, HTTP/2 and HTTP/3 (QUIC)**
   Connect DNS, TCP/TLS handshakes, and hostname choices to page latency and understand why HTTP/2 and HTTP/3 were developed.
   - Explain latency cost from extra hostnames: each unique hostname often causes a DNS lookup + new TCP/TLS handshake → added time before content arrives.
   - Summarize HTTP/2 benefits: multiplexing over single TCP connection, header compression (HPACK), and server push (requires TLS in most browsers).
   - Summarize HTTP/3/QUIC benefits: transport + TLS handshakes combined, avoids TCP head-of-line blocking, faster connection setup, better mobile resilience and privacy.

9. **HTTP vs other file-transfer protocols**
   Place HTTP in the broader ecosystem: when to use HTTP(S) vs FTP/SFTP/SCP/rsync for file operations and administration.
   - Use HTTPS/CDNs for delivering web assets; use SFTP or FTPS for secure file administration, and prefer rsync for efficient incremental backups/mirroring.
   - Know protocol tradeoffs: FTP supports directory listings but is plaintext by default; SFTP provides file management over SSH; SCP is simple secure copy without directory operations.
   - Choose tools appropriately: use SyncThing or managed cloud sync for persistent syncing; use SFTP/rsync for server uploads and backups.

10. **Lab tasks and practical server-side best practices**
   Follow the lab requirements and adopt server-side best practices for routing, logging, TLS, and database access.
   - Skill Check 2: Install MySQL on EC2, configure security groups or SSH tunnels, and verify remote/admin connectivity.
   - Skill Check 3: Create nginx server blocks for multiple hostnames, point DNS to your instance, obtain Let’s Encrypt certs with certbot, and enable automated renewals.
   - Server guidance: map routes to correct HTTP methods, return proper status codes (201, 401/403 distinctions, 404, 500), and consult both DevTools and server logs when debugging.
   - Security checklist: enable HTTPS, use Secure/HttpOnly/SameSite cookies, restrict DB access, enforce strong passwords and keep packages up to date.

11. **Practical demos & study actions to replicate**
   Replicate class demos to make the behaviors stick: DevTools workflows, redirect chain inspection, Wireshark observations (HTTP vs HTTPS), and hands-on lab commands.
   - Practice: open DevTools Network tab on a simple site and a news site; count resource requests, note third-party hostnames and timing.
   - Practice: inspect a redirecting domain and watch 3xx codes and address bar changes; force cache bypass and observe 304 responses.
   - Practice: install MySQL and nginx on EC2, configure server blocks, run certbot to obtain certificates, and verify HTTPS in the browser.


## Key Vocabulary

**HTTP (Hypertext Transfer Protocol)**: Application-layer request–response protocol used to transfer web resources; stateless by design.

**HTTPS**: HTTP transported over TLS; provides encryption, integrity, and domain authentication.

**TLS (Transport Layer Security)**: Cryptographic protocol that provides confidentiality, integrity, and authentication using certificates.

**X.509 certificate**: Digital certificate asserting domain control; chains to trusted root CAs to enable TLS authentication.

**ACME**: Automatic Certificate Management Environment — protocol Let’s Encrypt uses to validate domain control and issue/renew certs.

**HTTP method (verb)**: Action requested by the client (GET, POST, PUT, PATCH, DELETE) that expresses intended operation on a resource.

**Status code**: Three-digit numeric response indicating request result, grouped in families (1xx–5xx), e.g., 200, 301, 404, 500.

**Header**: Key/value metadata in HTTP requests/responses (e.g., Accept, Content-Type, Cache-Control, Set-Cookie).

**Cookie**: Browser-stored key/value pair used for state (sessions); can include Secure, HttpOnly, and SameSite flags.

**ETag / 304 Not Modified**: ETag is a validator used by servers; 304 tells the browser the cached copy is still valid so it can be reused.

**DNS & CNAME**: DNS maps names to IPs; a CNAME is an alias at DNS level that does not cause a browser-level redirect.

**CDN (Content Delivery Network)**: Distributed caching network that serves static assets from edge locations to reduce latency.

**HTTP/2**: HTTP version that multiplexes multiple streams over a single TCP connection and compresses headers to improve performance.

**HTTP/3 / QUIC**: HTTP over QUIC (UDP-based) that combines transport and TLS handshakes, reduces head-of-line blocking, and improves connection setup latency.

**rsync**: Tool for efficient incremental file synchronization that transfers only differences between source and target.

## Review Questions

1. Using DevTools Network tab, what three pieces make up the minimal HTTP request line and where do you see them?
2. Explain the difference between 401 and 403 status codes and give an example scenario for each.
3. Describe how Cache-Control and ETag interact to produce a 304 Not Modified response — what does the browser do after receiving 304?
4. List three secure cookie flags you should set for session cookies and explain what each one prevents.
5. Compare an HTTP 301 redirect and a DNS CNAME: how do they differ in behavior and user-visible effects?
6. Summarize two performance benefits of HTTP/3/QUIC over HTTP/1.1 and why consolidating hostnames can still help performance.
7. For the lab: outline the steps (high-level) to host two different sites on one EC2 instance using nginx and obtain Let’s Encrypt certificates for both.
