# Timing-Based Side-Channel Attack Simulation

This project demonstrates a basic timing side-channel attack in a controlled environment using Python. The purpose is to understand how execution time can inadvertently leak information about secret values, such as passwords.

## Objective

To simulate and analyze a timing attack in a safe, isolated Kali Linux virtual machine. The project demonstrates how attackers can infer secret information based on time delays in comparison operations.

## Files and Purpose

- `attack-demo.py`: Simulates a vulnerable password checker with character-by-character comparison and time delays.
- `parse_log.py`: Reads the raw output log and lists password guessing progress step by step.
- `setup.sh`: Installs Python3 dependencies on Kali Linux.
- `data/output.txt`: Output from the attack script execution.
- `data/parsed_output.txt`: Formatted version showing each guess attempt.
- `notes.md`: Documentation of the attack methodology and research notes.

## Attack Method

The core attack relies on measuring response time differences during string comparison. The simulated password checker delays slightly for each correct character, unintentionally leaking timing data.

Example behavior:
- If the first character is correct, it waits 0.1s before checking the next.
- If not, it returns immediately.
- By iterating through characters and measuring time taken, the full password can be reconstructed.

## Execution Steps

1. **Setup environment:**

   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. **Run the timing attack simulation:**

   ```bash
   python3 attack-demo.py | tee data/output.txt
   ```
![Side-Channel Attack Simulation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/side-channel-attacks/screenshots/0.png)

3. **Parse the log:**

   ```bash
   python3 parse_log.py | tee data/parsed_output.txt
   ```
![Side-Channel Attack Simulation](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/side-channel-attacks/screenshots/1.png)

## Environment

- Kali Linux VM (safe and isolated)
- Python 3.x
- No external libraries required

## Disclaimer

This project is for educational purposes only. All demonstrations were conducted in a secure virtual environment. Do not use these techniques on real systems or networks.

## Author
# mchyasn
