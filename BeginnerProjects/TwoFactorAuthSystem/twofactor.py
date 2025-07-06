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
