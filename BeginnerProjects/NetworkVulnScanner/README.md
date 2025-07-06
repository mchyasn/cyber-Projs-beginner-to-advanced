
# Network Vulnerability Scanner (Beginner Project)

## Description

This project performs basic network vulnerability scanning using `nmap` to identify open ports, detect services, and attempt OS fingerprinting on LAN devices. It simulates a foundational security assessment of your own home network.

> ⚠️ Ethical use only — always scan networks you own or have permission to test.

## Tools Used

- `nmap` – Network Mapper for port scanning, service detection, and OS fingerprinting

---
---

### Step 1: Basic Port Scan (Top Ports)

```bash
nmap -Pn 192.168.1.1
```

This scans common ports of your router or local device.

![Network Vulnerability Scanner - Step 0](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/NetworkVulnScanner/screenshots/step0.png)

---

### Step 2: Service and Version Detection

```bash
nmap -sV --host-timeout 30s -Pn 192.168.1.1
```

If service detection times out, note that in results.

![Network Scan Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/NetworkVulnScanner/screenshots/step1.png)

---

### Step 3: OS Fingerprinting (Optional)

```bash
sudo nmap -O -Pn 192.168.1.1
```

Attempts to detect the operating system of the device.

![Vulnerability Report](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/NetworkVulnScanner/screenshots/step3.png)

---
---

## Notes

- In real-world assessments, you'd also run:
  - `nmap --script vuln` for known vulnerabilities (safe scripts)
  - `nmap -sC` for default scripts
- Consider exporting results to XML or HTML using `-oX` or `-oN`
