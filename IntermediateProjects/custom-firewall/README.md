# Create a Custom Firewall on Kali Linux

This project demonstrates how to build and test a simple custom firewall using `iptables` on Kali Linux. It includes a firewall rule set, testing with `nmap`, and documentation using screenshots.

## Features

- Flush and reset iptables
- Set default DROP policy for input/forward chains
- Allow localhost and loopback
- Allow established/related connections
- Allow SSH (port 22), HTTP (port 80), and HTTPS (port 443)
- Log dropped packets

## Setup Instructions

1. Clone or create the folder locally on Kali Linux.
2. Place the `firewall-setup.sh` and `firewall-reset.sh` scripts in the root of the project directory.
3. Give executable permissions:

   ```bash
   chmod +x firewall-setup.sh firewall-reset.sh
   ```

4. Run the firewall script:

   ```bash
   sudo ./firewall-setup.sh
   ```

5. (Optional) Run the reset script to flush rules:

   ```bash
   sudo ./firewall-reset.sh
   ```

## Testing

Use the provided `nmap-scan.sh` script or manual scans to test rule effectiveness.

Example:

```bash
nmap -sS -p 22,80,443,21,23 127.0.0.1
```

Expected:
- Ports 22, 80, 443: open (if services are running)
- Ports 21, 23: closed or filtered

## Screenshots

![Custom Firewall Configuration](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/custom-firewall/screenshots/0.png)

### Allowed Traffic (e.g. port 22) ### Blocked Traffic (e.g. port 21)

![Custom Firewall Configuration](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/custom-firewall/screenshots/1.png)

