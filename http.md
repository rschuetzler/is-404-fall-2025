# IS 404 — HTTP 1 (Oct 28, 2025)

## Overview

This session explains HTTP as the web’s application‑layer request→response protocol and walks you through hands‑on DevTools Network inspection to see what really happens when a page loads. It covers methods, headers, status codes, cookies, dynamic requests, TLS/HTTPS, performance/waterfall analysis, and the transport evolution toward HTTP/2 and HTTP/3 (QUIC).

## Outline

1. **HTTP request→response model (core concepts)**
   Understand the pieces of a single HTTP interaction and how state is carried in a stateless protocol.
   - Describe a request: method + URL/path in the request line, request headers (Host, Accept, Cookie, Authorization, Referer/Origin, User‑Agent), and optional body (form data, JSON, file upload).
   - Describe a response: numeric status code, response headers (Content‑Type, Set‑Cookie, Cache‑Control, Location, Access‑Control‑Allow‑Origin) and optional body (HTML, JSON, image, font).
   - Explain statelessness: show how cookies, tokens, or URL parameters carry session state across requests (cookie = 'sticky note' analogy).
   - Give a concrete example: GET /images/logo.png → 404 Not Found with server HTML in the response preview.

2. **Methods, semantics and API usage**
   Know common HTTP methods, their intended safety/idempotence semantics, and how JavaScript APIs use them.
   - List common methods and intent: GET (read), POST (create/submit), PUT/PATCH (modify), DELETE (remove), HEAD/OPTIONS (metadata/CORS preflight).
   - Practice: use fetch or XHR to POST JSON to an API endpoint and inspect the request body and Content‑Type in DevTools.
   - Identify idempotent actions: explain why GET/PUT are idempotent and why that matters for retries and caching.

3. **Status codes and redirect chains**
   Recognize status code classes, common codes, and how redirects appear in a Network trace.
   - Map code classes: 1xx informational, 2xx success (200, 201), 3xx redirect (301/302/307/308 with Location), 4xx client errors (400/401/403/404), 5xx server errors (500/502).
   - Trace redirects: enable Preserve log, reload a page, and follow the Location header across sequential entries to find the final response.
   - Debug pattern example: a redirect loop appears as repeated entries in DevTools; inspect which response sets the Location header unexpectedly.

4. **Headers, content types and payloads**
   Learn which request/response headers matter for behavior, parsing, caching, and cross‑origin access.
   - Inspect key request headers: Host, Accept, Accept‑Encoding, User‑Agent, Referer, Origin, Cookie, Authorization and check their values in the Headers panel.
   - Inspect key response headers: Content‑Type (text/html, application/json, image/png, font/woff2), Cache‑Control/ETag/Last‑Modified, Set‑Cookie, Location, Access‑Control‑Allow‑Origin.
   - Practice: identify a JSON API response by Content‑Type and preview the JSON in DevTools; verify if caching produced a 304 Not Modified.

5. **Cookies, identity, and privacy controls**
   Understand how servers set cookies and which cookie attributes control security and cross‑site behavior.
   - Explain Set‑Cookie usage and attributes: Domain, Path, Expires/Max‑Age, Secure (HTTPS only), HttpOnly (JS inaccessible), SameSite (Lax/Strict/None for cross‑site sending).
   - Practice: find Set‑Cookie in a response, then confirm Cookie header is included on subsequent requests to the same domain/path.
   - Watch for privacy issues: identify third‑party cookies and blocked tracker requests in DevTools; note how stealing cookies can impersonate a user.

6. **DevTools Network workflow — hands‑on debugging**
   Use the Network tab as your primary diagnostic workflow to reproduce issues and inspect all request/response details.
   - Step‑by‑step: open DevTools (F12) → Network tab → optionally tick Preserve log and Disable cache → reload the page → click any request to inspect Headers / Preview / Response / Timing.
   - Always check: method, full URL, status code, redirect chain, request headers (Cookie/Authorization), response headers (Set‑Cookie/CORS/Cache), resource type and initiator.
   - Filter and reproduce: filter to XHR/fetch to watch dynamic API calls (e.g., infinite scroll), click UI elements and observe matching requests and JSON payloads.

7. **Dynamic/background requests (XHR/fetch) and single‑page behavior**
   Recognize and debug asynchronous requests made after the initial document load.
   - Identify XHR/fetch entries in Network and inspect payloads to debug APIs used by dynamic UI (infinite scroll, live updates, form submits).
   - Simulate interactions: trigger scrolling or button clicks while watching the Network tab to correlate UI behavior with API endpoints and status codes.
   - Spot problems: failing JSON endpoints, missing CORS headers, or long API response times that break client functionality.

8. **Performance, waterfall timings, and optimization cues**
   Use the waterfall and timing metrics to prioritize performance fixes and reduce page load overhead.
   - Read timing bars: identify DNS lookup, TCP connect, TLS handshake, TTFB (Time to First Byte), and content download; locate the largest/longest bars in the waterfall.
   - Prioritize fixes: reduce request count, bundle assets, use CDNs, enable caching (Cache‑Control, ETag), and minimize cross‑domain calls to lower DNS+connect overhead.
   - Concrete example: detect many small parallel requests causing connection queuing; consider HTTP/2/3 multiplexing or combining resources where sensible.

9. **Security, TLS/HTTPS, and CORS**
   Know why HTTPS matters, how browsers surface mixed content, and how CORS controls cross‑origin API access.
   - Verify HTTPS: check the protocol in DevTools, view certificate chain in the Security panel, and fix mixed content by loading all resources over HTTPS.
   - Explain cookie security: Secure cookies transmit only over HTTPS; HttpOnly prevents JavaScript access; SameSite limits cross‑site sends to reduce CSRF risk.
   - Debug CORS: observe preflight OPTIONS requests and confirm Access‑Control‑Allow‑Origin headers; fix missing headers on the server to allow cross‑origin requests.

10. **Application‑layer history and transport evolution (FTP, HTTP/2, HTTP/3/QUIC)**
   Place HTTP in historical context (file transfer needs) and understand how transport changes (HTTP/2, HTTP/3) affect performance but not semantics.
   - Recall FTP history: FTP (since 1971) is an older file transfer protocol that used separate control and data channels and lacked encryption by default — contrast with modern HTTP over TLS.
   - Summarize transport changes: HTTP/2 adds multiplexing and header compression; HTTP/3 runs over QUIC (UDP) to reduce head‑of‑line blocking and improve handshake latency.
   - Practice observation: notice reduced connection/handshake times and different timing patterns in DevTools when websites use HTTP/2 or HTTP/3, while methods/headers/status codes remain the same.

11. **Practical checklist & recommended workflows**
   Concrete steps to reproduce, diagnose, and triage issues using DevTools and knowledge of headers, cookies, and transport.
   - Reproduce the issue with Network open; enable Disable cache to force fresh fetches when appropriate.
   - Find failing entries (4xx/5xx or blocked), open the request → inspect Request Headers, Response Headers, and Response body to identify errors or missing headers.
   - For performance: use waterfall to spot slow DNS/TCP/TLS/TTFB; for redirects: use Preserve log and follow Location headers; for CORS: inspect OPTIONS preflight and Access‑Control headers.


## Key Vocabulary

**HTTP**: Hypertext Transfer Protocol — the application‑layer request→response protocol used by the web to fetch documents, images, APIs and other resources.

**Request / Response**: Request: client message (method + URL + headers + optional body). Response: server message (status code + headers + optional body).

**Method**: The action the client asks the server to perform (e.g., GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS).

**Status code**: Numeric response indicator grouped by class: 2xx success, 3xx redirect, 4xx client error, 5xx server error.

**Header**: Metadata key:value pairs sent with requests or responses (e.g., Content‑Type, Cache‑Control, Set‑Cookie, Authorization).

**Cookie / Set‑Cookie**: Small pieces of state set by servers via Set‑Cookie and sent by browsers in Cookie headers; attributes (Secure, HttpOnly, SameSite) control scope and security.

**CORS**: Cross‑Origin Resource Sharing — browser security model requiring servers to send explicit headers (Access‑Control‑Allow‑Origin, etc.) to permit cross‑origin requests.

**TLS / HTTPS**: Transport Layer Security; HTTPS is HTTP encrypted over TLS, providing confidentiality and server authentication for web traffic.

**Waterfall / TTFB**: Waterfall: DevTools visualization of request timing (DNS, connect, TLS, TTFB, download). TTFB: Time to First Byte, an important latency metric.

**QUIC / HTTP/3**: QUIC: transport protocol built on UDP that integrates encryption and improves multiplexing; HTTP/3 runs on QUIC to reduce latency and head‑of‑line blocking.

## Review Questions

1. 1) In a DevTools Network trace, what steps do you take to diagnose a failing AJAX call that returns no data? Which panels and headers do you inspect and why?
2. 2) Explain how cookies provide session state despite HTTP being stateless. What do the Secure, HttpOnly, and SameSite attributes each control?
3. 3) Describe how redirect chains appear in the Network tab and how you would find which response set the unexpected Location header.
4. 4) Give three specific waterfall timing metrics you would examine to diagnose a slow page load and one concrete optimization for each metric.
5. 5) What is the difference between HTTP/2 and HTTP/3 from a transport perspective, and why do these changes not require application‑layer changes to methods or headers?
6. 6) A POST to https://api.example.com returns a CORS error in the browser console. What preflight/request/response headers do you check and what server change would fix the error?
7. 7) Walk through the practical checklist you would use when you see mixed content warnings for a site after enabling HTTPS.
