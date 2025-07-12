# Steganography Tool Usage

## steghide
- Used to embed and extract hidden data in JPEG, BMP, WAV, and AU files.
- Example to extract hidden data:
  ```bash
  steghide extract -sf samples/steg_1.jpg -p ""
exiftool
Extracts metadata from image and media files.

Can reveal hidden comments, software info, or timestamps:

exiftool samples/steg_1.jpg
binwalk
Scans files for embedded file signatures and hidden data.

Can extract embedded files:

binwalk -e samples/steg_1.jpg
strings
Extracts human-readable text from binary files.

Useful for spotting hidden messages or suspicious strings:


strings samples/steg_1.jpg | less
ImageMagick (convert)
Used to generate test images locally.

Example to create a white JPEG for stego testing:


convert -size 1024x768 xc:white samples/steg_1.jpg
