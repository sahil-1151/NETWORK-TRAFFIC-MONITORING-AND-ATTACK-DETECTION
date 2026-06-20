@  Network Traffic Monitoring and Attack Detection

~ Overview

This project aims to monitor network traffic and detect suspicious activities such as:

1. Port scanning
2. Brute force attempts
3. ICMP sweep attacks
4. Abnormal traffic patterns

~  Objectives

1. Capture packets from the network.
2. Analyze packet information.
3. Detect malicious activities.
4. Generate alerts and logs.
5. Build a lightweight Intrusion Detection System (IDS).

~  Technologies

1. Python
2. Scapy
3. Flask
4. SQLite

~ Project Status

Phase 1: Project initialization and planning.

Phase 2: Create a simple network anyalising function so that it will provide us detailed of the system communticating with other devices and displayed source and destination ip .

Phase 3: Modify the function with some filter like -> tcp , udp , icmp and souce and destination port are extracted and also packet statics were maintained .

Phase 4: Now we have started storing capture packet in the csv file for future analysis , live traffic statistics and packet rate monitory were also implemented .

------------------

Future Work

The upcoming phase of the project focuses on attack detection and visualization.

Planned Features 
- Port Scan Detection
Detect when a host attempts connections to multiple ports in a short period of time.

- Brute Force Detection
Identify repeated login attempts on services like SSH and FTP.

- ICMP Sweep Detection
Detect ping sweeps used during network reconnaissance.

- SYN Flood Detection
Monitor excessive SYN packets to identify denial of service attacks.

- Suspicious Traffic Pattern Detection
Analyze unusual traffic behavior and abnormal packet rates.

- Alert Generation System
Generate warnings whenever suspicious activities are detected.

- Database Integration
Store alerts and traffic logs using SQLite for better management.

- Dashboard Development :Develop a Flask-based web dashboard to display:
 Live traffic statistics
Attack alerts
Top source IP addresses
Protocol distribution

Outcome 

The final aim of the system is to act as 'intrusion detection system' which is capable of monitoring network traffic & detect malicious activities -> such as port scanning , brute force attempts and suspicious traffic pattern .  
