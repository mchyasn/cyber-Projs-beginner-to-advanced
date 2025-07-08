#!/bin/bash
# Replace <target-ip> with the IP you're testing
nmap -sS -p 22,80,443 <target-ip>
