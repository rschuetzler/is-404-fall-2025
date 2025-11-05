# IS 404 — APIs (Oct 30, 2025) Study Guide

## Overview

This packet ties together HTTP and API fundamentals with hands‑on practice and practical troubleshooting. Use it to prepare for quizzes by focusing on verb→CRUD mappings, JSON vs HTML choices, authentication best practices, Postman → code workflows, and how email and remote‑access protocols relate to API troubleshooting.

## Outline

1. **APIs and HTTP fundamentals (verb → CRUD)**
   Understand what an API is and how HTTP methods map to common create/read/update/delete operations. Know the pragmatic REST conventions used in class even if full REST constraints are not required.
   - Define API as a programmatic network interface (usually HTTP + JSON for modern web APIs).
   - Map HTTP verbs to CRUD: GET=Read (safe, idempotent), POST=Create (non‑idempotent), PUT/PATCH=Update (PUT often replaces, PATCH modifies), DELETE=Remove.
   - Recognize status codes: 200/2xx success, 400 bad request, 401 unauthorized, 403 forbidden, 404 not found, 405 method not allowed, 500 server error.
   - Use clear resource paths (e.g., /todos/123) and correct verb for intended action to avoid 404/405 errors.

2. **Data formats: JSON vs HTML and form behavior**
   Choose JSON for machine consumption and HTML for browser rendering. Know how HTML form method attributes affect how data is sent and the security/UX tradeoffs.
   - Prefer JSON (application/json) for API responses and request bodies because it is structured and language‑friendly.
   - Treat HTML as presentation for people — scraping HTML to extract data is brittle compared to consuming JSON.
   - Use GET for safe/read operations; form method="get" places fields in the query string (e.g., /search?q=dogs) — avoid sending secrets here.
   - Use POST (body payload) for logins, uploads, and state changes; expect browser UX issues like re‑submission prompts on refresh.

3. **Authentication patterns and security best practices**
   Know common authentication schemes, how to transmit secrets safely, and the frequent causes of auth failures encountered in labs.
   - Pass bearer tokens in the Authorization header: Authorization: Bearer <token>; do not put tokens or passwords in URLs or query strings.
   - Store tokens/keys as secrets: never commit them to public repos or paste into public chat; scope tokens when possible.
   - Trim whitespace/newlines when copying tokens — stray characters commonly cause 401 Unauthorized.
   - Prefer headers for API keys and use HTTPS for all authenticated requests; set Content‑Type: application/json for JSON payloads.

4. **Tooling & workflow — prototype in Postman then wire to code**
   Use Postman to iterate interactively until the request works, then translate the working request into client code (fetch, axios, Python requests).
   - In Postman: set method, paste exact URL, add query params via UI, set headers (Content‑Type, Authorization), enter raw JSON body, and Send.
   - Follow a troubleshooting checklist before changing code: confirm URL/path params, verify method, validate JSON syntax, inspect headers and status codes, check token formatting.
   - Translate to code only after success in Postman: include same headers, JSON.stringify bodies in JS, and parse responses as JSON.
   - Example translation pattern: fetch(url, { method: 'POST', headers: { 'Content-Type':'application/json', 'Authorization':'Bearer <token>' }, body: JSON.stringify(data) })

5. **Class labs & concrete API examples**
   Recall concrete hands‑on exercises and what each lab practiced so you can reproduce the steps on your own.
   - Dog CEO (public, unauthenticated): GET /api/breeds/image/random — parse JSON and render the returned image URL in a page.
   - socialdo (instructor playground, authenticated): use provided bearer token to POST new todos, GET lists, PUT to update (mark complete), and DELETE items.
   - Study representative APIs (OpenAI, Twilio, Alpha Vantage) to see token billing, action APIs (SMS), and read APIs (stock data).
   - Reproduce lab flows in Postman first, then copy successful requests into your codebase.

6. **Email and other application‑level protocols (context for networking)**
   Remember email history and how SMTP/IMAP/POP3 operate over TCP ports — these concepts reinforce port, header, and routing troubleshooting for APIs.
   - Recall Ray Tomlinson’s use of '@' to separate user@host and that email messages carry headers (From, To, Subject, routing) shared along delivery paths.
   - Know key email protocols and ports: SMTP (send) port 25 and submission port 587; IMAP (sync) ports 143/993 (TLS); POP3 (download) ports 110/995 (TLS).
   - Use DNS MX records to route mail; analogously, verify hostnames and ports when diagnosing unreachable API endpoints (firewall/NAT issues).
   - Understand that webmail UIs are clients built on these SMTP/IMAP/POP3 backends — different application protocols can coexist with HTTP.

7. **Remote access, exposing services, and security**
   Know remote access options, why command‑line remote shells are powerful, and safer alternatives to direct port exposure for development and admin.
   - Value the command line: resource‑light, scriptable, repeatable — ideal for server config and automation via SSH.
   - Prefer SSH over Telnet: SSH encrypts traffic, supports key auth, SFTP, port forwarding, and VS Code Remote; Telnet is obsolete and unencrypted.
   - Avoid raw port forwarding to expose home services; prefer VPN/mesh tools like Tailscale (WireGuard) to securely connect devices without opening public ports.
   - For remote GUI access prefer tunneling (SSH/VPN) to secure RDP/VNC traffic; use SSH keys and IP restrictions instead of passwords where possible.

8. **Practical checklist & common quick fixes**
   Actionable steps to perform when a request or lab fails — apply these in Postman first to isolate issues before changing code.
   - Check exact URL and path parameters for typos or wrong resource ids (404 troubleshooting).
   - Verify HTTP method matches API docs; switch method if you get 405 Method Not Allowed.
   - Validate JSON body syntax with a linter and set Content‑Type: application/json to avoid 400 Bad Request.
   - Inspect Authorization header formatting and remove extra whitespace/newlines to resolve 401 issues.
   - If you hit CORS in the browser, verify server Access‑Control‑Allow‑Origin header; remember Postman does not enforce CORS.


## Key Vocabulary

**API (Application Programming Interface)**: A programmatic network interface that exposes data and functionality to other programs, commonly over HTTP using JSON.

**HTTP (Hypertext Transfer Protocol)**: The application‑level protocol most web APIs use; defines methods (GET, POST, etc.), headers, and status codes over TCP/SSL.

**REST (Representational State Transfer)**: An architectural style for web services emphasizing stateless interactions and resource representations; class focuses on HTTP verb → CRUD mapping.

**CRUD**: Create, Read, Update, Delete — the common operations mapped to HTTP methods (POST, GET, PUT/PATCH, DELETE).

**JSON (JavaScript Object Notation)**: A lightweight, machine‑readable data interchange format (key/value pairs and arrays) commonly used by APIs.

**HTML (HyperText Markup Language)**: Markup language intended for rendering content to humans in browsers; not ideal for structured machine consumption.

**Bearer token / Authorization header**: A token passed in the Authorization header (Authorization: Bearer <token>) used to authenticate API requests.

**Postman**: An interactive API client for composing, sending, and inspecting HTTP requests; useful for prototyping before coding.

**SMTP / IMAP / POP3**: Email application protocols: SMTP (send/submit, ports 25/587), IMAP (sync mail, ports 143/993), POP3 (download mail, ports 110/995).

**SSH (Secure Shell)**: An encrypted remote terminal protocol for secure shell access, file transfer (SFTP), and tunneling; preferred for remote admin.

**Telnet**: An older unencrypted remote terminal protocol (largely obsolete); historically notable (e.g., towel.blinkenlights.nl demo).

**Tailscale**: A mesh VPN built on WireGuard that connects devices securely without exposing public ports, recommended over raw port forwarding.

**NAT (Network Address Translation) / Port forwarding**: NAT maps private IPs to public IPs; port forwarding opens a private device’s port to the public internet (increasing attack surface).

## Review Questions

1. Explain how the HTTP methods GET, POST, PUT/PATCH, and DELETE map to CRUD actions and give one concrete example API path and method for each.
2. When should you use GET vs POST in an HTML form? List at least three behavioral or security consequences of using GET for sensitive data.
3. Describe the recommended way to send an API bearer token and three common reasons you might still get a 401 Unauthorized in your lab requests.
4. List the step‑by‑step Postman → code workflow and the five items in the troubleshooting checklist you should run before changing client code.
5. Compare JSON and HTML: for what use cases do you prefer each, and why is JSON the preferred API data format?
6. Name the main email protocols, their primary purpose, and the typical ports you would check if email delivery fails (include submission vs relay).
7. Explain why SSH is preferred over Telnet and why you should prefer Tailscale/VPN over port forwarding when exposing a home development service.
8. Given a response with HTTP 405 Method Not Allowed and another with 400 Bad Request, describe the likely causes and immediate fixes to try in Postman.
