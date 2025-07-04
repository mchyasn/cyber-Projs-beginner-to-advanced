import socket

def scan_port(ip, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

target = input("Enter target IP or domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n[*] Scanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    scan_port(target, port)
