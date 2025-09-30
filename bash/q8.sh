#!/bin/bash

echo "Mini System Report"

# a) Current date and time
echo "Date & Time: $(date)"

# b) Logged-in users
echo -e "\nLogged-in Users:"
who

# c) System uptime
echo -e "\nSystem Uptime:"
uptime -p

# d) Top 5 processes by memory usage
echo -e "\nTop 5 Processes by Memory Usage:"
ps -eo pid,comm,%mem --sort=-%mem | head -n 6

