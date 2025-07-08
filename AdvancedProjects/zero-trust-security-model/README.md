# Zero Trust Security Model (Advanced)

## Overview

This project demonstrates the core components of a Zero Trust Security Model implemented in a simulated environment using shell and Python scripts. It assumes a compromised internal network and enforces strict identity, device, and policy-based access controls.

## Objectives

- Eliminate implicit trust in the internal network
- Enforce user and device authentication
- Implement least-privilege access
- Apply microsegmentation for service isolation
- Monitor and simulate policy enforcement


## Components
```
### Threat Model (`docs/threat-model.md`)
Outlines Zero Trust assumptions and the threats this model mitigates, including lateral movement, insider threats, and device compromise.
```
### Access Verification (`src/verify-access.py`)
Validates users, devices, and IP addresses against trusted lists. Access is granted only if all parameters match trusted conditions.
```
### Device Health Check (`src/health-check.sh`)
Simulates endpoint trust evaluation:
- Antivirus service running
- System update status
- Absence of known suspicious processes
```
### Access Policies (`policies/access-policies.yaml`)
Defines who can access which services based on role. Uses a default-deny approach.
```
### Microsegmentation Rules (`policies/firewall-rules.json`)
Logical rules to restrict service communication paths. Only authorized sources may access protected services like databases.
```
### Setup Script (`setup/config-zero-trust.sh`)
Simulates a complete Zero Trust posture by running health checks, identity verification, and policy applications in sequence.

```
```
To simulate the Zero Trust model:

```bash
cd zero-trust-security-model/
./setup/config-zero-trust.sh
```

You will be prompted to provide:
- A username
- Device name
- IP address

Based on predefined access policies, access will be granted or denied.
## screenshots
![Zero Trust Architecture Implementation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/AdvancedProjects/zero-trust-security-model/screenshots/0.png)
![Zero Trust Architecture Implementation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/AdvancedProjects/zero-trust-security-model/screenshots/1.png)
![Zero Trust Architecture Implementation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/AdvancedProjects/zero-trust-security-model/screenshots/2.png)
![Zero Trust Architecture Implementation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/AdvancedProjects/zero-trust-security-model/screenshots/22.png)

## Requirements

- Kali Linux (or any Linux-based environment with Python 3 and Bash)
- Basic terminal permissions

## Notes

This project is a conceptual demonstration of Zero Trust principles. In real-world deployments, enforcement would occur via centralized identity providers, endpoint management, and firewall/orchestration platforms.
