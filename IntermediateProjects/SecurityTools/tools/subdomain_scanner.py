import dns.resolver

def run(domain):
    print(f"[*] Scanning subdomains for {domain}")
    try:
        with open("tools/subdomains.txt") as file:
            for sub in file:
                sub = sub.strip()
                url = f"{sub}.{domain}"
                try:
                    dns.resolver.resolve(url, "A")
                    print(f"[+] Found: {url}")
                except:
                    pass
    except FileNotFoundError:
        print("Missing subdomains.txt")
