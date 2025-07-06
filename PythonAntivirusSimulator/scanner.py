import os

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
