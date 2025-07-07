#!/bin/bash

echo "[*] File listing:"
find ../extracted/ -type f | tee ../logs/files.txt

echo -e "\n[*] Looking for ELF binaries:"
find ../extracted/ -type f -exec file {} \; | grep ELF | tee ../logs/elf_binaries.txt

echo -e "\n[*] Looking for password keywords:"
grep -Ri "pass" ../extracted/ | tee ../logs/password_strings.txt
