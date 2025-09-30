#!/bin/bash

end=$((SECONDS + 60))

while [ $SECONDS -lt $end ]; do
  date | awk '{print $4}'   
  sleep 10
done

