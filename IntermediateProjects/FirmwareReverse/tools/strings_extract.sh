#!/bin/bash

mkdir -p ../logs/strings

echo "[*] Extracting strings from binaries..."

for f in $(find ../extracted/ -type f -executable); do
    name=$(basename "$f")
    strings "$f" > "../logs/strings/${name}.txt"
done

echo "[+] Strings dumped into ../logs/strings/"
