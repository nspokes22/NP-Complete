"""
    name:  Nick Spokes & Abdallah Derbala
    Program type: Random

    Source: https://www.guru99.com/travelling-salesman-problem.html
"""
import time
import random
import sys


def tsp(graph, t):
    start = 0
    curr_permut, cycle = [], None
    min_cost = float('inf')
    # adds/assigns a number to each vertex to be inputted to current purmutation
    for index in range(len(graph)):
        if index != start:
            curr_permut.append(index)

    # adds the time inputted to the current time to essentially act as a countdown
    time_limit = time.time() + t  # 60 seconds

    while time.time() < time_limit:
        curr_cycle = [start]
        current_cost = 0
        item = start
        # randomizes the current permutation to find a better cycle
        random.shuffle(curr_permut)

        # calculates the total cost of the current cycle
        for index in curr_permut:
            current_cost += graph[item][index]
            item = index
            curr_cycle.append(index)
        current_cost += graph[item][start]

        # checks if the current cost of the cycle is lower than the current min cost
        if current_cost < min_cost:
            cycle = curr_cycle
            min_cost = current_cost
    cycle.append(start)
    return min_cost, cycle


def main():
    timing = int(sys.argv[1])
    arb2num, num2arb, count, ending = {}, {}, 0, ' '
    qty_v, qty_e = [int(item) for item in input().split()]
    items = [[0] * qty_v for _ in range(qty_v)]
    for _ in range(qty_e):
        v1, v2, w = input().split()
        for v in [v1, v2]:
            if v not in arb2num:
                arb2num[v] = count
                num2arb[count] = v
                count += 1
        index1 = arb2num[v1]
        index2 = arb2num[v2]
        items[index1][index2] = float(w)
        items[index2][index1] = float(w)
    min_cost, cycle = tsp(items, timing)
    print(min_cost)
    if len(cycle) > 2:
        for index, item in enumerate(cycle):
            if index == len(cycle) - 1:
                ending = '\n'
            print(num2arb[item], end=ending)


if __name__ == "__main__":
    main()
