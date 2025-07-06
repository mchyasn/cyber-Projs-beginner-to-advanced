# DNS Spoofing Detection with tcpdump

This project demonstrates how to detect potential DNS spoofing activity using basic tools like `tcpdump` and `nslookup` on Kali Linux.

## Objective
Observe suspicious or altered DNS responses that may indicate spoofing on the network.

## Step 1: Setup

Make sure you're connected to a network and have internet access. Confirm your active interface:

```bash
ip a
```

Identify the correct interface (e.g., `eth0` or `wlan0`).

## Step 2: Start DNS Packet Capture

Run tcpdump to monitor DNS traffic (UDP port 53) on your active interface:

```bash
sudo tcpdump -i eth0 port 53 -n
```

This will start capturing all DNS request/response packets on your interface.

![DNS Spoofing Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/DetectDNSSpoofing/screenshots/2025-07-05_19-56.png)

## Step 3: Trigger DNS Requests

In a second terminal window, manually trigger DNS lookups:

```bash
nslookup github.com
nslookup kali.org
nslookup google.com
```

You should see matching packets appear in the tcpdump terminal.

If you see inconsistent IPs for the same domain (e.g., github.com resolving to different IPs), it may suggest spoofing or DNS manipulation.

![DNS Spoofing Alert](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/DetectDNSSpoofing/screenshots/2025-07-05_19-57.png)

## Step 4: Save the Capture (Optional)

If you want to analyze in Wireshark later:

```bash
sudo tcpdump -i eth0 port 53 -n -w dns_spoof_test.pcap
```

Then trigger your lookups again. Open the pcap file in Wireshark and filter with:

```
dns
```

## Summary

This project helps you visually monitor DNS behavior and understand how DNS spoofing could be detected through inconsistent responses or unexpected changes in IP address mappings.
