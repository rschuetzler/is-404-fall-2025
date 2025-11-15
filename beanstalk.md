# IS 404 — Beanstalk (Elastic Beanstalk) Study Guide

## Overview

This packet combines lecture, in-class demos, and the supplemental deployment guides to prepare you for deploying Node.js apps with AWS Elastic Beanstalk (EB). Read it as a checklist + quick reference for the deploy → read logs → fix → re‑deploy iterative workflow you'll use in quizzes and labs.

## Outline

1. **Cloud service model and practical implications**
   Understand where Elastic Beanstalk sits in the cloud-service spectrum and the tradeoffs between operational burden and control.
   - Place EB on the spectrum: On‑prem → IaaS (EC2) → PaaS (Elastic Beanstalk) → FaaS → SaaS; EB is PaaS so AWS manages instances, OS, and runtime images while you supply code and configuration.
   - Compare responsibilities: AWS handles provisioning, runtime installation and instance lifecycle; you handle application correctness, schema/data, secrets and cost management.
   - Decide when to move right or left: use EB for speed and reduced ops; use Docker/containers or EC2 when you need OS-level control or custom runtimes.

2. **What Elastic Beanstalk automates and what you must manage**
   Know the exact boundaries of EB automation so you can prepare your app and environment correctly.
   - EB automates: provisioning EC2 instances, installing Node runtime, starting your app (using package.json start), wiring load balancers/auto-scaling, exposing health metrics, and injecting RDS env vars when requested.
   - You must: write correct application code, provide migrations or seed data for RDS, manage secrets via EB environment properties (never commit .env), and control costed AWS resources.
   - Use EB application versions: upload a ZIP package (created by git archive of committed files) as each deployable release.

3. **Packaging and Git workflow (prepare the deployable artifact)**
   Follow a deterministic packaging process so what you test locally is what runs on EB.
   - Confirm repository root: open your project folder in VS Code and ensure .git exists in that root (avoid stray ancestor .git folders).
   - Use .gitignore to exclude node_modules/, .env and *.zip so you don't commit secrets or bulky files. Example entries: "node_modules/", ".env", "*.zip".
   - Ensure package.json contains a start script (e.g., "start": "node index.js") and use process.env.PORT in your server: "const port = process.env.PORT || 3000;"
   - Create a zip of committed files with git archive, e.g.: "git archive --format=zip --output=v1.zip main" — always commit before archiving.

4. **Deploy loop: how to deploy, observe, and iterate**
   Use the repeatable loop demonstrated in class to deploy reliably and fix issues quickly.
   - Iterative steps: commit changes → git archive (zip) → upload zip as new EB application version → watch Environment events and health → download logs → fix locally → commit → repeat.
   - Use the EB console: Application → Environment → Upload and deploy application version; check Environment → Health and Domain link to verify.
   - For CI/CD: set up CodePipeline/GitHub Actions in your own AWS account for automation (not available in the Learner Lab).

5. **Troubleshooting & logs — where to look and common fixes**
   Know exact log locations and common root causes so you can quickly diagnose failures after deploy.
   - Check logs in EB console: Environment → Logs → Request logs → "Last 100 lines" or download full logs; search for the word "error" and read from the bottom (most recent).
   - Key log files on instances: /var/log/web.stdout.log (your Node app stdout/stderr), /var/log/eb-engine.log (Beanstalk agent/runtime errors), /var/log/nginx/access.log and /var/log/nginx/error.log (nginx routing/TLS issues).
   - Common fixes: add a missing "start" script in package.json; use process.env.PORT; don’t connect to DB at localhost — use EB-injected RDS env vars (RDS_HOSTNAME, RDS_USERNAME, RDS_PASSWORD, RDS_DB_NAME, RDS_PORT); enable DB SSL when required.
   - If tables are missing: run migrations (preferred) or manually create tables after opening RDS access for your IP using a DB client.

6. **RDS integration, migrations, and SSL handling**
   Prepare your app to read EB-provided database credentials and to run migrations so production databases are reproducible.
   - When EB creates an RDS instance it injects connection values into env vars (RDS_HOSTNAME, etc.); update your DB config to prefer these values.
   - Prefer running migrations (Knex or similar) to create tables reproducibly; keep migration scripts in source control and run them as a deploy step or separate job.
   - Handle SSL differences: use an env toggle like DB_SSL and configure your client accordingly (example: knex ssl: process.env.DB_SSL ? { rejectUnauthorized: false } : false).

7. **Runtime pattern: nginx reverse proxy + Node.js process**
   Understand why EB uses nginx as a front-end and how Node should be configured to cooperate.
   - Pattern: nginx terminates TLS, serves static assets and proxies dynamic requests to a Node process listening on an internal port (provided via process.env.PORT).
   - Benefits: let nginx handle HTTP/TLS optimizations and connection management while Node handles application logic; use host-based routing or ALB/ELB for multi-host setups.
   - For HTTPS on single-instance EB: you can add certbot + nginx config files (example walkthrough exists in supplemental guides) but prefer IaC if you must recreate certs/configs.

8. **Operations, deployment strategies, and when to use containers**
   Know operational best practices (blue/green, cost awareness) and when to transition to Docker or lower-level services.
   - Perform blue/green deploys: deploy the new version to a parallel environment, test it, then swap traffic to avoid downtime and simplify rollback.
   - Monitor costs: EB often creates EC2 and RDS resources that bill in normal AWS accounts — terminate environments and RDS when not needed.
   - Choose containers (Docker) when you need custom OS packages or specific runtime versions that EB's managed platform doesn't support; containers are next in the course.

9. **Actionable pre-deploy checklist (what to do before your first EB deploy)**
   A one-stop checklist you can run through before uploading your first zip to EB — follow these items in order.
   - Run locally: npm install and npm start to verify the app works before deploying.
   - Add package.json start script and use process.env.PORT in your code.
   - Create .gitignore with at least: node_modules/, .env, *.zip and initialize Git in the project root.
   - Commit all changes; create a zip for deployment: git archive --format=zip --output=v1.zip main.
   - In EB console: Create application → Web server environment → Platform: Node.js → Upload zip. If adding RDS, enable it during environment creation.
   - After deploy: check Health and Domain link; if errors, download logs and inspect /var/log/web.stdout.log and /var/log/eb-engine.log, fix locally, commit, re-archive and re-deploy.


## Key Vocabulary

**Elastic Beanstalk (EB)**: AWS PaaS that provisions and manages instances, runtimes (like Node.js), and instance lifecycle so you can provide application code and configuration.

**Platform-as-a-Service (PaaS)**: Cloud model where the provider manages OS and runtime; the user supplies application code and configuration but has less OS-level control.

**Infrastructure as Code (IaC)**: The practice of declaring and scripting provisioning/configuration so environments are reproducible, auditable, and recoverable.

**Reverse proxy**: A server (e.g., nginx) that accepts client requests, terminates TLS/handles static assets, and forwards dynamic requests to backend services like a Node process.

**nginx**: High-performance HTTP server and reverse proxy commonly used in front of application servers to handle TLS, caching, and connection management.

**RDS**: AWS Relational Database Service; can be provisioned by EB and exposes connection details to your app via environment variables.

**Environment property (EB env var)**: Key/value pairs configured on an EB environment that are injected into running application processes for configuration and secrets.

**git archive**: A Git command that creates a zip/tar archive of the committed files in a branch; use it to create deterministic deployment packages (e.g., git archive --format=zip --output=v1.zip main).

**.gitignore**: A repository file listing patterns that Git should ignore (commonly used to exclude node_modules/, .env and generated zip files).

**Blue/green deploy**: A deployment strategy that creates a parallel environment for the new version and swaps traffic after verification to reduce downtime and rollback risk.

**Knex**: A Node.js SQL query builder and migration tool often used to define and run database schema migrations as part of deploys.

**Bus factor**: A measure of project risk: how many people can be unavailable (e.g., 'hit by a bus') before the project cannot continue; IaC and docs reduce bus factor risk.

## Review Questions

1. 1) Describe what Elastic Beanstalk manages for you and list three responsibilities you still must handle when deploying a Node.js app.
2. 2) What exact command sequence produces a deployment ZIP from committed files in Git? Explain why uncommitted files are excluded.
3. 3) Where should you look first when your EB-deployed app returns a 500 or fails to start? Name two specific log files and what they contain.
4. 4) How should your Node app choose its port so it works on EB and locally? Show the code line(s) you would use.
5. 5) EB can inject RDS connection info via env vars. Name at least three of those env vars and explain how you would modify your DB config to enable SSL only in production.
6. 6) Explain blue/green deployment and why it can be safer than directly updating an existing environment.
7. 7) When would you choose Docker/containers over Elastic Beanstalk for deployment? Give two concrete reasons.
