Network Simulator Project:

Overview
This project is a simple Python-based Network Simulator that uses basic functions and modules. It simulates essential networking concepts such as IP analysis, device connectivity, VLAN segmentation, and IP conflict detection. The project is divided into four modules for better structure and understanding.

 Modules

1. IP Address Analyze (ip_address_analyze.py)
Takes an IP address as input
Checks basic IP format
Performs simple validation

2. Connectivity Check (connectivity_check.py)
takes multiple devices as input
Stores:
Device Name
VLAN ID
IP Address
Checks if devices can communicate:
Same VLAN → Can communicate
Different VLAN → Needs inter-VLAN routing

3. Security Rule Engine (security_rule_engine.py)
Simulates VLAN segmentation rules
Demonstrates basic network security logic
Shows whether communication is allowed or restricted

4. Innovation Section (innovation_section.py)
Detects duplicate IP address conflicts
Identifies if two devices have the same IP
Displays warning message if conflict found

How to Run
Open terminal in project folder
Run:
python main.py
Follow the input instructions on screen

Technologies Used
Python 
Basic Functions
Loops
Lists
Dictionaries
Conditional Statements

Networking/
│
├── main.py
├── ip_address_analyze.py
├── connectivity_check.py
├── security_rule_engine.py
├── innovation_section.py
└── README.md
