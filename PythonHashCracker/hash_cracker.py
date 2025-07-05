import hashlib
import sys
import os

def crack_hash(hash_to_crack, wordlist_path, hash_type='md5'):
    if not os.path.exists(wordlist_path):
        print("[-] Wordlist file not found.")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for word in f:
                word = word.strip()
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("[-] Unsupported hash type.")
                    return

                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in wordlist.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 hash_cracker.py <hash> <wordlist.txt> <md5|sha1|sha256>")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist = sys.argv[2]
    hash_type = sys.argv[3]

    crack_hash(target_hash, wordlist, hash_type)
