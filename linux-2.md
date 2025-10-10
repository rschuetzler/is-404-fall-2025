# IS 404 — Linux 2 (September 18, 2025)

## Overview

This session deepened practical command-line fluency and explained the Linux file-permission model you will use when administering servers or deploying web apps. Focus on practicing terminal workflows (navigation, searching, editing, pipes/redirection, environment variables) and on changing/understanding permissions (chmod, chown, chgrp, sudo) so you're ready for Skill Check 1 and the upcoming exam.

## Outline

1. **Session goals & core takeaways**
   Know how to operate in a terminal-first environment, find and edit files, and correctly set ownership and permission bits to avoid common 'Permission denied' errors and security problems.
   - Use the terminal for server administration — GUI habits won’t always apply.
   - Interpret ls -l output to read permission bits and file type (e.g., -rw-r--r--, d for directories).
   - Apply the principle of least privilege — grant only the permissions required, avoid chmod 777.
   - Practice now: install the web server on your VM for Skill Check 1 (Learning Suite instructions).

2. **Command-line basics: navigation and listing**
   Memorize a few essential commands and flags to move around and inspect the filesystem quickly.
   - Run pwd to confirm your location and cd <path> to change directories.
   - Use ls -l to view permissions and ownership; use ls -a or ls -la to show hidden dotfiles (e.g., .git).
   - Use absolute paths (start with /) when you need an unambiguous target; use ~ for your home directory.
   - Practice: create directories with mkdir, create/update timestamps with touch, and remove carefully with rm.

3. **Finding text and files: grep, cat, find, and pipes**
   Chain simple commands with pipes and redirects to search and capture output — learning pipelines is high leverage.
   - Pipe stdout into other commands: e.g., ls | grep py to list entries containing 'py'.
   - Search file contents: cat file.py | grep import or grep -n 'pattern' file.py for line numbers.
   - Use > to overwrite and >> to append output to a file; recognize < as input redirection (less commonly used).
   - Combine commands practically: ps aux | grep nginx to find running processes related to nginx.

4. **Text editing and terminal tools**
   Know at least one terminal editor and the quick helpers to get documentation or richer UX.
   - Edit files with nano for simplicity or start learning vim for power; open VS Code from terminal with code . when available.
   - Use man <command> or <command> --help to read usage; use which <cmd> or whereis <cmd> to locate executables on $PATH.
   - Install better terminals (e.g., iTerm2 on macOS) for usability improvements like colors and drop-down panels.

5. **Environment variables and PATH**
   Use environment variables for configuration and secrets, and understand PATH so you can run tools without full paths.
   - Inspect variables with echo $VAR and list PATH with echo $PATH (colon-separated directories).
   - Export persistent variables in shell startup files (e.g., export MY_KEY=value in ~/.bashrc or ~/.profile).
   - Add a directory to PATH by exporting PATH="$HOME/bin:$PATH" so installed tools run by name.
   - Never hardcode secrets into source code — pass them via environment variables for deployments.

6. **Permissions model: read/write/execute and classes (u/g/o)**
   Understand the three permission types (r,w,x) and three classes (owner/user, group, others) and how they affect files and directories.
   - Interpret permission triplets: e.g., -rw-r--r-- = owner: rw-, group: r--, others: r--.
   - Remember directory execute bit: add x to a directory so it can be entered/traversed (chmod +x dir).
   - List files with ls -l to check both permission bits and owner/group before changing anything.
   - Practice concrete examples: chmod 744 file (owner rwx, group r, others r); chmod 000 file (no perms for anyone).

7. **Changing permissions and ownership (chmod, chown, chgrp, sudo)**
   Learn both symbolic and numeric chmod forms, and when to use chown/chgrp or sudo to resolve access issues safely.
   - Use octal chmod: digits represent owner/group/others, where 4=read, 2=write, 1=execute (e.g., chmod 750 file).
   - Use symbolic chmod for incremental changes: chmod u+x script.sh, chmod g-w file.txt, chmod o+r public.txt.
   - Change owner or group with chown <user> <file> and chgrp <group> <file>; be careful—wrong owner can lock you out.
   - Use sudo to run privileged commands; if you forgot sudo, run sudo !! to re-run the previous command as root.

8. **Security, troubleshooting, and best practices**
   Use minimal permissions, check ownership and groups when hitting 'Permission denied', and use available help resources.
   - Diagnose permission errors: run groups and ls -l to compare your user/group with file owner/group before chmod/chown.
   - Avoid chmod 777; instead grant specific bits needed (e.g., chmod 750 or 644 depending on use case).
   - Recover from mistakes: re-add execute to directories with chmod +x if you can't cd into them; consult TAs if unsure.
   - Use man pages, Google/ChatGPT, and the course slides/AI summaries when you need syntax or quick examples.

9. **Resources, assessments, and action items**
   Follow the hands-on tasks and study aids provided — install the web server now, practice commands, and prepare for the next exam.
   - Complete Skill Check 1: install the web server on your VM using Learning Suite instructions; ask TAs for help during lab time.
   - Memorize common flags: ls -a, ls -l, grep -n, and basic chmod usage; use the provided cheat sheet if requested.
   - Use roadmap.sh to align skills to career goals and review slides/AI summaries to prepare for the multiple-choice exam next Thursday.
   - Optionally request a printable cheat sheet or the in-class pop quiz converted to a practice quiz from the instructor.


## Key Vocabulary

**Permission bits (r, w, x)**: Three flags for each file/directory: read (r), write (w), and execute (x); they control who can view, modify, or execute files (execute on directories allows traversal).

**Classes (u, g, o)**: The three classes that permissions apply to: u = owner (user), g = group, o = others (everyone else).

**chmod**: Command to change file or directory permissions; supports numeric (octal) mode (e.g., 744) and symbolic mode (e.g., u+x, g-w).

**chown / chgrp**: chown changes the owner of a file; chgrp changes the group associated with a file. Both typically require sudo to change to another user/group.

**sudo**: Runs a command with superuser (root) privileges; only users in the sudoers group can use it. Shortcut sudo !! reruns the previous command as root.

**PATH**: An environment variable containing a colon-separated list of directories the shell searches for executables when you type a command name.

**Pipe (|) and redirection (>, >>, <)**: Pipe (|) sends stdout of one command to stdin of the next; > overwrites a file, >> appends, and < redirects file contents to a command's stdin.

**Dotfiles**: Files or directories whose names start with a dot (.) are hidden by default (e.g., .git, .bashrc). They are not secure by default—just out of the immediate listing.

## Review Questions

1. Interpret the permissions shown by ls -l: -rwxr-x--- owner=user1 group=dev. What can the owner, group, and others do? Give a chmod numeric command to set that state.
2. Explain the difference between chmod 744 and chmod u+x file.txt. When would you use symbolic vs numeric modes?
3. You try to edit /etc/nginx/nginx.conf and get 'Permission denied'. List the diagnostic steps you should take and at least two safe ways to proceed.
4. What does echo $PATH show and why might you add $HOME/bin to your PATH? Give the export command to do that for the current shell session.
5. Demonstrate a pipeline that lists Python files and shows only lines that contain import statements from those files (use commands shown in session).
6. What does chmod 000 file.py do, and how would the owner restore read and execute permissions using both numeric and symbolic forms?
7. Name three best practices from class for handling secrets and for setting file permissions on servers, with a short justification for each.
