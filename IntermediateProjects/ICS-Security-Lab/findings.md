# ICS Security Lab Findings

## 1. Summary

This lab simulates an ICS network with a Modbus server. The attacker connects to the fake PLC and modifies holding register values without authentication.

## 2. Detected Vulnerabilities

- **Unauthenticated Access**: Modbus protocol lacks built-in authentication.
- **Unencrypted Communication**: All reads/writes occur in plaintext over TCP.
- **Register Tampering**: Attacker overwrites critical registers with arbitrary values.

## 3. Evidence

- See `attacks/ics_attack.log` for a full trace of the attacker session.
- `logs/server.log` confirms the malicious activity was executed.
- `scans/nmap.txt` proves the service exposure (TCP port 502).

## 4. Mitigation Recommendations

- Place PLCs behind firewalls/VPNs.
- Use Modbus variants with TLS where possible.
- Implement network segmentation and intrusion detection.
