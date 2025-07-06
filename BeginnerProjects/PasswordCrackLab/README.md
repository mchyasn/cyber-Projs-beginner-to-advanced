PasswordCrackLab – GPU-Accelerated Password Cracking with Hashcat


Objective:
```
Simulate password cracking using GPU acceleration with Hashcat. 
Generate test hashes, use dictionary attacks with rockyou.txt, 
and monitor performance.
```
Step 0: Create Project Structure
```
mkdir PasswordCrackLab && cd PasswordCrackLab
mkdir hashes wordlists screenshots
touch README.txt
```
Step 1: Install Hashcat
```
Check version:
    hashcat --version

If not installed:
    sudo apt update
    sudo apt install hashcat -y
```
![Password Cracking Lab](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PasswordCrackLab/screenshots/1.png)

Step 2: Generate Sample Hashes
```
Generate SHA256 hash for the password "pass123":
    echo -n "pass123" | sha256sum

Example output:
    ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f

Save it to file:
    echo "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f" > hashes/sha256.txt
```
![Password Hash Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PasswordCrackLab/screenshots/2.png)

Optional: Generate MD5 hash
```
    echo -n "pass123" | md5sum
    echo "<md5_hash>" > hashes/md5.txt
```

Step 3: Extract and Copy rockyou.txt Wordlist
```
Unzip the default wordlist:
    sudo gunzip /usr/share/wordlists/rockyou.txt.gz

Copy it to project folder:
    cp /usr/share/wordlists/rockyou.txt wordlists/

Verify:
    ls wordlists/
```

Step 4: Crack SHA256 Hash with Hashcat
```
Run dictionary attack:
    hashcat -a 0 -m 1400 hashes/sha256.txt wordlists/rockyou.txt

Options:
    -a 0        Dictionary attack
    -m 1400     SHA256 hash mode

To see the cracked password after cracking completes:
    hashcat -m 1400 hashes/sha256.txt --show
```
![Password Recovery Results](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/PasswordCrackLab/screenshots/3.png)

Step 5: Monitor GPU Usage (Optional)
```
Install GPU inspection tool:
    sudo apt install clinfo

View GPU device name:
    clinfo | grep -i "device name"

View temperature and load:
    watch -n 1 sensors
```

Legal Notice:
-------------
This lab is for educational purposes only. 
Never attempt to crack passwords or hashes you do not own or have explicit permission to test.

Date: July 6, 2025
