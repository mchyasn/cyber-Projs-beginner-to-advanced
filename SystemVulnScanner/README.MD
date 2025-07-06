System Vulnerability Scanning
=============================

This project demonstrates how to scan a local or remote Linux system for vulnerabilities using two primary tools: LinPEAS for local enumeration and Nmap for remote scanning using NSE scripts.


Step 0: Create Project Folder
-----------------------------
Create the project folder and organize files:

    mkdir SystemVulnScanner
    cd SystemVulnScanner
    mkdir screenshots

Step 1: Local Enumeration with LinPEAS
--------------------------------------
1. Download and give execute permission:

    wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
    chmod +x linpeas.sh

2. Run LinPEAS:

    ./linpeas.sh
![System Vulnerability Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/SystemVulnScanner/screenshots/Screenshot%202025-07-05%20161915.png)


3. Review the output for potential privilege escalation vectors, insecure configurations, and outdated software.
![Vulnerability Scan Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/SystemVulnScanner/screenshots/Screenshot%202025-07-05%20162406.png)
![System Scan Details](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/SystemVulnScanner/screenshots/Screenshot%202025-07-05%20162428.png)
Step 2: Remote Vulnerability Scanning with Nmap
-----------------------------------------------
Run an Nmap scan against the local or remote system:

    nmap -sV --script vuln 127.0.0.1
![Nmap Scan Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/SystemVulnScanner/screenshots/nmap00.png)

This uses Nmap's vulnerability scripts to identify exposed services and known CVEs.

