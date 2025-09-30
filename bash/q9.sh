#!/bin/bash

num=(4 3 8 6 7)
max=${num[0]}
min=${num[0]}

for i in "${num[@]}"
do
	if [[ "$i" -gt "$max" ]]; then
		max="$i"
	fi

	if [[ "$i" -lt "$min" ]]; then
		min="$i"
	fi

done

echo "max is:" $max
echo "min is:" $min
