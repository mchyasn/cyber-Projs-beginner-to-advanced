import requests
from bs4 import BeautifulSoup
import time

# TOR proxy settings
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Example dark web sites (safe research-based .onion pages)
onion_sites = [
    "http://expyuzz4wqqyqhjn.onion"  # Tor Project mirror
]

# Log file
log_file = "scraper.log"

def scrape_site(url):
    print(f"[+] Connecting to: {url}")
    try:
        response = requests.get(url, proxies=proxies, timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title else "No Title"
            print(f"[✓] Title: {title}")
            with open(log_file, "a") as f:
                f.write(f"{url} - {title}\n")
        else:
            print(f"[!] Failed to load: {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"[!] Error scraping {url}: {e}")

def main():
    print("[*] Dark Web Scraper Started")
    with open(log_file, "a") as f:
        f.write(f"\n--- New Scan {time.ctime()} ---\n")
    for url in onion_sites:
        scrape_site(url)
    print("[*] Done.")

if __name__ == "__main__":
    main()
