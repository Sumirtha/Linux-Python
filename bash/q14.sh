#!/bin/bash
end=$((SECONDS + 300))

while [ $SECONDS -lt $end ]; do
  free_mem=$(free -m | awk 'NR==2 {print $7}')
  if [ "$free_mem" -lt 500 ]; then
    echo "Warning: Low memory ($free_mem MB)"
  fi
  sleep 10
done

