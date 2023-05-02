#!/bin/bash
for i in {1..15}
do
    echo "Graph size: $i"
    /usr/bin/time -f "Run time: %e sec" python approx-solution.py $1 < test_cases/$i.txt
    echo
done