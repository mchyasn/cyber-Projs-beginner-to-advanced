# CryptoWallet – Secure Cryptocurrency Wallet (CLI)

A lightweight, educational Python-based crypto wallet that supports secure key generation, encryption, decryption, and ECDSA signing. Built to demonstrate the security fundamentals of blockchain wallets.
```
Features

- Generate ECDSA private/public keys
- Derive Bitcoin-style wallet address (Base58 + checksum)
- Encrypt private key using AES with password-based KDF
- Decrypt and load the encrypted key securely
- Sign messages or dummy transactions using ECDSA
```
1. Clone the project

    git clone https://github.com/YOUR_USERNAME/CryptoWallet.git
    cd CryptoWallet

2. Create a virtual environment

    python3 -m venv venv
    source venv/bin/activate

3. Install required packages
```
    pip install -r requirements.txt
```
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/0.png)

Generate Wallet Keys
```
    python wallet/generate_keys.py
```
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/1.png)

Encrypt Private Key
```
    python wallet/encrypt_keys.py
```
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/2.png)

Decrypt Private Key
```
    python wallet/decrypt_keys.py
```
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/3.png)

Sign a Message
```
    python wallet/sign_transaction.py
```
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/4.png)
![Crypto Wallet Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/CryptoWallet/screenshots/44.png)
```
Security Notes

- AES encryption using CFB mode and PBKDF2-HMAC-SHA256.
- This is an educational wallet, not for real-world crypto.

License

Educational use only. No warranties.
