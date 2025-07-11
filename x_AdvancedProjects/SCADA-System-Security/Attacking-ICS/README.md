# Attacking ICS Lab #1
Hands-on ICS security labs from TryHackMe, including Attacking ICS #1 and #2. Exploring vulnerabilities in SCADA systems, Modbus protocol, and critical infrastructure security.

![AltText](main.png)

## Key Tasks & Concepts
### Task 1: Introduction to OT/ICS

    Learn about Operational Technology (OT) systems like SCADA and PLCs.

    Key takeaway: Security is often secondary to operational continuity in ICS


### Task 2: Modbus Protocol Analysis

Use Python’s pymodbus library to interact with PLC registers:

- read_holding_registers(): Reads sensor/control values
        
- write_register(): Modifies register values (e.g., activating valves)

Scripts provided:

    discovery.py (for monitoring registers)

    attack_move_fill.py (for sending malicious commands)
![AltText](ics5.png)

<br>

![AltText](ics4.png)

### Task 3: Simulated Plant Interaction

Observe 16 binary registers (0 or 1) controlling the plant’s behavior (e.g., conveyor belts, fill valves)


Static register (e.g., register 16) identifies non-changing components

![AltText](ics3.png)

### Task 4/5: Attack Simulation

Manipulate registers to disrupt the production line using set_reg.py:

- Overfill bottles by forcing valves to stay open.

- Stop conveyors to cause spills
    
![AltText](ics6.png)

# Attacking ICS #2

## Lab Overview

Objective: Exploit insecure Modbus communications to manipulate PLC registers and trigger physical process failures.

Simulation: Oil refinery plant with valves, pumps, and counters controlled via registers

## Core Tasks & Attack Methodology
### Task 1: Trigger Tank Overflow

Objective: Overflow the oil tank for ≥60 seconds to retrieve flag1.txt.

    Steps: 1. Observe registers with discover.py
           2. Change register values with set_reg.py

Use discovery.py to identify critical registers:

- PLC_FEED_PUMP (Register 1): Controls oil inflow.
  
- PLC_OUTLET_VALVE (Register 3): Manages oil outflow.


Modify attack_move_fill.py to:

    Open the feed pump (write_register(3, 1)).

    Close the outlet valve (write_register(3, 0)

![AltText](ics7.png)

<br> 

After 60 seconds, access http://<MACHINE_IP>/flag1.txt

![AltText](ics8.png)

### Task 2: Redirect Oil Flow

    Objective: Route oil exclusively through the separator valve until 2000 units are processed (flag2.txt).

    Steps: Reset the simulation

Configure registers to:

    Open: Feed pump (Register 1), outlet valve (Register 3), separator valve (Register 4).

    Close: Wastewater valve (Register 8)

Monitor PLC_OIL_PROCESSED (Register 7) until it reaches 2000

![AltText](ics9.png)

### Simulation Tools:

- VirtuaPlant: GitHub-based ICS simulator used in the lab

- ModbusPal: Alternative Modbus slave simulator for testing


### Security Implications

Protocol Vulnerabilities:

1. Modbus’ plaintext communication enables MITM attacks and unauthorized register manipulation
2. Autonomous PLC operation allows persistent malicious control during network outages


### Physical Implications
Attacks can cause spills, equipment damage, or production halts


























