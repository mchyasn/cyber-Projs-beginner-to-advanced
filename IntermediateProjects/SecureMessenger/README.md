# SecureMessenger – Encrypted Messaging App (CLI-based)

SecureMessenger is a terminal-based, encrypted messaging app built in Python. It simulates secure chat between two users over a LAN or localhost using AES-256 encryption via the cryptography library. This project is designed for educational, offline lab use.

-------------------------------------------------------------------------------

Features:
- End-to-end encryption using AES-256 (Fernet)
- CLI-based chat system (no GUI)
- Simulated client-server setup using TCP sockets
- Real-time encrypted communication
- Ideal for labs, screenshots, and cybersecurity training


Setup:
1. Create virtual environment and activate it:
```
    python3 -m venv venv
    source venv/bin/activate
```
2. Install dependencies:
```
    pip install -r requirements.txt
```
requirements.txt:
```
    cryptography
```
![Secure Chat Interface](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/SecureMessenger/screenshots/1.png)

How It Works:
```
- When the server starts, it generates an AES key and saves it to key.key
- The client loads that same key to encrypt and decrypt messages
- Messages are sent over a TCP socket connection

```
Usage:
1. Start the Server
```
    python server.py
```
2. Start the Client (in a new terminal)
```
    python client.py
```
![Secure Chat Interface](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/SecureMessenger/screenshots/2.png)

Encryption Logic:
```
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
cipher = f.encrypt("hello".encode())

Only the key holder can decrypt:

f.decrypt(cipher).decode()
```

Educational Value:
- Practice symmetric encryption
- Simulate secure communication between two parties
- Great lab demo for red/blue team training
- Extendable with file transfers, GUI, authentication, and TLS

-------------------------------------------------------------------------------

Notes:
- This is not a production-ready messaging app
- For real-world use, implement TLS and secure key exchange (Diffie-Hellman)
"""

txt_path = "/mnt/data/SecureMessenger_README.txt"
with open(txt_path, "w") as f:
    f.write(secure_messenger_readme_txt)

txt_path
