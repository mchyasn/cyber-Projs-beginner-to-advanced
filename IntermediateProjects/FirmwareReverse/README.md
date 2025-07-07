# Firmware Reverse Engineering

## Objective
Reverse-engineer an embedded firmware image to inspect its contents, extract file systems, and analyze for possible flaws or backdoors.

## Tools Used
- binwalk
- wget
- Linux shell commands (mv, rm, grep, file)

## Steps

1. Create project folders:
```
   mkdir -p FirmwareReverse/bin FirmwareReverse/extracted
   cd FirmwareReverse
```
2. Download a sample OpenWRT firmware binary:
```
   cd bin
   wget https://downloads.openwrt.org/releases/18.06.9/targets/ar71xx/tiny/openwrt-18.06.9-ar71xx-tiny-tl-wr841-v8-squashfs-factory.bin
   cd ..
```
![Firmware Reverse Engineering](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/FirmwareReverse/screenshots/0.png)

3. Extract firmware using binwalk:
```
   binwalk -e bin/openwrt*.bin
```
![Firmware Reverse Engineering](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/FirmwareReverse/screenshots/1.png)
4. Move extracted files:
```
   mkdir -p extracted
   mv bin/_openwrt-18.06.9-ar71xx-tiny-tl-wr841-v8-squashfs-factory.bin.extracted/* extracted/
   rm -rf bin/_openwrt*
```
5. Explore the extracted filesystem:
```
   - Inspect init scripts:
     ls extracted/squashfs-root/etc/init.d/
   - Analyze binaries:
     file extracted/squashfs-root/bin/*
   - Search for credentials or interesting strings:
     grep -Ri 'password' extracted/
     grep -Ri 'admin' extracted/
```
6. Optional deeper inspection:
```
   - Use `strings`, `radare2`, or `ghidra` to inspect binaries.
   - Check for outdated or hardcoded packages.
   - Look for insecure default configurations.
```
## Notes
- Be cautious of symlink warnings during extraction.
- Do not run binaries from firmware directly on your host system.

## Outcome
This project demonstrates how to extract, inspect, and perform a basic security review of embedded firmware using open source tools.
