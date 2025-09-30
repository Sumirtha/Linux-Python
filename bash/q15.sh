#!/bin/bash

backup_file="backup_$(date).tar.gz"
files=$(find /var/log/ -type f -mtime +7)
if [ -z "$files" ]; then
  echo "No files older than 7 days found in /var/log/"
  exit 0
fi
echo "Creating archive: $backup_file"
tar czf "$backup_file" $files

