# SCADA System Security: Simulated Modbus Attack

## Project Overview

This project focuses on exploring the security vulnerabilities within SCADA systems, specifically targeting the Modbus protocol, commonly used in industrial environments. A simulated manufacturing process was created using **Factory IO**, **OpenPLC runtime**, and **ScadaBR**. The goal was to analyze and identify potential vulnerabilities and test proactive cybersecurity measures.

## Key Technologies

- **Factory IO**: Simulation software for industrial processes.
- **OpenPLC Runtime**: Open-source runtime for controlling programmable logic controllers (PLCs).
- **ScadaBR**: Open-source SCADA software for monitoring industrial systems.
- **Metasploit Framework**: Used for ethical hacking and exploiting vulnerabilities in the Modbus protocol.
- **Nmap**: A network scanning tool used to detect open services and ports.

## Project Setup

### Prerequisites

- **Factory IO**: Install and configure Factory IO for simulating industrial processes.
- **OpenPLC Runtime**: Install OpenPLC runtime for controlling the simulated PLC.
- **ScadaBR**: Install and configure ScadaBR for monitoring the simulated environment.
- **Metasploit Framework**: Install the Metasploit Framework to simulate attacks.
- **Kali Linux**: The environment used for running Nmap and Metasploit.

### Steps to Run

1. **Set up the simulation environment** using Factory IO and OpenPLC runtime.
   
   ![image](https://github.com/user-attachments/assets/8c385a92-94e7-434e-994e-84fdc8609504)

2. **Configure ScadaBR** to monitor and visualize the industrial process.
3. **Run Nmap** to identify open services, focusing on the Modbus protocol's port.
4. **Simulate attacks** using Metasploit's Modbus-specific modules:
   - `modbusdetect`: Detect Modbus services on the network.

      ![image](https://github.com/user-attachments/assets/7d585998-d66c-486d-a093-0c99560c0136)

   - `modbus_findunitid`: Identify slave devices connected to Modbus.
   - `modbusclient`: Exploit vulnerabilities by modifying register values.

      ![image](https://github.com/user-attachments/assets/37f6de17-f71b-4a12-8605-40f5ffcd5229)

      ![image](https://github.com/user-attachments/assets/dff9aeeb-e935-433e-80c5-1bb0b8715a1a)

      ![image](https://github.com/user-attachments/assets/8d36ecb8-43ea-4fbc-99f7-5898fa0736f1)


## Vulnerability Insights

- **Modbus Vulnerabilities**: The project demonstrated how Modbus protocol weaknesses could be exploited in a controlled environment.
- **Proactive Cybersecurity Measures**: Regular vulnerability assessments, ethical hacking, and network monitoring are crucial for preventing cyberattacks.
- **Firewall Configuration**: Properly configuring firewalls to filter and control network traffic is a critical security measure.

## Conclusion

This project highlights the importance of understanding and mitigating security risks in SCADA systems. The simulated attacks on the Modbus protocol revealed critical vulnerabilities, reinforcing the need for proactive cybersecurity strategies in industrial settings.

## Acknowledgments

- Thank you to all contributors for their support and collaboration.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
