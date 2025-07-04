
# 🕵️ Internal Network Recon Project

This beginner-level cybersecurity project simulates internal network reconnaissance using **Nmap** inside a virtual lab (Kali Linux + Windows 11). Each step includes commands, screenshots, and output files for full documentation.

---

## 📁 Folder Structure

```
Internal-Recon/
│
├── scans/
│   ├── ping-scan.txt
│   ├── port-scan.txt
│   ├── quick-scan.txt
│   └── final-scan.txt
│
├── screenshots/
│   ├── Create-Output-Directory.png
│   ├── firewall-rules.png
│   ├── full-detection.png
│   ├── ip.a.png
│   ├── ping-sweep.png
│   └── quick-scan.png
│
└── README.md
```

---

## 🧪 Step-by-Step

### ✅ Step 1: Get Your IP Address (Kali Linux)

Command:
```bash
ip a
```

📸 Screenshot:  
![IP Address](screenshots/ip.a.png)

---

### ✅ Step 2: Create Output Directory

Command:
```bash
mkdir -p ~/Desktop/scans
```

📸 Screenshot:  
![Create Output Directory](screenshots/Create-Output-Directory.png)

---

### ✅ Step 3: Ping Sweep (Detect Live Hosts)

Command:
```bash
nmap -sn 192.168.44.0/24 -oN ~/Desktop/scans/ping-scan.txt
```

📄 [ping-scan.txt](scans/ping-scan.txt)  
📸 Screenshot:  
![Ping Sweep](screenshots/ping-sweep.png)

---

### ✅ Step 4: Full Port Scan on Target

Command:
```bash
nmap --privileged -p- 192.168.44.130 -oN ~/Desktop/scans/port-scan.txt
```

📄 [port-scan.txt](scans/port-scan.txt)

---

### ✅ Step 5: Quick TCP SYN Scan

Command:
```bash
nmap -sS 192.168.44.130 -oN ~/Desktop/scans/quick-scan.txt
```

📄 [quick-scan.txt](scans/quick-scan.txt)  
📸 Screenshot:  
![Quick Scan](screenshots/quick-scan.png)

---

### ✅ Step 6: Final Service + OS Detection Scan

Command:
```bash
nmap -sS -sV -O 192.168.44.130 -oN ~/Desktop/scans/final-scan.txt
```

📄 [final-scan.txt](scans/final-scan.txt)  
📸 Screenshot:  
![Full Detection](screenshots/full-detection.png)

---

### ✅ Step 7: Enable Windows Firewall Rules

Command (on Windows 11 VM, PowerShell):

```powershell
New-NetFirewallRule -DisplayName "Allow RDP" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Allow
New-NetFirewallRule -DisplayName "Allow SMB" -Direction Inbound -Protocol TCP -LocalPort 445 -Action Allow
New-NetFirewallRule -DisplayName "Allow RPC" -Direction Inbound -Protocol TCP -LocalPort 135 -Action Allow
```

📸 Screenshot:  
![Firewall Rules](screenshots/firewall-rules.png)

---

## ✅ Summary

| Step | Purpose |
|------|---------|
| 1    | Find Kali VM's IP |
| 2    | Create folder for outputs |
| 3    | Discover live hosts on subnet |
| 4    | Full port scan on target |
| 5    | Quick scan for open TCP ports |
| 6    | Detect services + OS |
| 7    | Open necessary firewall ports in Windows |

---

## 🧠 Skills Practiced

- Internal recon with `nmap`
- Firewall configuration (Windows)
- Scanning methodology
- Screenshot documentation
- Result analysis and port identification

---

> 🛡️ Keep building more advanced steps — we’ll add them in this repo. Need help with the next project? I’m ready.
