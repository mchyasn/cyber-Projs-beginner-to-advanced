System Vulnerability Scanning with LinPEAS & Nmap

Project Description:
Use LinPEAS and Nmap to find vulnerabilities on a local or remote Linux system. This is useful for both local privilege escalation and remote enumeration.

Project Structure:
SystemVulnScanner/
├── screenshots/
│   ├── step0.png
│   ├── step1.png
│   └── step2.png
├── linpeas.sh
└── README.md

Installation and Usage:

Step 0: Setup Project Folder
mkdir SystemVulnScanner
cd SystemVulnScanner
mkdir screenshots
Screenshot: screenshots/step0.png - Terminal showing folder creation.

Step 1: Local Enumeration with LinPEAS
Download LinPEAS:
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
Run LinPEAS on your Kali system or a test VM:
./linpeas.sh
Screenshot: screenshots/step1.png - Running linpeas.sh and showing colorful output.
Save or export the results for review.

Step 2: Remote Scan with Nmap Vulnerability Scripts
Use Nmap's NSE scripts to check for known vulnerabilities:
nmap -sV --script vuln 127.0.0.1
You can replace 127.0.0.1 with another host on your network.
Screenshot: screenshots/step2.png - Nmap output showing vulnerable or safe ports.