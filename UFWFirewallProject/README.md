
# UFW Firewall Configuration Project

## Description

This beginner project walks through configuring basic firewall rules using `ufw` (Uncomplicated Firewall) on Kali Linux. It covers default policies, allowing safe services, blocking threats, and managing rules.

## Tools Used

- `ufw` – Uncomplicated Firewall (frontend for iptables)

---

## Step-by-Step Instructions

### Step 1: Install and Enable UFW

Install UFW and enable the firewall with default deny policy:

```bash
sudo apt update
sudo apt install ufw -y
sudo ufw status
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
```

![UFW Firewall Configuration](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/UFWFirewallProject/screenshots/Screenshot_2025-07-05_12_33_20.png)
---

### Step 2: Allow Safe Services

Allow specific known services:

```bash
sudo ufw allow 22     # SSH
sudo ufw allow 80     # HTTP
```

![UFW Firewall Rules](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/UFWFirewallProject/screenshots/Screenshot_2025-07-05_12_34_30.png)
---

### Step 3: Block Suspicious IPs or Ports

Block an IP and dangerous service:

```bash
sudo ufw deny from 192.168.1.123
sudo ufw deny 23     # Telnet
```

![UFW Firewall Status](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/UFWFirewallProject/screenshots/Screenshot_2025-07-05_12_35_00.png)
---

### Step 4: View and Delete Rules

Check configured rules and delete if needed:

```bash
sudo ufw status numbered
sudo ufw delete [rule_number]
```
![UFW Firewall Logs](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/UFWFirewallProject/screenshots/Screenshot_2025-07-05_12_35_33.png)---

## Notes

- Always allow SSH before enabling UFW on remote systems.
- Combine with fail2ban for stronger protection.

