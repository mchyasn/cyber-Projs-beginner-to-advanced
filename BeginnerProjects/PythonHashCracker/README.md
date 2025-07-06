
# Simple Hash-Based Password Cracker

## Description

This Python script attempts to crack a given hashed password by comparing it to hashes of words from a wordlist file. It supports common hashing algorithms such as MD5, SHA1, and SHA256.

## Features

- Supports MD5, SHA1, and SHA256 hashing algorithms
- Accepts custom wordlists
- Pure Python, no external libraries required
- Great for learning how password hashing and brute-force works

## Usage

### Step 0: Set Up Project Folder

```
mkdir PythonHashCracker
cd PythonHashCracker
python3 -m venv venv
source venv/bin/activate
```

### Step 1: No External Libraries Required

This project uses only built-in libraries (`hashlib`, `sys`, `os`). No installation needed.

```
pip list
```
![Step 0 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/82e0b1336581a4b30b46ec85e9d7c9761c59359d/PythonHashCracker/screenshots/step0.png)

### Step 2: Create the Script

Create a file:

```
nano hash_cracker.py
```

Paste this code:

![Step 1 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonHashCracker/screenshots/step1.png)

```python
import hashlib
import sys
import os

def crack_hash(hash_to_crack, wordlist_path, hash_type='md5'):
    if not os.path.exists(wordlist_path):
        print("[-] Wordlist file not found.")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for word in f:
                word = word.strip()
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("[-] Unsupported hash type.")
                    return

                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in wordlist.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hash_cracker.py <hash> <wordlist.txt> <md5|sha1|sha256>")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist = sys.argv[2]
    hash_type = sys.argv[3]

    crack_hash(target_hash, wordlist, hash_type)
```

### Step 3: Create a Wordlist and Run

Create a small test wordlist:

```
echo -e "123456\npassword\nletmein\nadmin\nqwerty" > wordlist.txt
```

Get a hash of the word `admin`:

```
echo -n "admin" | md5sum
# 21232f297a57a5a743894a0e4a801fc3
```

Run the script:

```
python3 hash_cracker.py 21232f297a57a5a743894a0e4a801fc3 wordlist.txt md5
```

Expected Output:

![Step 2 Screenshot](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonHashCracker/screenshots/step2.png)

```
[+] Password found: admin
```

## Notes

- This is a simple wordlist-based cracker.
- For more complex hashes, use advanced tools like `hashcat`.
- Always crack passwords legally and ethically — for CTFs, pentesting labs, or educational purposes only.


