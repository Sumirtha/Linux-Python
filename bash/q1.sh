#!/bin/bash

read -p "Enter a number: " n
if [ "$n" -le 1 ]; then 
	echo "Not prime"; exit; fi
for ((i=2; i*i<=n)); do
  if ((n % i == 0)); then 
  	echo "Not prime"; exit; fi
done
echo "Prime"

