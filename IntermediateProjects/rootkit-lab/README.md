# Rootkit Lab: Hiding a Process by PID

This project demonstrates a basic Loadable Kernel Module (LKM) rootkit that hides a specific process from user-space tools by filtering kernel interactions. The goal is to understand how kernel modules can be used to manipulate visibility of processes in Linux.

## Objective

To create and insert a kernel module that hides a process with a specific PID (e.g., 9999) from tools like `ps` and `/proc`, using safe and isolated testing in Kali Linux.

## Environment

- Kali Linux (virtual machine, isolated)
- Linux Kernel Headers installed
- Custom kernel module (written in C)
- Kernel version: 6.12.33+kali-amd64

## Execution Steps

1. **Setup environment and install headers**  
   ```bash
   sudo apt install linux-headers-$(uname -r) -y
   ```
![Rootkit Behavior Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/rootkit-lab/screenshots/0.png)

2. **Build the module**  
   ```bash
   make clean
   make
   ```
![Rootkit Behavior Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/rootkit-lab/screenshots/3.png)

3. **Run a test process to hide**  
   ```bash
   sleep 1000 &
   echo $!  # Note this PID (e.g., 9999)
   ```

4. **Insert the rootkit module**  
   ```bash
   sudo insmod rk_hideproc.ko hide_pid=9999
   dmesg | tail
   ```
![Rootkit Behavior Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/rootkit-lab/screenshots/4.png)

5. **Check process visibility**  
   ```bash
   ps aux | grep 9999
   ```

   The target PID should be hidden from the output.

6. **Remove the module**  
   ```bash
   sudo rmmod rk_hideproc
   dmesg | tail
   ```
![Rootkit Behavior Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/rootkit-lab/screenshots/2.png)

7. **Verify the process reappears**  
   ```bash
   ps aux | grep 9999
   ```
![Rootkit Behavior Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/rootkit-lab/screenshots/5.png)

## Disclaimer

This project is intended for educational purposes only. All development and testing were conducted in a secure, virtualized lab. Do not deploy rootkits or similar code on production systems or unauthorized machines.

## Author

Developed by [mchyasn](https://github.com/mchyasn)
