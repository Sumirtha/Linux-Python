#!/bin/bash
read -p "Enter file: " f
[ -f "$f" ] && wc "$f" || echo "File not found."

