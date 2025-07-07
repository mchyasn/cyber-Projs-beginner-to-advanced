# SecurityTools

A command-line toolkit of basic security testing tools written in Python.  
Built for labs, ethical hacking, and educational purposes.

## Features

- Subdomain Scanner (DNS resolution)
- TCP Port Scanner
- Directory Bruteforcer (HTTP)
- Modular design — easily extendable

## Folder Structure

SecurityTools/
├── main.py
├── requirements.txt
├── findings.md
├── README.md
├── screenshots/
├── reports/
├── tools/
│ ├── init.py
│ ├── subdomain_scanner.py
│ ├── port_scanner.py
│ └── dir_bruteforce.py

bash
Copy
Edit

## Setup

```bash
# Clone repo and enter directory
git clone https://github.com/mchyasn/SecurityTools.git
cd SecurityTools

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
Usage
bash
Copy
Edit
python main.py
You will be prompted to choose a tool:

csharp
Copy
Edit
[1] Subdomain Scanner
[2] Port Scanner
[3] Directory Bruteforce
Choose tool:
Enter the target information when prompted.

Example Inputs:
Domain for subdomain scanner: example.com

IP for port scanner: 127.0.0.1

URL for dir brute: http://testphp.vulnweb.com

Wordlists
Edit or extend the wordlists used by the tools:

tools/subdomains.txt

tools/wordlist.txt

Sample Outputs
Subdomain Scanner
less
Copy
Edit
[*] Scanning subdomains for example.com
[+] Found: www.example.com
[+] Found: mail.example.com
Port Scanner
css
Copy
Edit
[*] Scanning ports on 127.0.0.1
[+] Port 22 open
[+] Port 80 open
Directory Bruteforcer
less
Copy
Edit
[*] Brute-forcing directories on http://testphp.vulnweb.com
[+] Found: http://testphp.vulnweb.com/admin (403)
[+] Found: http://testphp.vulnweb.com/uploads (200)
