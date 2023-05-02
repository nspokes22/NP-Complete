#!/bin/bash
echo "Lower Bound Test Cases"
echo
echo
for i in {1..14}
do
    echo "Graph size: $i"
    python lower_bound.py < test_cases/$i.txt
    echo
done