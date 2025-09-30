#!/bin/bash
read -p "Number: " n
for i in {1..20}; do
  echo "$n x $i = $((n*i))"
done

