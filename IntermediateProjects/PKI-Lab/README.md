# PKI-Lab – Build a Public Key Infrastructure (Offline Lab)

This lab demonstrates how to build a full Public Key Infrastructure (PKI) from scratch using OpenSSL in a safe, offline environment. It simulates real-world certificate management for HTTPS, secure internal services, and identity validation.

## Project Structure

PKI-Lab/
├── rootCA/               # Root Certificate Authority
│   ├── root.key.pem
│   ├── root.cert.pem
│   └── root.srl
├── intermediateCA/      # Intermediate CA
│   ├── intermediate.key.pem
│   ├── intermediate.csr.pem
│   ├── intermediate.cert.pem
│   └── intermediate.srl
├── certs/               # Issued certs
│   └── server.cert.pem
├── csr/                 # Certificate Signing Requests
│   └── server.csr.pem
├── private/             # Private keys
│   └── server.key.pem
├── screenshots/         # Proof/screenshots
└── README.md

## Steps

### Step 1: Root Certificate Authority

1.1 Generate Root Private Key
```
openssl genrsa -out rootCA/root.key.pem 4096
chmod 600 rootCA/root.key.pem
```
1.2 Generate Root Self-Signed Certificate
```
openssl req -x509 -new -nodes -key rootCA/root.key.pem \\
  -sha256 -days 3650 \\
  -out rootCA/root.cert.pem
```
### Step 2: Intermediate CA
```
2.1 Generate Intermediate Private Key
openssl genrsa -out intermediateCA/intermediate.key.pem 4096
chmod 600 intermediateCA/intermediate.key.pem
```
2.2 Generate CSR
```
openssl req -new -key intermediateCA/intermediate.key.pem \\
  -out intermediateCA/intermediate.csr.pem
```
2.3 Sign CSR with Root CA
```
openssl x509 -req -in intermediateCA/intermediate.csr.pem \\
  -CA rootCA/root.cert.pem -CAkey rootCA/root.key.pem \\
  -CAcreateserial -out intermediateCA/intermediate.cert.pem \\
  -days 1825 -sha256
```
### Step 3: Issue Server Certificate

3.1 Generate Server Key
```
openssl genrsa -out private/server.key.pem 2048
```
3.2 Create CSR
```
openssl req -new -key private/server.key.pem -out csr/server.csr.pem

3.3 Sign Server CSR with Intermediate CA
openssl x509 -req -in csr/server.csr.pem \\
  -CA intermediateCA/intermediate.cert.pem \\
  -CAkey intermediateCA/intermediate.key.pem \\
  -CAcreateserial -out certs/server.cert.pem \\
  -days 365 -sha256
```
![PKI Infrastructure Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/PKI-Lab/screenshots/0.png)
![PKI Infrastructure Setup](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/PKI-Lab/screenshots/1.png)
### Step 4: Verify the Chain
```
openssl verify -CAfile <(cat intermediateCA/intermediate.cert.pem rootCA/root.cert.pem) \\
  certs/server.cert.pem

Expected Output:
certs/server.cert.pem: OK
```
## Educational Value
```
- Understand root and intermediate CA roles
- Practice real-world certificate lifecycle
- Recreate HTTPS-style trust chain offline
- Perfect for IT/Cybersecurity portfolios
