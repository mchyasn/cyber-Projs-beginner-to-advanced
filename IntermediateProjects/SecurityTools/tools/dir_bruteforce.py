import requests

def run(url):
    print(f"[*] Brute-forcing directories on {url}")
    try:
        with open("tools/wordlist.txt") as file:
            for line in file:
                line = line.strip()
                full_url = f"{url}/{line}"
                r = requests.get(full_url)
                if r.status_code != 404:
                    print(f"[+] Found: {full_url} ({r.status_code})")
    except FileNotFoundError:
        print("Missing wordlist.txt")
