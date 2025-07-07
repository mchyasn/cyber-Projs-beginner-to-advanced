from tools import subdomain_scanner, port_scanner, dir_bruteforce

def main():
    print("[1] Subdomain Scanner")
    print("[2] Port Scanner")
    print("[3] Directory Bruteforce")
    choice = input("Choose tool: ")

    if choice == "1":
        target = input("Enter domain: ")
        subdomain_scanner.run(target)
    elif choice == "2":
        target = input("Enter IP: ")
        port_scanner.run(target)
    elif choice == "3":
        target = input("Enter URL: ")
        dir_bruteforce.run(target)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
