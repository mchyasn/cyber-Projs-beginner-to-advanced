# Detect Kernel Backdoors in Systems

This project focuses on detecting possible kernel-level backdoors and rootkits using Linux-based tools in a virtual lab environment (Kali Linux). Tools like `chkrootkit` and `rkhunter` were used to scan the system for known rootkits, suspicious files, and system anomalies.

## Tools Used

- `chkrootkit`: Lightweight rootkit scanner
- `rkhunter`: Rootkit Hunter with extensive known rootkit DB
- `less`, `dmesg`, `lsmod`: Manual inspection helpers
- Kali Linux (2025)

## Steps Taken

1. Installed `chkrootkit` and `rkhunter` via apt
2. Ran `chkrootkit`, result:
   - Most entries returned "not infected" or "not found"
   - One generic warning under "suspicious files and dirs"

3. Ran `rkhunter`, result:
   - No warnings, no suspicious files
   - Summary reported clean system:
     - Files checked: OK
     - Applications: OK
     - Rootkits detected: 0

4. Logged outputs in `logs/`
5. Documented results in `notes/detection_summary.txt`

## Outcome

No evidence of kernel-level backdoors or rootkits were detected using these tools. While no current threats were found, manual inspection and custom kernel analysis may be used in future work.

