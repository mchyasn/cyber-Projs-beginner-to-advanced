WHOIS & DNS Info Tool
=====================

Description
-----------
A simple Python-based command-line tool that performs WHOIS lookups and DNS record retrieval (A, MX, NS) for any domain using public libraries.

Features
--------
- WHOIS info retrieval
- DNS record queries (A, MX, NS)
- Clear CLI output with exception handling

How to Use
----------

Step 0: Setup Project Folder
----------------------------
mkdir PythonWhoisDnsTool  
cd PythonWhoisDnsTool  
python3 -m venv venv  
source venv/bin/activate  

Step 1: Install Required Libraries
----------------------------------
pip install python-whois dnspython

![WHOIS DNS Lookup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonWhoisDnsTool/screenshots/step0.png)

Step 2: Create the Script
-------------------------
Create a file `whois_dns_tool.py` and paste the following:

![WHOIS DNS Lookup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonWhoisDnsTool/screenshots/step1.png)
```
import whois  
import dns.resolver  
  
def get_whois_info(domain):  
    print("\n[WHOIS Info]")  
    try:  
        w = whois.whois(domain)  
        print(w)  
    except Exception as e:  
        print(f"Error fetching WHOIS: {e}")  
  
def get_dns_info(domain):  
    print("\n[DNS Info]")  
    record_types = ['A', 'MX', 'NS']  
    for record in record_types:  
        try:  
            answers = dns.resolver.resolve(domain, record)  
            print(f"\n{record} Records:")  
            for rdata in answers:  
                print(rdata.to_text())  
        except Exception as e:  
            print(f"Failed to retrieve {record} records: {e}")  
  
if __name__ == "__main__":  
    domain = input("Enter domain: ")  
    get_whois_info(domain)  
    get_dns_info(domain)  
```

Step 3: Run the Tool
--------------------
python3 whois_dns_tool.py

Example Output
--------------
Enter domain: example.com

[WHOIS Info]  
Domain Name: EXAMPLE.COM  
Registrar: RESERVED-EXAMPLE  
...  

[DNS Info]  

A Records:  
93.184.216.34  

MX Records:  
10 smtp.google.com.  

NS Records:  
ns1.google.com.  
ns2.google.com.  
...
![WHOIS DNS Lookup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonWhoisDnsTool/screenshots/step2.png)

Requirements
------------
- Python 3.x  
- python-whois  
- dnspython  

Tested On
---------
- Kali Linux 2024  
- Python 3.13  
- Virtual environment (venv)  

License
-------
MIT – Free to use, share, or modify.
