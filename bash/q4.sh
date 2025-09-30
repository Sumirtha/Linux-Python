#!/bin/bash

echo "Contents of current directory:"
ls -lh

echo -e "\nLargest file in the current directory:"
find . -maxdepth 1 -type f -exec ls -lh {} + | sort -k 5 -hr | head -n 1

