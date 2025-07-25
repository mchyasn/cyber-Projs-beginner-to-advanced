# CS-Security-Lab

### This lab simulates an Industrial Control System (ICS) environment by setting up a fake Modbus PLC server and simulating an attacker who exploits it. The goal is to demonstrate common ICS threats and log attack traces.

1. Clone the repo and enter the project directory:
```
   $ cd ICS-Security-Lab
```

2. Run the setup:
```
   $ chmod +x setup.sh
   $ ./setup.sh
```
![ICS Security Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/ICS-Security-Lab/screenshots/0.png)

3. Start the fake PLC server:
```
   $ python server.py
```
4. Open a second terminal and launch the attacker:
```
   $ python attacker.py
```
![ICS Security Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/ICS-Security-Lab/screenshots/3.png)
5. Check `attacks/`, `logs/`, and `scans/` for evidence.

Dependencies
```
- Python 3
- pymodbus
- nmap (for scanning)
- binwalk (optional for firmware inspection)
```

The project demonstrates:
```
- Weaknesses of ICS protocols (like Modbus)
- Register manipulation by attackers
- Evidence collection through logs and scans
```
![ICS Security Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/ICS-Security-Lab/screenshots/2.png)

![ICS Security Analysis](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/ICS-Security-Lab/screenshots/3.png)
Credits
-------

## Developed by mchyasn for hands-on cybersecurity lab simulations.
