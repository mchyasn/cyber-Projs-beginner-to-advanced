import socket
from crypto_utils import *

key = generate_key()
save_key(key)

server = socket.socket()
server.bind(('0.0.0.0', 9999))
server.listen(1)
print("[*] Waiting for connection...")

conn, addr = server.accept()
print(f"[+] Connected with {addr}")

while True:
    data = conn.recv(4096)
    if not data:
        break
    try:
        message = decrypt_message(data, key)
        print(f"[Client] {message}")
    except Exception as e:
        print("[!] Error decrypting:", e)

    reply = input("You: ")
    conn.send(encrypt_message(reply, key))

conn.close()
