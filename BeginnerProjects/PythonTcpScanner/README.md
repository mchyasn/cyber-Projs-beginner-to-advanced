#                                                                         TCP Port Scanner (Basic)

## Description

This Python script scans TCP ports 1–1024 of a target IP address or domain and displays whether each port is open or closed. It uses only Python's built-in `socket` and `datetime` modules.

## Features

- Scans ports 1–1024
- Detects open and closed TCP ports
- Lightweight and fast
- Requires no external libraries

## Usage

### Step 0: Set Up Project Folder

```bash

mkdir PythonTcpScanner
cd PythonTcpScanner
python3 -m venv venv
source venv/bin/activate

```

Step 1: No External Libraries Required

This project uses only built-in modules. Run the following to confirm:

pip list

You should see only the default packages like pip and setuptools.

![Step 0](\BeginnerProjects/)


Step 2: Create the Script

Create a file:
```bash
nano tcp_port_scanner.py
```
Paste the following code:

![Step 1 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/b5b4df744cc42bfa655c216f4f6d0c5cda3dff80/PythonTcpScanner/screenshots/step1.png)

python

```bash

import socket
from datetime import datetime
import sys

def scan_ports(target):
    print(f"[*] Scanning target: {target}")
    print("[*] Scanning ports 1–1024...\n")
    start_time = datetime.now()

    try:
        for port in range(1, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN]  Port {port}")
            else:
                print(f"[CLOSED] Port {port}")
            s.close()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("[-] Could not connect to server.")
        sys.exit()

    duration = datetime.now() - start_time
    print(f"\n[✓] Scan completed in {duration}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tcp_port_scanner.py <target_ip_or_hostname>")
        sys.exit()

    scan_ports(sys.argv[1])

```

Step 3: Run the Tool

python3 tcp_port_scanner.py scanme.nmap.org
Example output:

![Step 2](\BeginnerProjects/)


### [*] Scanning target: scanme.nmap.org.

### [*] Scanning ports 1–1024...

[OPEN]  Port 22.
[CLOSED] Port 23.
...

[✓] Scan completed in 0:00:09.350000

Notes
Port 22 (SSH) is often open on Linux servers.

Always scan only authorized targets (e.g. scanme.nmap.org, 127.0.0.1).

This scanner uses no parallelism; performance is fine for 1–1024 ports.
