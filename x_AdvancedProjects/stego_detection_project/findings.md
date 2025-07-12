# Steganography Detection Project – Findings

## Target File
- **Filename**: samples/steg_1.jpg
- **Purpose**: Detect and extract hidden data from a JPEG file using open-source tools.

---

## Tools Used and Results

### steghide
- Successfully extracted hidden file:

- Password used: empty string (`""`)

### exiftool
- Output saved in `scans/exiftool_steg1.log`
- No suspicious metadata found; standard fields only.

### binwalk
- Output saved in `scans/binwalk_steg1.log`
- No embedded file signatures or extractable data detected.

### strings
- Output saved in `scans/strings_steg1.txt`
- No meaningful strings indicating hidden content.

---

## Conclusion

The file `steg_1.jpg` was embedded with a secret message using `steghide`. It successfully bypassed `binwalk` and `strings` analysis, demonstrating that metadata- and signature-based tools may fail to detect steganography when encryption or LSB methods are used.

Detection and extraction succeeded only through steghide with knowledge of the format and password.

