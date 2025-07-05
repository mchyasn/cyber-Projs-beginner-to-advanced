# Basic Network Sniffer with Scapy

## Description

This Python script captures and displays live network packets using Scapy. It shows source and destination IPs, protocols (TCP, UDP, ICMP), and ports in real time.

## Features

- Real-time packet sniffing
- Displays TCP, UDP, and ICMP traffic
- Lightweight and pure Python
- Great for beginners to learn about network layers

## Usage

### Step 0: Set Up Project Folder
```
mkdir PythonSnifferTool
cd PythonSnifferTool
python3 -m venv venv
source venv/bin/activate
```
shell

### Step 1: Install Requirements
```
pip install scapy
```
![Step 0 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/PythonSnifferTool/screenshots/step0.png)

### Step 2: Create the Sniffer Script

Create a file:
```
nano sniffer.py
```
python

Paste the code:

![Step 1 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/PythonSnifferTool/screenshots/step1.png)


```python

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        if TCP in packet:
            l4 = packet[TCP]
            print(f"[TCP] {src}:{l4.sport} → {dst}:{l4.dport}")
        elif UDP in packet:
            l4 = packet[UDP]
            print(f"[UDP] {src}:{l4.sport} → {dst}:{l4.dport}")
        elif ICMP in packet:
            print(f"[ICMP] {src} → {dst}")
        else:
            print(f"[IP] {src} → {dst} (Proto {proto})")

if __name__ == "__main__":
    print("[*] Starting packet capture... Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)
```

Step 3: Run the Script (Requires Root)
nginx
```
sudo python3 sniffer.py
```
You will see output like:

![Step 3](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/PythonSnifferTool/screenshots/step3.png)


[TCP] 192.168.1.2:443 → 192.168.1.5:49832
[UDP] 192.168.1.5:546 → 192.168.1.1:547
[ICMP] 8.8.8.8 → 192.168.1.5


Notes
You must run the sniffer with sudo due to raw socket permissions.

Works best on your actual network or VM with bridged adapter.
