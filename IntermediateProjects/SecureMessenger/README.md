# Generate a clean SQL INSERT statement containing the SecureMessenger README content

secure_messenger_readme_sql = """\
INSERT INTO projects (title, filename, content) VALUES (
    'SecureMessenger – Encrypted Messaging App (CLI-based)',
    'SecureMessenger_README.md',
    "-- SecureMessenger – Encrypted Messaging App (CLI-based)\n\n\
SecureMessenger is a terminal-based, encrypted messaging app built in Python. It simulates secure chat between two users over a LAN or localhost using AES-256 encryption via the cryptography library. This project is designed for educational, offline lab use.\n\n\
-- Features\n\
- End-to-end encryption using AES-256 (Fernet)\n\
- CLI-based chat system (no GUI)\n\
- Simulated client-server setup using TCP sockets\n\
- Real-time encrypted communication\n\
- Ideal for labs, screenshots, and cybersecurity training\n\n\
-- Project Structure\n\
SecureMessenger/\n\
├── client.py           # Secure chat client\n\
├── server.py           # Secure chat server\n\
├── crypto_utils.py     # Handles key generation + encryption/decryption\n\
├── requirements.txt    # Python dependencies\n\
├── README.md           # Documentation\n\
└── screenshots/        # Add your proof/screenshots here\n\n\
-- Setup\n\
1. Install Dependencies:\n\
python3 -m venv venv\n\
source venv/bin/activate\n\
pip install -r requirements.txt\n\n\
-- requirements.txt:\n\
cryptography\n\n\
-- How It Works\n\
- Server generates an AES key and saves to key.key\n\
- Client loads the same key to encrypt and decrypt messages\n\n\
-- Usage\n\
1. Start the Server:\n\
python server.py\n\
2. Start the Client:\n\
python client.py\n\n\
-- Encryption Logic\n\
from cryptography.fernet import Fernet\n\
key = Fernet.generate_key()\n\
f = Fernet(key)\n\
cipher = f.encrypt('hello'.encode())\n\
f.decrypt(cipher).decode()\n\n\
-- Screenshot Suggestions\n\
- Terminal showing key creation\n\
- Encrypted message in server log\n\
- Chat view from both client and server\n\n\
-- Educational Value\n\
- Practice symmetric encryption\n\
- Simulate secure comms for lab training\n\
- Take screenshots for documentation\n\
- Expand with auth or file transfer\n\n\
-- Notes\n\
- Not for production use\n\
- For real apps, use TLS and secure key exchange"
);
"""

# Save as a SQL file
sql_path = "/mnt/data/secure_messenger_insert.sql"
with open(sql_path, "w") as f:
    f.write(secure_messenger_readme_sql)

sql_path
