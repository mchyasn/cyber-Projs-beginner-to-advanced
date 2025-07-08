# Cloud Security Monitoring Project

This project simulates a cloud-like environment and builds a local security monitoring system using `auditd` on Kali Linux. It monitors and alerts on system events such as command executions and potential privilege abuse, mimicking basic functionality of cloud security systems like AWS GuardDuty.

## Objective

To demonstrate how Linux audit tools and custom scripts can be used to detect suspicious activities in a local or simulated cloud system.

## Tools Used

- Kali Linux (host)
- `auditd` for auditing kernel events
- Python script (`monitor.py`) for log monitoring
- Linux audit rules for capturing command execution

## Steps

1. **Install auditd**
   ```bash
   sudo apt update
   sudo apt install auditd
   ```

2. **Start auditd and verify**
   ```bash
   sudo service auditd start
   sudo auditctl -s
   ```

3. **Add audit rules**
   ```bash
   sudo nano /etc/audit/rules.d/cloud.rules
   ```

   Paste the following rule to monitor all command executions:
   ```
   -a always,exit -F arch=b64 -S execve -k exec_log
   ```

   Then load the rule:
   ```bash
   sudo augenrules --load
   sudo auditctl -l
   ```

4. **Create and run the monitor script**

   Create `monitor.py`:
   ```python
   import time
   import os

   LOG_FILE = "/var/log/audit/audit.log"
   ALERT_FILE = "alerts/alert.log"

   def monitor():
       print("[*] Monitoring audit log for EXECVE events...")
       os.makedirs("alerts", exist_ok=True)
       with open(LOG_FILE, "r") as f:
           f.seek(0, os.SEEK_END)
           while True:
               line = f.readline()
               if not line:
                   time.sleep(0.5)
                   continue
               if "type=EXECVE" in line:
                   print(f"[!] Alert: EXECVE detected")
                   with open(ALERT_FILE, "a") as alert_file:
                       alert_file.write(f"[EXECVE ALERT] {line}")

   if __name__ == "__main__":
       monitor()
   ```

   Run the script:
   ```bash
   sudo python3 monitor.py
   ```

5. **Trigger an alert**

   In another terminal:
   ```bash
   sudo ls /root
   ```

   You should see an alert printed by `monitor.py`.

## Disclaimer

This project is for educational purposes only and was run in a safe, local Kali Linux environment. Do not use this setup for monitoring systems without authorization.

## Author

Developed by [mchyasn](https://github.com/mchyasn)
