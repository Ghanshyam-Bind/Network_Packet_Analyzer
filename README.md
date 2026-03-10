# Network_Packet_Analyzer

## Overview

This project is a simple **Network Packet Analyzer** built using Python.
It captures network packets in real time and displays useful information such as:

* Source IP address
* Destination IP address
* Protocol type (TCP / UDP / ICMP)
* Packet payload (if available)

The program uses the Python library **Scapy** to monitor network traffic and analyze packet data.

---

## Features

* Real-time packet capturing
* Detects common protocols (TCP, UDP, ICMP)
* Displays source and destination IP addresses
* Extracts payload data from packets
* Lightweight and easy to run

---

## Requirements

Before running the program, install the following:

1. **Python 3.x**
2. **Npcap** (required for packet capture on Windows)
3. **Scapy library**

Install Scapy using:

pip install scapy

---

## Installation

1. Clone or download this project Link :- https://github.com/Ghanshyam-Bind/Network_Packet_Analyzer.git

2. Navigate to the project folder

3. Install dependencies

pip install scapy

4. Make sure **Npcap** is installed on your system.(https://npcap.com/#download)

---

## How to Run

Run the script from the terminal:

python packet_sniffer.py

The program will start capturing packets and display information about each packet in the terminal.

---

## Example Output

Packet 1
Source IP: 192.168.0.114
Destination IP: 142.251.220.14
Protocol: TCP
Payload: b'GET / HTTP/1.1'

---

## How It Works

1. The program listens for network packets using Scapy's `sniff()` function.
2. When a packet is captured, it checks if it contains an IP layer.
3. It extracts source IP, destination IP, and protocol information.
4. If a payload exists, the program prints a portion of it.

---

## Educational Purpose

This project is intended for **educational and learning purposes only**.
It demonstrates how packet sniffing and basic network analysis works.

---

## Author

Ghanshyam Bind
