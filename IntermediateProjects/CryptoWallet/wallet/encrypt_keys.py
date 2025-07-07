import os
import base64
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_private_key(private_key: str, password: str) -> dict:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(private_key.encode()) + encryptor.finalize()

    return {
        'salt': base64.b64encode(salt).decode(),
        'iv': base64.b64encode(iv).decode(),
        'ciphertext': base64.b64encode(ciphertext).decode()
    }

if __name__ == "__main__":
    private_key = input("Enter private key to encrypt: ")
    password = input("Enter password: ")

    encrypted = encrypt_private_key(private_key, password)

    # Save to absolute path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(project_root, "keys", "encrypted_key.json")

    try:
        with open(output_path, "w") as f:
            json.dump(encrypted, f, indent=4)
        print(f"\n✅ Encrypted key saved to: {output_path}")
    except Exception as e:
        print(f"\n❌ Error saving file: {e}")
