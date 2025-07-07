import socket

def run(ip):
    print(f"[*] Scanning ports on {ip}")
    for port in range(20, 1025):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            print(f"[+] Port {port} open")
            sock.close()
        except:
            pass
