# Steganography Detection Project

This project demonstrates how to detect and extract hidden data from image files using popular steganography and forensic tools on Linux.

## Objective

Detect hidden messages or files inside a sample JPEG image (`steg_1.jpg`) using a set of tools commonly used in forensic investigations and CTFs.


## Tools Used

- **steghide** – Embed/extract hidden data in media files
- **exiftool** – Extract image metadata
- **binwalk** – Scan for embedded file signatures
- **strings** – Extract printable characters from binaries
- **ImageMagick** – Generate test images for local stego testing

## How to Reproduce

### 1. Create a Test Image

```bash
sudo apt install -y imagemagick steghide exiftool binwalk
mkdir -p samples
convert -size 1024x768 xc:white samples/steg_1.jpg

2. Embed a Secret Message
```
echo "Flag{Stego_Detection_Successful}" > secret_message.txt
steghide embed -cf samples/steg_1.jpg -ef secret_message.txt -p ""
rm secret_message.txt
```
3. Attempt Extraction
```
steghide extract -sf samples/steg_1.jpg -p ""
cat secret_message.txt
```
4. Metadata and Signature Scanning
```
# Metadata
exiftool samples/steg_1.jpg > scans/exiftool_steg1.log

# Binary signatures
binwalk samples/steg_1.jpg > scans/binwalk_steg1.log

# Strings
strings samples/steg_1.jpg > scans/strings_steg1.txt
```
Results Summary
See findings.md for a detailed write-up.

steghide successfully extracted the embedded flag

exiftool, binwalk, and strings did not reveal obvious signs of steganography

Demonstrates the importance of format-specific tools in detection

Author
mchyasn | github.com/mchyasn
