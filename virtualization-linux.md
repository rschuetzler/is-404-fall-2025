# IS 404 — Virtualization and Linux (Sept 16, 2025)

## Overview

This session combined a compassionate opening about charity and peacemaking with a technical deep dive into virtualization and an introductory hands‑on with Linux VMs. Students practiced core CLI commands, learned hypervisor and networking concepts, and received step‑by‑step guidance for building and troubleshooting VMs for upcoming assignments.

## Outline

1. **Opening: Charity, Peacemaking, and Classroom Values**
   The instructor framed technical work within a values‑focused opening that emphasized small, consistent acts of service and peacemaking as practical habits that shape community behavior.
   - Reflect on the 'baffle' metaphor: small acts can interrupt harmful momentum—consider one concrete act you can do this week.
   - Connect class participation to service: sign up for prayer volunteers or Slack check‑ins as listed in LearningSuite.
   - Remember the teaching routine: Think → Pair → Share; use it to build and test mental models with a partner.

2. **Why Virtualization Matters (Big Picture)**
   Virtualization underpins modern cloud and data‑center operations by improving resource utilization, enabling isolation, and speeding provisioning; understanding desktop VMs builds intuition for cloud servers.
   - Describe virtualization as 'a computer inside a computer' — the VM (guest) runs on virtualized hardware from a hypervisor.
   - Explain cost benefits: consolidate many logical servers on one physical host to save space, power, and licensing (example: VMware consolidation savings slide).
   - List everyday examples: personal VMs on laptops, AWS EC2 instances, and instructor's Proxmox home server running services like Plex and VPN.

3. **Core Technical Concepts and Vocabulary**
   Master host vs guest, hypervisor types, RAM vs storage, ISOs, snapshots, and networking modes to correctly create and manage VMs.
   - Differentiate Type 1 (bare‑metal, e.g., Proxmox) vs Type 2 (hosted, e.g., VirtualBox) hypervisors and give an example use case for each.
   - Allocate resources deliberately: choose CPU cores, RAM, and storage when creating a VM; note that CPU/RAM are reserved only while the VM runs.
   - Treat an ISO like a CD image: use it to install an OS and then delete it if you don't need it after installation.
   - Use snapshots to capture a clean state after you install tools (e.g., create snapshot 'Clean-Tools' after installing VS Code).

4. **Hands‑On VM Setup, GUI vs CLI, and Troubleshooting**
   Follow practical steps for installing Ubuntu in a VM, choose between GUI and CLI based on the task, and know quick fixes if a VM is slow or won’t boot.
   - Follow LearningSuite now: install VS Code and the 'crack-attack' game inside your VM (or host) to practice package managers.
   - If the VM is slow, power it off and increase CPU cores or RAM (e.g., 2 cores → 4 cores, 4GB RAM → 8GB) and then restart.
   - When a VM won't boot: check that the ISO is attached correctly, verify boot order, confirm enough storage is allocated, and test networking mode.
   - Use snapshots and clones to recover quickly—restore a snapshot to revert to a known clean state in seconds.

5. **Command Line Review — Essential Commands**
   Be fluent with a minimal set of shell commands needed for file and directory operations; these are essential for server work and upcoming labs.
   - Use PWD to show your current directory and CD to change into another directory (example: cd ~/projects).
   - List files with LS, create directories with MKDIR (mkdir lab1), and create empty files with touch (touch notes.txt).
   - Copy files with CP (cp file.txt ../backup/), move/rename with MV (mv oldname.txt newname.txt).
   - Practice the commands in your VM terminal; expect more CLI practice later this week (Thursday session).

6. **Security, Isolation, and Practical Rules**
   VMs provide a safer environment for risky experiments, but default convenience features can weaken isolation; follow concrete steps to keep testing environments isolated.
   - Disable shared folders and shared clipboard if you require strong isolation for malware testing or sensitive experiments.
   - Remember that users are the largest vulnerability—inspect third‑party packages and prefer reputable sources (watch for compromised NPM packages).
   - When testing malware or suspicious software, snapshot then delete the VM rather than attempting to disinfect a host machine.
   - Use USB passthrough only when necessary and remove passthrough when finished to reduce attack surface.

7. **Networking Modes and Cloud Parallels**
   Understand NAT vs bridged networking on desktop VMs and map those ideas to cloud VM behavior and production tradeoffs.
   - Use NAT for default private internet access through the host; use bridged mode to give the VM its own IP on your LAN.
   - Recognize cloud VMs as similar to desktop VMs but often without a GUI and with provider-managed IP addressing and larger resource options.
   - When you need a publicly reachable machine (for a server demo), use bridged networking or a cloud VM with a public IP.

8. **Class Logistics, Expectations, and Next Steps**
   Follow the LearningSuite tasks and Slack for logistics; VMs are required for Skill Check 1 and additional CLI practice is scheduled this week.
   - Join Slack, check LearningSuite for the sign‑up survey, and complete the install tasks (VS Code + crack‑attack) before next class.
   - Use campus lab machines if your laptop cannot run VMs—labs have adequate CPU/RAM for assignments.
   - Bring incomplete setups to office hours or ask TAs for help; expect a BYU data‑center tour sign‑up and one daily section recording.


## Key Vocabulary

**Virtual Machine (VM)**: A guest operating system running on virtualized hardware inside another computer—essentially 'a computer inside a computer.'

**Hypervisor (Type 1 vs Type 2)**: Software that creates and runs VMs. Type 1 (bare‑metal) installs directly on hardware (e.g., Proxmox); Type 2 runs on a host OS (e.g., VirtualBox, UTM).

**Host vs Guest**: Host is the physical machine and its primary OS (your laptop); guest is the OS running inside the VM (e.g., Ubuntu).

**ISO**: A disk image file (like a virtual CD) used to install an operating system into a VM; can be deleted after installation if not needed.

**Snapshot**: A saved VM state (disk + memory/CPU state depending on settings) that lets you revert or clone an environment quickly.

**NAT vs Bridged Networking**: NAT gives the VM internet access through the host's IP (private from LAN); bridged mode assigns the VM its own IP on the local network.

**RAM vs Storage**: RAM (memory) is ephemeral workspace released when a VM powers off; storage (HDD/SSD) persists files across reboots and is usually a file on the host.

**Container**: A lightweight virtualization method (e.g., Docker, LXC) that shares the host kernel and isolates processes and filesystems differently than full VMs.

## Review Questions

1. Explain in your own words the difference between a Type 1 and Type 2 hypervisor and give one example of when you'd use each.
2. List the steps you would take to speed up a sluggish Ubuntu VM running on your laptop, and explain why each step helps.
3. Using the CLI commands from class, write the sequence of commands to create a directory called 'lab1', create an empty file 'notes.txt' inside it, and copy that file to a folder 'backup' one level above.
4. Describe two ways that VM convenience features can weaken isolation and what concrete settings you would change to make a VM safer for malware testing.
5. When should you keep an ISO file after installing an OS in a VM, and when is it safe to delete it? Give a concrete example.
6. Compare NAT and bridged networking modes: if you want to run a web server accessible to other machines on your dorm network, which mode should you choose and why?
7. Explain why snapshots are useful in coursework and provide a concrete naming convention and timing for when to take a snapshot during VM setup (example: after installing core tools).
