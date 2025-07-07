# OS Fingerprinting Tool (TTL-based)

## Description
This Python script attempts to guess a remote host's operating system by sending a ping and analyzing the TTL value in the response. This basic technique can help differentiate between Linux/Unix and Windows systems.

## Features
- Uses TTL value to infer operating system
- Works across platforms (Windows/Linux)
- Requires no special permissions

## How It Works
Operating systems use different default TTL values:
- Windows: 128
- Linux/Unix: 64
- Cisco/Other: 255 (or different)

This tool runs the system's native `ping` command and parses the TTL value.

## Usage

### Step 0: Setup Project Folder

```bash
mkdir PythonOSFingerprint
cd PythonOSFingerprint
python3 -m venv venv
source venv/bin/activate
```

Step 1: Install Required Library

pip install scapy  # Optional (not used in final script)

![OS Fingerprinting Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonOSFingerprint/screenshots/step1.png)

Step 2: Create Script

nano os_fingerprint.py
Paste this code:

python
```bash

import subprocess
import platform
import re
import sys

def extract_ttl(ping_output):
    match = re.search(r"ttl[=|:](\d+)", ping_output, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None

def detect_os(ip):
    print(f"[*] Pinging {ip} ...")

    system = platform.system().lower()
    if "windows" in system:
        cmd = ["ping", "-n", "1", ip]
    else:
        cmd = ["ping", "-c", "1", ip]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)
    except subprocess.CalledProcessError:
        print("[-] Ping failed.")
        return

    ttl = extract_ttl(output)
    if ttl is None:
        print("[-] TTL not found in ping output.")
        return

    print(f"[+] Received TTL: {ttl}")

    if ttl >= 128:
        print("[+] Likely OS: Windows")
    elif 64 <= ttl < 128:
        print("[+] Likely OS: Linux/Unix")
    else:
        print("[?] OS Unknown")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 os_fingerprint.py <target_ip>")
        sys.exit(1)


    detect_os(sys.argv[1])
```
![OS Detection Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonOSFingerprint/screenshots/step2.png)

Step 3: Run the Tool

python3 os_fingerprint.py 8.8.8.8
Example Output

![Operating System Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonOSFingerprint/screenshots/step3.png)

[*] Pinging 8.8.8.8 ...
[+] Received TTL: 128
[+] Likely OS: Windows

Tested On
Kali Linux 2024

Python 3.13

Works without root
