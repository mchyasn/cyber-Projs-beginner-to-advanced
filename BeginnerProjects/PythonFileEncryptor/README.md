# Python File Encryptor

## Description

This project uses the `cryptography` library to securely encrypt and decrypt files using Fernet symmetric encryption. It's ideal for beginners to practice real-world file protection.

## Features

- Symmetric encryption using Fernet
- Key generation and secure storage
- Encrypt any file type (txt, PDF, images, etc.)
- Decrypt previously encrypted files

## Usage

### Step 0: Set Up Project Folder

```
mkdir PythonFileEncryptor
cd PythonFileEncryptor
python3 -m venv venv
source venv/bin/activate
```

### Step 1: Install Required Library

```
pip install cryptography
```
![Step 0](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonFileEncryptor/screenshots/step0.png)

### Step 2: Create the Script

```
nano file_encryptor.py
```

Paste the following code:
![Step 1](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonFileEncryptor/screenshots/step1.png)
```python
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = fernet.decrypt(data)
    with open(filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 file_encryptor.py [encrypt/decrypt] <filename>")
        exit()

    action = sys.argv[1]
    target_file = sys.argv[2]

    if action == "encrypt":
        generate_key()
        encrypt_file(target_file)
        print(f"[+] Encrypted '{target_file}' to '{target_file}.enc'")
    elif action == "decrypt":
        decrypt_file(target_file)
        print(f"[+] Decrypted '{target_file}' back to original")
    else:
        print("[-] Unknown action")
```

### Step 3: Encrypt/Decrypt a File
![Step 2](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonFileEncryptor/screenshots/step2.png)
```
echo "secret message" > myfile.txt
python3 file_encryptor.py encrypt myfile.txt
python3 file_encryptor.py decrypt myfile.txt.enc
cat myfile.txt
```

