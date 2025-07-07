# Internal Network Recon Project

This beginner-level cybersecurity project simulates internal network reconnaissance using **Nmap** inside a virtual lab (Kali Linux + Windows 11). Each step includes commands, screenshots, and output files for full documentation.


##  Step-by-Step

###  Step 1: Get Your IP Address (Kali Linux)

Command:
```bash
ip a
```
![Network IP Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/ip.a.png)


###  Step 2: Create Output Directory

Command:
```bash
mkdir -p ~/Desktop/scans
```
![Output Directory Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/Create-Output-Directory.png)

###  Step 3: Ping Sweep (Detect Live Hosts)

Command:
```bash
nmap -sn 192.168.44.0/24 -oN ~/Desktop/scans/ping-scan.txt
```
![Network Ping Sweep](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/ping-sweep.png)

###  Step 4: Full Port Scan on Target

Command:
```bash
nmap --privileged -p- 192.168.44.130 -oN ~/Desktop/scans/port-scan.txt
```
![Network Host Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/full-detection.png)

###  Step 5: Quick TCP SYN Scan

Command:
```bash
nmap -sS 192.168.44.130 -oN ~/Desktop/scans/quick-scan.txt
```

![Quick Network Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/quick-scan.png)

### Step 6: Final Service + OS Detection Scan

Command:
```bash
nmap -sS -sV -O 192.168.44.130 -oN ~/Desktop/scans/final-scan.txt
```

![Network Host Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/full-detection.png)



###  Step 7: Enable Windows Firewall Rules

Command (on Windows 11 VM, PowerShell):

```powershell
New-NetFirewallRule -DisplayName "Allow RDP" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow
New-NetFirewallRule -DisplayName "Allow SMB" -Direction Inbound -Protocol TCP -LocalPort 445 -Action Allow
New-NetFirewallRule -DisplayName "Allow RPC" -Direction Inbound -Protocol TCP -LocalPort 135 -Action Allow
```
![Firewall Rules Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/Internal-Recon/screenshots/firewall-rules.png)



##  Summary

| Step | Purpose |
|------|---------|
| 1    | Find Kali VM's IP |
| 2    | Create folder for outputs |
| 3    | Discover live hosts on subnet |
| 4    | Full port scan on target |
| 5    | Quick scan for open TCP ports |
| 6    | Detect services + OS |
| 7    | Open necessary firewall ports in Windows |


##  Skills Practiced

- Internal recon with `nmap`
- Firewall configuration (Windows)
- Scanning methodology
- Screenshot documentation
- Result analysis and port identification
