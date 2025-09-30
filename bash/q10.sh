#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage: $0 <csv_file>"
	exit 1 
fi

csv_file=$1

if [ ! -f "$csv_file" ]; then
	echo "Error:File '$csv_file' not found"
	exit 1
fi

awk -F ',' '{print $1","$3}' "$csv_file"

