import socket
from crypto_utils import *

key = load_key()

client = socket.socket()
client.connect(('127.0.0.1', 9999))
print("[*] Connected to server")

while True:
    msg = input("You: ")
    client.send(encrypt_message(msg, key))

    reply = client.recv(4096)
    try:
        print(f"[Server] {decrypt_message(reply, key)}")
    except Exception as e:
        print("[!] Decryption failed:", e)
