from ecdsa import SigningKey, SECP256k1
import hashlib
import base58

def generate_wallet():
    # Generate private key
    sk = SigningKey.generate(curve=SECP256k1)
    private_key = sk.to_string().hex()

    # Get public key
    vk = sk.get_verifying_key()
    public_key = vk.to_string().hex()

    # Derive wallet address (Bitcoin-style)
    sha256_pk = hashlib.sha256(bytes.fromhex(public_key)).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_pk)
    hashed_pk = ripemd160.digest()

    # Add version byte (0x00) + checksum
    versioned = b'\x00' + hashed_pk
    checksum = hashlib.sha256(hashlib.sha256(versioned).digest()).digest()[:4]
    address = base58.b58encode(versioned + checksum).decode()

    return private_key, public_key, address

if __name__ == "__main__":
    priv, pub, addr = generate_wallet()
    print(f"Private Key: {priv}")
    print(f"Public Key:  {pub}")
    print(f"Address:     {addr}")
