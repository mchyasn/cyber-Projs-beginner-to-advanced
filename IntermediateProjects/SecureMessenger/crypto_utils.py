from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def load_key(path="key.key"):
    with open(path, "rb") as f:
        return f.read()

def save_key(key, path="key.key"):
    with open(path, "wb") as f:
        f.write(key)

def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(ciphertext, key):
    f = Fernet(key)
    return f.decrypt(ciphertext).decode()
