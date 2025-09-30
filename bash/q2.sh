#!/bin/bash
read -p "Enter filename: " f
if [ -e "$f" ]; then
  echo "File exists."
  [ -r "$f" ] && echo "Readable"
  [ -w "$f" ] && echo "Writable"
else
  echo "File does not exist."
fi

