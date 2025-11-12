# IS 404 — AWS and Cloud (Session: November 11, 2025)

## Overview

This study packet synthesizes lecture slides, readings, and in-class artifacts to give you a concise checklist of what to know for quizzes and the Elastic Beanstalk lab. Focus on service roles (EC2, S3, RDS, DynamoDB, Route 53), networking and availability (Regions/AZs, VPCs), scaling and database tradeoffs, security responsibilities, large-data ingress options, and the Well‑Architected pillars.

## Outline

1. **AWS core services — what they do and when to use them**
   Understand each service's primary function, operational responsibilities, and a concrete use case so you can choose the right tool for a given problem.
   - Describe EC2 as virtual machines you manage (OS, patching, backups). Example: use EC2 for custom application servers; pick compute-optimized (c-series) for heavy CPU jobs or memory-optimized (r-series) for in-memory caches.
   - Use S3 for object storage (photos, backups, static website assets); store the object URL or path in your relational DB rather than BLOBs inside tables.
   - Pick RDS (managed) for relational workloads needing automated backups and multi‑AZ failover (MySQL, PostgreSQL, Aurora); create read replicas for read scaling.
   - Choose DynamoDB for high-throughput, low-latency key-value/document workloads where a flexible schema and massive horizontal scaling are required.
   - Use Route 53 for DNS: register domains, configure weighted/geolocation routing, and set health checks (mnemonic: port 53).
   - Leverage Elastic Beanstalk to deploy web apps quickly: upload code, let Beanstalk create ELB/ASG/EC2 and optionally RDS, and retain the option to take over resources manually.

2. **Networking, isolation, and global infrastructure**
   Know how VPCs, security groups, Regions, AZs, Local Zones and networking choices affect availability, latency and security.
   - Explain VPC as a logically isolated virtual network; map home-network analogy: internet gateway = modem, route table = router, devices = EC2 instances.
   - Configure Security Groups as instance-level, stateful firewalls and use Network ACLs for stateless subnet filtering.
   - Deploy across multiple AZs for high availability; replicate across regions for disaster recovery or geo-locality; choose the region closest to users to reduce latency.
   - Consider Local Zones/Wavelength when your app needs ultra-low latency to a specific metro or telco edge.

3. **Scaling patterns and database constraints**
   Distinguish vertical vs horizontal scaling and the practical strategies for scaling databases and application tiers.
   - Use vertical scaling (scale up) to increase instance size for simplicity; expect downtime and finite limits.
   - Use horizontal scaling (scale out) with load balancers and Auto Scaling Groups for resilience and elasticity; example: put web servers behind an ALB, scale based on CPU or request count.
   - Scale reads via read replicas; scale writes by sharding/partitioning or moving write-heavy workloads to specialized stores; consider caching (Redis/Memcached) to reduce DB load.
   - When writes are the bottleneck, evaluate sharding vs moving to a NoSQL store; document expected growth and operational complexity before choosing.

4. **Managed vs self-hosted databases — tradeoffs and operational tasks**
   Compare managed services (RDS/Aurora/DynamoDB) with self-hosted DBs on EC2 and list the daily ops implications of each choice.
   - Choose managed RDS when you want automated backups, patching, snapshots and easier failover—trade loss of some low-level control for reduced ops burden.
   - Choose self-hosted on EC2 when you need custom OS-level tuning, nonstandard DB engines, or potential cost advantages at massive scale—but plan for manual patching, backups, clustering and monitoring.
   - List operational tasks for self-hosted DBs: OS patching, backup scheduling and testing, monitoring alerts, failover automation, and security hardening (ports, encryption).
   - Use the HEY/Basecamp reading to justify when predictable, large steady-state workloads might prefer owned hardware or self-hosted solutions for cost reasons.

5. **Security: Shared Responsibility Model and IAM best practices**
   Apply the Shared Responsibility Model and concrete IAM/security actions you must take as the customer.
   - State the model: AWS = security of the cloud (infrastructure, physical data centers); customer = security in the cloud (data, OS, apps, IAM, configurations).
   - Implement least privilege with IAM: create roles for services, use short-lived credentials, and audit policies regularly.
   - Protect data at rest and in transit: enable encryption (S3/KMS, RDS encryption), use HTTPS/TLS for traffic, and rotate keys.
   - Automate security checks and logging: enable CloudTrail, VPC Flow Logs, and monitoring/alerting to provide traceability and incident response.

6. **Well‑Architected Framework & cost/operational checklists**
   Use the five pillars as a practical checklist to evaluate architecture decisions and to prepare for quizzes and lab grading.
   - Apply cost optimization: turn off unused resources, use reserved instances when stable, and monitor billing and cost allocation tags.
   - Design for reliability: add redundancy across AZs, test disaster recovery, and automate recovery runbooks.
   - Optimize performance: choose appropriate instance types, use caching, and measure before changing architecture.
   - Enforce operational excellence: document runbooks, run post‑incident reviews, and use automation for repeatable operations.
   - Treat security as a pillar: enforce strong identity foundations, logging, and automated remediation.

7. **Large data ingress and the Snow family**
   For multi‑terabyte to petabyte transfers, decide between network upload and physical transfer; know the Snow family options and their use cases.
   - For < tens of TB: prefer network upload (multipart S3 uploads, DataSync) if bandwidth allows.
   - For 10s–100s of TB or PB: use Snowcone/Snowball Edge or Snowmobile (or AWS physical transfer terminals) depending on size and compute needs; example: ship a Snowball Edge for 100 TB or Snowmobile for 100+ PB.
   - Plan secure shipment and ingestion: encrypt data before shipping, catalog contents, and run local verification before returning devices.
   - Incorporate ingestion choice early in architecture planning to avoid late-stage bottlenecks.

8. **Deployment models and Elastic Beanstalk lab preparation**
   Know cloud vs hybrid vs on‑prem tradeoffs and prepare for the hands‑on Elastic Beanstalk deployment steps and operational hygiene.
   - Compare deployment models: cloud-native for agility and low upfront cost; hybrid for phased migrations or compliance; on-prem for strict data sovereignty/low latency.
   - Before the lab: practice a local deployment, confirm team roles, and ensure a fallback AWS learner account for permissions or billing issues.
   - During the lab: observe Beanstalk-created resources (ELB, ASG, EC2, optional RDS); use the Beanstalk console to check logs, health, and scaling events.
   - After the lab: terminate environments or run cleanup scripts to avoid charges, and review logs and monitoring metrics to learn debugging steps.


## Key Vocabulary

**Availability Zone (AZ)**: A physically separate fault domain (data center or cluster) within an AWS Region used to provide high availability and redundancy.

**Region**: A geographic area that contains multiple Availability Zones; choose regions to balance latency, compliance, and cost.

**EC2 (Elastic Compute Cloud)**: AWS virtual machines (instances) that you provision and manage; you are responsible for the OS, patches and backups.

**S3 (Simple Storage Service)**: Object storage for static assets, user media, backups and archives; supports multiple storage classes and lifecycle rules for cost optimization.

**RDS (Relational Database Service)**: Managed relational database service offering automated backups, patching, snapshots, and multi‑AZ options for engines like MySQL/Postgres/Aurora.

**DynamoDB**: Fully managed NoSQL key-value/document database for high-throughput, low-latency workloads and schema flexibility.

**Route 53**: AWS DNS and domain registration service that routes traffic (supports weighted, geolocation routing and health checks) — mnemonic: port 53.

**VPC (Virtual Private Cloud)**: A logically isolated virtual network in AWS where you define subnets, route tables, NAT/gateways and control inbound/outbound traffic.

**Security Group**: Instance-level, stateful firewall rules that control inbound and outbound traffic for EC2 and other resources.

**Shared Responsibility Model**: AWS concept that AWS secures the cloud infrastructure while customers secure data, applications, OS configurations and identities within the cloud.

**Elastic Beanstalk**: A managed deployment service that provisions EC2, load balancing and autoscaling for web apps while allowing you to retain control of underlying resources.

**Snow Family**: Physical devices (Snowcone, Snowball Edge, Snowmobile) for edge compute and large-scale secure data transfer to AWS when network transfer is impractical.

## Review Questions

1. List the primary responsibilities you keep when you run an application on EC2 vs when you use RDS. Give two concrete tasks for each scenario.
2. Sketch (in words) a three‑tier web app architecture that serves user photos. Specify where you would store photos, where you would store metadata, and how you would enable scaling and availability.
3. Explain vertical versus horizontal scaling. For a bursty web application with unpredictable peak traffic, which scaling approach would you favor and why? Name the AWS services you would combine.
4. Given a one-time 50 TB dataset to import to AWS from an on‑prem data center, list the practical ingestion options, and state the pros/cons that would lead you to choose a Snow family device versus network upload.
5. Using the Shared Responsibility Model, identify three security controls that remain the customer's responsibility even when using managed services like RDS or S3.
6. Name the five pillars of the Well‑Architected Framework and give one concrete action you would take to address each pillar in a simple web app deployment.
7. Describe what Elastic Beanstalk creates for you during a standard web app deployment and list three places you would look to debug a failing deployment.
8. Summarize the HEY/Basecamp argument for leaving the cloud: identify one scenario where owning infrastructure may be cheaper and one scenario where the cloud is clearly superior.
