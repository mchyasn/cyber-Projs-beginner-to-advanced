import psutil
import time

# Define a whitelist of expected process names
KNOWN_PROCESSES = {
    "systemd", "bash", "sshd", "python3", "zsh", "firefox", "chrome", "Xorg"
}

def detect_unusual_processes():
    print("[*] Scanning for unusual activity...\n")
    found_unusual = False

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            name = proc.info['name']
            if name not in KNOWN_PROCESSES:
                print(f"[!] Unusual process detected: {name} (PID: {proc.info['pid']}, User: {proc.info['username']})")
                found_unusual = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if not found_unusual:
        print("[+] No unusual processes found.")

if __name__ == "__main__":
    detect_unusual_processes()
