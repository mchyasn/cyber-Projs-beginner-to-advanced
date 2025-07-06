
# Wi-Fi Security Audit (Beginner Project)

## Description

This project simulates a basic Wi-Fi security audit on your own home network. It uses built-in Linux tools to check Wi-Fi security levels, detect encryption types, and identify connected devices on the LAN. Designed for ethical use only.

## Tools Used

- `nmcli` – to view available Wi-Fi networks and security protocols
- `arp-scan` – to detect connected devices on the local network
- `iwconfig` – to check Wi-Fi interfaces and modes
- `nmap` – (optional) live host detection

---

## 📶 Step-by-Step

iwconfig

![WiFi Security Audit - Step 0](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/WifiSecurityAudit/sc/step0.png)

### Step 1: List Nearby Wi-Fi Networks

```bash
nmcli dev wifi list
```

Check your router's encryption type (WPA2, WPA3 is good. WEP or OPEN is weak).

![WiFi Security Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/WifiSecurityAudit/sc/step1.png)

---

### Step 2: Scan for Connected Devices

Make sure you're connected to your home Wi-Fi via `wlan0`, then run:

```bash
sudo arp-scan --interface=wlan0 --localnet
```

Shows all connected devices (IP + MAC).

![WiFi Security Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/WifiSecurityAudit/sc/step3.png)

---

### Optional: Scan Network with Nmap

```bash
sudo nmap -sn 192.168.1.0/24
```
![WiFi Audit Report](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/WifiSecurityAudit/sc/step5.png)

Can be used instead of `arp-scan`.

---

---

## Disclaimer

This project is for **educational and ethical use only**. Always ensure you have permission to scan any network you analyze.

---

