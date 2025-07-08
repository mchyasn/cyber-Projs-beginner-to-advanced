#!/bin/bash
echo "[*] Loaded Kernel Modules:"
lsmod | head -n 10

echo -e "\n[*] Recent Kernel Messages (filtered):"
dmesg | tail -n 20 | grep -iE "error|root|fail"

echo -e "\n[*] Suspicious /proc entries:"
ls -la /proc | grep "\.\."

echo -e "\n[*] Hidden network listeners:"
netstat -tulnp | grep -v "127.0.0.1"
