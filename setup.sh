#!/bin/bash

# ask for number but accept anything, why not
read -p "Which day? (input number, default today) " DAY
if [ "$DAY" == "" ]; then
    DAY=$(date +%d)
fi
echo "Creating files for day:" $DAY


read -p "Which part? [1]/2 " PART
if [ "$PART" == "" ]; then
    PART=1
fi
echo "Creating files for part:" $PART
mkdir -p "day$DAY"
cd "day$DAY"
if [ "$PART" == 1 ]; then
    cp -n "../template.py" "p1.py"
    touch "p1-input.txt"
    touch "p1-test.txt"
elif [ "$PART" == 2 ]; then
    cp -n "p1-input.txt" "p2-input.txt"
    cp -n "p1-test.txt" "p2-test.txt"
    cp -n "p1.py" "p2.py"
    sed -e "s/p1-/p2-/g" -i "" "p2.py"
fi
