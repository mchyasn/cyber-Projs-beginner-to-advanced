# verify-access.py

TRUSTED_USERS = {"alice", "bob", "carol"}
TRUSTED_DEVICES = {"laptop-01", "laptop-02"}
TRUSTED_IPS = {"192.168.1.10", "10.0.0.5"}

def verify_access(user, device, ip):
    if user not in TRUSTED_USERS:
        return "Access Denied: Unrecognized user."
    if device not in TRUSTED_DEVICES:
        return "Access Denied: Untrusted device."
    if ip not in TRUSTED_IPS:
        return "Access Denied: IP not in trusted list."
    return "Access Granted."

if __name__ == "__main__":
    print("=== Zero Trust Access Check ===")
    user = input("Enter username: ")
    device = input("Enter device name: ")
    ip = input("Enter IP address: ")

    result = verify_access(user, device, ip)
    print(result)
