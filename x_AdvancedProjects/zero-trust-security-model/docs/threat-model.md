# Zero Trust Security Threat Model

## Assumptions

- The internal network is not inherently trusted.
- Any device, user, or service may be compromised.
- Attackers can already be inside the perimeter.
- Traditional perimeter defenses (e.g., firewalls) are insufficient on their own.

## Threats Addressed

- Lateral movement by compromised accounts or malware
- Phishing and credential theft
- Insider threats (intentional or accidental)
- Compromised devices connecting to internal resources
- Privilege escalation through excessive trust

## Zero Trust Planning Goals

- Enforce least-privilege access across users, services, and devices.
- Require identity verification and context-based access decisions.
- Segment access to resources using logical policies, not network location.
- Monitor and log all access attempts and policy decisions.

## Key Security Components

- Identity and Access Management (IAM)
- Multi-Factor Authentication (MFA)
- Micro-segmentation
- Device health verification
- Policy-based access control
