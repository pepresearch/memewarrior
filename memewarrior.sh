#!/bin/sh

pip install --upgrade pip
OUTPUT=`pip list`

if ! grep -q "[Pp]illow" <<< "$OUTPUT" ; then
  pip install pillow
fi

python memewarrior.py "$1"
echo "Hit ENTER to continue . . ."
read line
