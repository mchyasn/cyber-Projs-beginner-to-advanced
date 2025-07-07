from pathlib import Path

# Re-define the findings content after code reset
findings_content = """
SecurityTools – Findings
=========================

This document contains summary results from running the built-in tools.

--------------------------------------------------

1. Subdomain Scanner
--------------------
Target: example.com
Wordlist Used: tools/subdomains.txt

Results:
[+] Found: www.example.com
[+] Found: mail.example.com

--------------------------------------------------

2. Port Scanner
---------------
Target: 127.0.0.1
Ports Scanned: 1–1000

Results:
[+] Port 22 open (SSH)
[+] Port 80 open (HTTP)

--------------------------------------------------

3. Directory Bruteforcer
------------------------
Target: http://testphp.vulnweb.com
Wordlist Used: tools/wordlist.txt

Results:
[+] Found: /admin        (403 Forbidden)
[+] Found: /uploads      (200 OK)
[+] Found: /login        (200 OK)

--------------------------------------------------

Notes
-----
- Scans were performed in a controlled lab environment.
- All tools were executed manually using the command line.
- Screenshots of each tool’s output are available in screenshots/.

--------------------------------------------------

Next Steps
----------
- Add HTTP header analyzer
- Add hash cracker
- Extend wordlists
"""
