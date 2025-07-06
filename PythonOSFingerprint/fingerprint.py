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
