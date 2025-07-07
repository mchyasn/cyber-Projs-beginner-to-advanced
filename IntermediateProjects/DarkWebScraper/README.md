# Dark Web Scraper for Research (Tor-Based)

This project demonstrates how to build a safe, educational Tor-based web scraper for research and cybersecurity intelligence. It simulates attempts to access `.onion` services via the Tor network and scrape non-sensitive data (such as page titles), while documenting common failure cases experienced in real-world operations.

---

## ⚠️ Legal & Ethical Disclaimer

This project is for **educational purposes only**. It does **not access, store, or share illegal content**. All targets are public `.onion` addresses from known and safe research sources. Use this project responsibly and according to your country's cybersecurity laws.


##  Setup Instructions

### 1. Install Required Tools

```bash
sudo apt update
sudo apt install tor torsocks python3-venv -y
```

### 2. Start Tor Service

```bash
sudo service tor start
```
![Dark Web Monitoring Tool](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/DarkWebScraper/screenshots/0.png)

Verify:

```bash
sudo netstat -tulpen | grep 9050
```

You should see:
```
tcp 127.0.0.1:9050 ... tor
```

### 3. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

##  Run the Scraper

```bash
torsocks python main.py
```

This will attempt to connect to `.onion` URLs via Tor and log the page titles.

##  Troubleshooting

If you see errors like:

```
SOCKSHTTPConnectionPool: Failed to establish a new connection: 0x01: General SOCKS server failure
```

Or:

```
curl: (97) Not resolving .onion address (RFC 7686)
```

These are **normal limitations** in modern Linux systems due to `.onion` DNS blocking (RFC 7686). It demonstrates a real-world research blocker.





##  Notes

- This is a legit cybersecurity project even if `.onion` targets fail.
- Failure to connect is part of **real-world dark web research**, where uptime, anonymity, and DNS resolution are all challenging.

