#!/bin/bash

echo "My HOME value is :$HOME"

bc << EOF
scale=7
23934/44343
EOF


echo "Files starting with D:"
ls -p $HOME | grep '^D'

echo "Lines in /etc/passwd"
grep "$USER" /etc/passwd

