# Linux Review Guide (Day 3)

## Main Topics

### 1. Why Linux?
- **Servers and market share**: About 90% of servers run Linux/Unix-like operating systems; Windows has ~10%:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}.
- **Astronauts joke**: “You can’t open Windows in space” — memorable way of stressing Linux’s importance.

### 2. Basic Linux Navigation and Commands
- **Navigation**:  
  - `cd` (change directory)  
  - `pwd` (print working directory)  
  - `.` (current directory), `..` (parent directory), `../..` (two levels up)  
  - `clear` (clear terminal screen)  

- **File and directory management**:  
  - `ls` (list files; options `-a` for all, `-l` for detailed view)  
  - `mkdir` (make directory)  
  - `touch` (create new file / update timestamp)  
  - `cp` (copy files)  
  - `mv` (move or rename files)  
  - `rm` (remove files)  

- **Working with files and text**:  
  - `cat` (display file contents)  
  - `nano` (command-line text editor)  
  - `echo` (print text or write text to files)  

- **Redirection and piping**:  
  - `>` (redirect/overwrite output to file)  
  - `>>` (append output to file)  
  - `|` (pipe: send output of one command as input to another, often with `grep`)  

- **Searching**:  
  - `grep` (search text, often used with pipes)  

- **Environment and system**:  
  - `env` (show environment variables)  
  - PATH variable: tells the shell where to look for commands/programs.  

### 3. Linux Permissions
- **Permission types**: Read (r), Write (w), Execute (x).  
- **Permission groups**: Owner, Group, Others.  
- **Viewing permissions**: `ls -l`  
- **Changing permissions**:  
  - `chmod` (change permissions; numeric codes 4=read, 2=write, 1=execute).  
  - `chown` (change file owner).  
  - `chgrp` (change group).  
- **Superuser commands**:  
  - `sudo` (run as root).  
  - Only users in the sudo group can use it.  
  - `sudo !!` re-runs the last command with sudo.  

### 4. Getting Help
- `command --help` or `command -h` (sometimes).  
- `man command` (open manual).  
- Online search, documentation, and tools like ChatGPT.  

---

## Review Questions

### Linux Basics
1. What percentage of servers run Linux or Unix-like operating systems? Why is this important for learning Linux?  
2. What do the following commands do: `cd`, `pwd`, `ls -a`, `ls -l`?  
3. What is the difference between `cat` and `ls`?  
4. How are hidden files represented in Linux, and how can you see them?  
5. What does the `touch` command do if the file already exists?  

### File Management & Redirection
6. How do you create a new directory? How do you remove one?  
7. How do you copy a file? Move a file? Delete a file?  
8. What is the difference between `>` and `>>`?  
9. What does the pipe (`|`) operator do? Give an example of using `ls` with `grep`.  
10. What does `echo "Hello" > file.txt` do?  

### Editing & Environment
11. What is `nano` and why is it useful on a server?  
12. What is the PATH environment variable and why is it important?  
13. How can you check the value of an environment variable?  

### Permissions
14. What are the three types of Linux permissions?  
15. Who are permissions assigned to (the three groups)?  
16. How do you view file permissions?  
17. How does `chmod 744 file.txt` change permissions?  
18. What is the difference between `chmod`, `chown`, and `chgrp`?  
19. What does `sudo` do, and who can use it?  
20. What does `sudo !!` do?  

### Help & Resources
21. How can you find documentation for a Linux command from the terminal?  
22. Why might using `man` or `--help` be better than just guessing command syntax?  
