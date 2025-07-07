from ecdsa import SigningKey, SECP256k1
import hashlib
import binascii

def sign_transaction(private_key_hex: str, message: str):
    # Convert private key hex → SigningKey object
    private_key_bytes = bytes.fromhex(private_key_hex)
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)

    # Hash the message using SHA256
    hashed_msg = hashlib.sha256(message.encode()).digest()

    # Sign the hash
    signature = sk.sign(hashed_msg)
    return binascii.hexlify(signature).decode()

if __name__ == "__main__":
    private_key = input("Enter decrypted private key: ")
    message = input("Enter message to sign: ")
    signature = sign_transaction(private_key, message)
    print(f"\n✅ Signature:\n{signature}")
