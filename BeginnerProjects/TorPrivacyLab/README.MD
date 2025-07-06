# Tor + ProxyChains Anonymous Routing Lab
=======================================

Goal:
-----
Learn how to route terminal-based tools through the Tor network using ProxyChains
to simulate anonymous activity and protect identity during security research.

Tools Used:
```
- Tor (SOCKS5 proxy on port 9050)
- ProxyChains4 (configurable CLI traffic router)
- curl, wget, nmap (used through Tor)
- Kali Linux
```
Step-by-Step Guide:
-------------------

1. Install Tor
```
sudo apt update
sudo apt install tor -y
```
![Tor Network Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TorPrivacyLab/screenshots/1.png)

2. Start and Enable Tor
-----------------------
```
sudo systemctl start tor
sudo systemctl enable tor
```
3. Check if Tor is Running
--------------------------
sudo systemctl status tor

Expected output: "Active: active (running)"
![Tor Connection Established](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TorPrivacyLab/screenshots/2.png)

4. Install ProxyChains
----------------------
sudo apt install proxychains4 -y

5. Configure ProxyChains to Use Tor
-----------------------------------
sudo nano /etc/proxychains4.conf

Edit the bottom section to:
[ProxyList]
socks5  127.0.0.1 9050
![Tor Privacy Verification](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TorPrivacyLab/screenshots/5.png)

Uncomment this line near the top to avoid DNS leaks:
proxy_dns

Save and exit (Ctrl+X, Y, Enter)

6. Test Anonymous Requests via Tor
----------------------------------

a) curl through Tor:
proxychains curl https://check.torproject.org

Expected: HTML saying "Congratulations. This browser is configured to use Tor."

![Tor Network Test](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TorPrivacyLab/screenshots/3.png)

b) wget through Tor:
proxychains wget https://example.com


c) nmap through Tor:
proxychains nmap -sT -Pn scanme.nmap.org

(Note: Only TCP connect scans like -sT work over SOCKS5)

7. Optional: Test DNS Leak Protection
-------------------------------------
If "proxy_dns" is enabled, DNS requests will be routed through Tor.

![Tor Anonymity Check](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/TorPrivacyLab/screenshots/4.png)
Security Notes:
---------------
- Never rely on Tor alone for OPSEC. Metadata leaks are still possible.
- For stronger anonymity, use live systems like Tails or Whonix.
- Avoid logging into real identities or using personal accounts over Tor.

Date: July 6, 2025
