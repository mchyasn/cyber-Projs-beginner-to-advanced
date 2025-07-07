# Rootkit Detection and Removal Lab

This project simulates a rootkit-like attack on a Linux system, demonstrating how to detect and remove hidden files, users, and binaries using Linux tools and forensic techniques.

## Objective
```
- Simulate rootkit behavior (safely)
- Detect hidden binaries and root-level users
- Remove and clean the system manually and with tools
- Document everything with screenshots
```
## Tools Used
```
- chkrootkit
- rkhunter
- Manual inspection (ls, grep, cat, ps)
```

## Setup Steps

### 1. Simulate Rootkit

```bash
chmod +x simulate_rootkit.sh
./simulate_rootkit.sh
```
![Rootkit Detection Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/RootkitLab/screenshots/1.png)
Creates:
```
Hidden binary: /usr/bin/.hidden_binary

Hidden shell: /usr/bin/.bash_hidden

Root-level user: ghostuser
```
![Rootkit Detection Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/RootkitLab/screenshots/nano.png)
2. Run Detection Tools
```
sudo apt install chkrootkit rkhunter unhide -y
sudo chkrootkit
sudo rkhunter --update
sudo rkhunter --check --skip-keypress --nocolors
```
![Rootkit Detection Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/RootkitLab/screenshots/2.png)
Manual checks:
```
ls -la /usr/bin/ | grep '\.'
cat /etc/passwd | grep '0:'
ps aux | grep bash
```
![Rootkit Detection Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/RootkitLab/screenshots/4.png)

Save all terminal output to detect_rootkit.txt.

3. Clean Up
```
chmod +x remove_rootkit.sh
./remove_rootkit.sh
Removes the hidden files and ghost user.

```
![Rootkit Detection Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/RootkitLab/screenshots/3.png)
