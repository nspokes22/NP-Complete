#!/bin/bash
for i in {1..14}
do
    echo "Graph size: $i"
    python lower_bound.py < test_cases/$i.txt
    echo
done