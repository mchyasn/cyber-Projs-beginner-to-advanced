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
