# Two-Factor Authentication System (Python)

## Description

This project demonstrates a simple command-line two-factor authentication (2FA) system using:

- Username and password (1st factor)
- TOTP via Google Authenticator (2nd factor)

It uses the `pyotp` and `qrcode` libraries to simulate a secure login flow with QR-based setup.

---

## Step-by-Step Instructions

Step 1: Set Up Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install pyotp qrcode[pil]
```
![2FA Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/TwoFactorAuthSystem/screenshots/Screenshot_2025-07-05_12_53_25.png)

Step 2: Create 2FA Python Script
Create a file named twofactor.py with the following:
![2FA Authentication](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/TwoFactorAuthSystem/screenshots/Screenshot%202025-07-05%20095557.png)
```
import pyotp
import qrcode
import getpass

# Setup user credentials
USERNAME = "admin"
PASSWORD = "supersecret"

# Generate TOTP secret
totp = pyotp.TOTP(pyotp.random_base32())
print("[*] Secret:", totp.secret)

# Display QR code
uri = totp.provisioning_uri(name=USERNAME, issuer_name="SecureApp")
qrcode.make(uri).show()

# First Factor: Username + Password
username_input = input("Username: ")
password_input = getpass.getpass("Password: ")

if username_input != USERNAME or password_input != PASSWORD:
    print("❌ Invalid credentials")
    exit()

# Second Factor: TOTP from Authenticator
code = input("Enter 2FA code from Authenticator app: ")

if totp.verify(code):
    print("✅ 2FA success. Access granted.")
else:
    print("❌ Invalid 2FA code. Access denied.")
```
Step 3: Test the Tool
```
python3 twofactor.py
```
Scan the QR code in Google Authenticator.

Enter credentials and the 6-digit code.

![2FA Verification](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/TwoFactorAuthSystem/screenshots/Screenshot%202025-07-05%20095651.png)
![2FA Success](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/TwoFactorAuthSystem/screenshots/Screenshot%202025-07-05%20095943.png)

Notes
This is a demo project, not production-ready.

You can extend it by storing secrets in a database or adding rate limiting.

