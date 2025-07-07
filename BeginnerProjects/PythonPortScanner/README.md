# Basic Python Port Scanner – Cybersecurity Project

This project demonstrates how to build a simple **Port Scanner in Python** for internal network testing and reconnaissance.

**⚠️ Educational Use Only – Never scan networks without permission.**

---

## Step 1: Create Your Python Script

![Port Scanner Initialization](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonPortScanner/screenshots/step0.png)

Save the following code as `port_scanner.py`:

```python
import socket

target = input("Enter the IP to scan: ")
ports = [21, 22, 23, 25, 53, 80, 135, 139, 443, 445, 8080]

print(f"Scanning {target} for open ports:")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()
```

![Port Scanner Initialization](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonPortScanner/screenshots/step1.png)

---

## Step 2: 
```
Run the Scanner

Make sure you are connected to a test network (e.g. using VMs or isolated lab).

Run the scanner using:


python3 port_scanner.py
```

Enter a target IP such as `192.168.1.1` or another local IP.

![Port Scan Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonPortScanner/screenshots/step2.png)

## Step 3: Interpret Results

The output will list open ports based on the predefined list. This is useful for:

- Identifying exposed services
- Mapping internal systems
- Practicing basic scanning logic
---

## Notes

- You can expand the list of ports to include full ranges (e.g., 1–1024).
- Always get permission before scanning.
- Works on Linux, macOS, or Windows with Python 3.

---

