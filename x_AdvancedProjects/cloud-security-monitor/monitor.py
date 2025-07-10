import time

LOG_FILE = "/var/log/audit/audit.log"
ALERT_FILE = "alerts/alert.log"

def monitor():
    print("[*] Monitoring audit log...")
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            if "type=EXECVE" in line:
                print(f"[!] Alert: EXECVE detected\n{line}")
                with open(ALERT_FILE, "a") as alert:
                    alert.write(f"[EXECVE ALERT] {line}")

if __name__ == "__main__":
    monitor()
