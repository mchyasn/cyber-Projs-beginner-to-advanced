#!/bin/bash
echo "[*] Installing steganography analysis tools..."

sudo apt update
sudo apt install -y steghide exiftool binwalk ruby binutils foremost ffmpeg

echo "[*] Installing zsteg (Ruby-based)..."
sudo gem install zsteg

echo "[+] Tools installed:"
echo "- steghide"
echo "- exiftool"
echo "- binwalk"
echo "- zsteg"
echo "- foremost"
echo "- strings (via binutils)"
