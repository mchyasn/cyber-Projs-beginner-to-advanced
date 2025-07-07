
---

## Educational Value

- Understand root and intermediate CA roles
- Practice real-world certificate lifecycle
- Recreate HTTPS-style trust chain offline
- Perfect for IT/Cybersecurity portfolios

---

## Screenshots to Take

- root key/cert creation
- intermediate CSR + cert
- server cert creation
- openssl verify
"""

# Save the README.md file
readme_path = "/mnt/data/PKI-Lab_README.md"
with open(readme_path, "w") as f:
    f.write(pki_readme)

readme_path
