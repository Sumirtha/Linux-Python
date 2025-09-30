#!/bin/bash

for file in *.txt; do
  [ -e "$file" ]
  mv "$file" "old_$file"
done

