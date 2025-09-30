#!/bin/bash
u=$(df / | awk 'NR==2 {print $5}' | tr -d '%')
echo "Disk Usage: $u%"
[ "$u" -gt 80 ] && echo "Warning: Usage above 80%!"

