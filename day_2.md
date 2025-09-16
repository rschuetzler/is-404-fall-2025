# IS 404 – Day 2 Review Guide  
**Topic: Virtualization & Linux**

## Main Topics

### 1. Virtualization Basics
- **Definition**: Running a computer inside a computer (“a virtual machine” or VM).
- **How it works**:  
  - Allocate resources (CPU cores, RAM, storage).  
  - Insert a virtual disk image (ISO) with an operating system installer.  
  - Boot and install the OS onto virtual storage.  
- **Hypervisors**: Software that manages VMs.  
  - *Type 1 (bare-metal)*: Runs directly on hardware.  
  - *Type 2*: Runs on top of a host OS (e.g., VirtualBox, VMware, Hyper-V, UTM).  

### 2. Benefits of Virtualization
- **Resource utilization**: Cheaper and more efficient to run one big server split into VMs than many small servers.  
- **Isolation**: Each VM is separate from the host and from other VMs → useful for security, testing, and running risky software.  
- **Ease of setup/takedown**: Hypervisors allow cloning, snapshots, and easy resets.  

### 3. Virtualization in Practice
- **Desktop virtualization**: Run alternate operating systems (Linux on Windows/Mac, or vice versa). Useful for compatibility or testing.  
- **Server/cloud virtualization**: Most servers and cloud services (AWS EC2, Azure, etc.) run on VMs. Students will use AWS later in the course.  
- **Performance tradeoffs**: VM speed depends on allocated resources; shutting down the VM releases resources back to the host.  

### 4. Linux Basics
- **Why Linux?**  
  - Dominates server market (≈ 2/3 to 3/4 of servers).  
  - Open source, free, widely supported.  
  - Based on Unix (similar roots as macOS).  
- **Using Linux in class**:  
  - Students interact with Ubuntu in VMs.  
  - Practice with the **command line**.  
  - Learn core commands (e.g., `pwd`, `ls`, navigating directories).  
  - Understand that “directory” and “folder” are the same thing.  

---

## Review Questions

### Virtualization Concepts
1. What is a virtual machine, and how is it created?  
2. What role does an ISO file play in creating a VM?  
3. What is a hypervisor, and how do Type 1 and Type 2 hypervisors differ?  
4. Why is virtualization widely used in cloud computing?  
5. How does virtualization improve resource utilization compared to running many small physical servers?  
6. Why is environment isolation important when running applications or testing software in a VM?  

### Practical Applications
7. Give an example of when you might use desktop virtualization versus server virtualization.  
8. Why might someone use a VM for testing malware or doing sensitive tasks like online banking?  
9. What happens to your host computer’s resources (CPU, RAM) when you shut down a VM?  
10. Can you run a virtual machine inside another virtual machine? Why or why not?  

### Linux Basics
11. Why is Linux such an important operating system to learn for working with servers?  
12. What advantages does Linux have in terms of cost and licensing?  
13. What is the relationship between Linux and Unix?  
14. On the command line, what does `pwd` do?  
15. What’s the difference (if any) between a directory and a folder?  
