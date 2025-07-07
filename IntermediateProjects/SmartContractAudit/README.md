# Smart Contract Audit – VulnerableBank.sol

## Overview

This project demonstrates a basic smart contract audit workflow using industry-standard tools. The contract `VulnerableBank.sol` simulates a vulnerable banking contract to showcase typical smart contract flaws and how to analyze them using static analysis tools such as Mythril and Slither.


## Contract Audited
```
**File:** `contracts/VulnerableBank.sol`  
**Solidity Version:** ^0.8.0  
**Type:** Minimal banking contract with deposit/withdraw functions  
**Purpose:** Intentionally vulnerable for security auditing practice

```

## Tools Used
```
- [Mythril](https://github.com/ConsenSys/mythril) – Symbolic analysis engine
- [Slither](https://github.com/crytic/slither) – Static analyzer from Trail of Bits
- Docker (to ensure clean environments)
```
## Setup Instructions
```
1. Clone the repository and `cd` into the project:
   ```bash
   cd ~/Desktop/SmartContractAudit
Ensure Docker is installed and running:


sudo apt install docker.io -y
sudo systemctl enable --now docker
Audit using Mythril via Docker:

```

```
docker run -v $(pwd):/data mythril/myth analyze /data/contracts/VulnerableBank.sol --execution-timeout 60 --solv 0.8.0 > reports/mythril_report.txt
Optionally, analyze with Slither (requires a compatible host Python environment):


docker run -v $(pwd):/src trailofbits/eth-security-toolbox slither /src/contracts/VulnerableBank.sol > reports/slither_report.txt
Summary of Findings
Refer to findings.md for a high-level audit summary. Includes critical vulnerabilities, severity, and suggestions for remediation.
```
![Smart Contract Security Audit](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/SmartContractAudit/screenshots/1.png)

![Smart Contract Security Audit](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/SmartContractAudit/screenshots/0.png)

Notes
This project is for educational and portfolio purposes only. It does not represent a professional audit of production contracts.

## Author
## Name: mchyasn

## GitHub: github.com/mchyasn

