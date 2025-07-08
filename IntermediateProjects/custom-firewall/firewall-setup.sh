#!/bin/bash

# Flush existing rules
iptables -F

# Default policy: deny all incoming, allow all outgoing
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback interface
iptables -A INPUT -i lo -j ACCEPT

# Allow traffic from localhost explicitly
iptables -A INPUT -s 127.0.0.1 -j ACCEPT

# Allow established & related connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow SSH from any source for testing (tighten later)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Allow HTTP & HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Log all other traffic
iptables -A INPUT -j LOG --log-prefix "Dropped Packet: "
