#!/bin/bash

m=1
c=299792458
E=$(bc << EOF
scale=9
$m*$c*$c
EOF
)
echo "The calculated energy-mass equivalence is" $E
