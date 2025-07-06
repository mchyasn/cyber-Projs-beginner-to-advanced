# Basic Antivirus Scanner (Signature-Based)

This project simulates how traditional antivirus software works by scanning files for known malware signatures.

## Objective

Learn how signature-based detection works by building a simple antivirus scanner that searches files for suspicious patterns.

## Step 0: Setup

Create a new project folder and set up a virtual environment:

```bash
mkdir PythonAntivirusSimulator
cd PythonAntivirusSimulator
python3 -m venv venv
source venv/bin/activate
```
Step 1: Create Signature Database
Create a file signatures.txt and add the following malware signatures:
```
malicious.exe
evil_payload
rm -rf /
powershell -nop -w hidden
```
![Antivirus Scan Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonAntivirusSimulator/screenshots/2025-07-05_20-08.png)

Step 2: Create Sample Files
Generate some test files to simulate clean and infected files:
```
echo "This is a clean file" > clean.txt
echo "rm -rf /" > malware1.txt
echo "Just a normal script" > script.py
echo "powershell -nop -w hidden" > malware2.txt
```
![Virus Detection Alert](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonAntivirusSimulator/screenshots/2025-07-05_20-10.png)

Step 3: Create Scanner Script
Create a file scanner.py and paste the following code:

import os
```
def load_signatures(signature_file):
    with open(signature_file, 'r') as f:
        return [line.strip() for line in f]

def scan_file(file_path, signatures):
    try:
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read()
            for sig in signatures:
                if sig in content:
                    return True, sig
    except Exception as e:
        return False, f"Error: {e}"
    return False, None

def scan_directory(directory, signature_file):
    signatures = load_signatures(signature_file)
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            infected, info = scan_file(path, signatures)
            if infected:
                print(f"[!!] Malware Detected: {path} | Signature: {info}")
            else:
                print(f"[OK] Clean: {path}")

if __name__ == "__main__":
    scan_directory(".", "signatures.txt")
```
![Antivirus Quarantine](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonAntivirusSimulator/screenshots/2025-07-05_20-11.png)

Step 4: Run the Scanner
Execute the script:
```
python3 scanner.py
```

You’ll see output indicating which files were flagged and which were clean.

Example Output
```
[!!] Malware Detected: ./malware1.txt | Signature: rm -rf /
[!!] Malware Detected: ./malware2.txt | Signature: powershell -nop -w hidden
[OK] Clean: ./clean.txt
[OK] Clean: ./script.py
```
![Antivirus Scan Complete](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonAntivirusSimulator/screenshots/2025-07-05_20-12.png)
![Antivirus Threat Report](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PythonAntivirusSimulator/screenshots/2025-07-05_20-15.png)

This basic antivirus simulator teaches how malware detection engines look for known patterns in files. It's a simplified but effective way to understand the foundation of signature-based security tools.
"""
