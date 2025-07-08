#!/bin/bash

echo "=== Zero Trust Device Health Check ==="

# Simulate antivirus check
AV_PROCESS="clamd"
if pgrep "$AV_PROCESS" > /dev/null; then
    echo "[+] Antivirus service ($AV_PROCESS) is running."
else
    echo "[-] Antivirus service ($AV_PROCESS) not found."
fi

# Simulate update check
if [ -f /var/lib/apt/periodic/update-success-stamp ]; then
    LAST_UPDATE=$(stat -c %y /var/lib/apt/periodic/update-success-stamp | cut -d' ' -f1)
    echo "[+] Last system update was on $LAST_UPDATE"
else
    echo "[-] System update status unknown."
fi

# Simulate suspicious process check
SUSPICIOUS="nc"
if pgrep "$SUSPICIOUS" > /dev/null; then
    echo "[-] Suspicious process detected: $SUSPICIOUS"
else
    echo "[+] No suspicious processes found."
fi
