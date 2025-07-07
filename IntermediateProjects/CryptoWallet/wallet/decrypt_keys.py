import os
import json
import base64
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

def decrypt_private_key(data: dict, password: str) -> str:
    salt = base64.b64decode(data['salt'])
    iv = base64.b64decode(data['iv'])
    ciphertext = base64.b64decode(data['ciphertext'])

    key = derive_key(password, salt)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted.decode()

if __name__ == "__main__":
    # Load encrypted file
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(project_root, "keys", "encrypted_key.json")

    try:
        with open(file_path, 'r') as f:
            encrypted_data = json.load(f)
    except Exception as e:
        print(f"❌ Failed to load encrypted file: {e}")
        exit()

    password = input("Enter password to decrypt: ")

    try:
        private_key = decrypt_private_key(encrypted_data, password)
        print(f"\n🔓 Decrypted Private Key:\n{private_key}")
    except Exception as e:
        print(f"\n❌ Failed to decrypt: {e}")
