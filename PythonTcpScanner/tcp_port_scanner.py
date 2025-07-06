import socket
from datetime import datetime
import sys

def scan_ports(target):
    print(f"[*] Scanning target: {target}")
    print("[*] Scanning ports 1–1024...\n")
    start_time = datetime.now()

    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN]  Port {port}")
        else:
            print(f"[CLOSED] Port {port}")
        s.close()

    duration = datetime.now() - start_time
    print(f"\n[✓] Scan completed in {duration}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tcp_port_scanner.py <target_ip_or_hostname>")
        sys.exit()

    scan_ports(sys.argv[1])
