"""
    name:  Nick Spokes & Abdallah Derbala
    Program type: Random

    Source: https://www.guru99.com/travelling-salesman-problem.html
"""
import time
import random
from copy import deepcopy
import argparse
import math


def tsp(graph, t):
    start = 0
    curr_permut, cycle = [], None
    min_cost = float('inf')
    for index in range(len(graph)):
        if index != start:
            curr_permut.append(index)
    time_limit = time.time() + t
    while time.time() < time_limit:
        random.shuffle(curr_permut)
        sa = SA(100000, 1000, graph, curr_permut, 0.99)
        best, curr_cycle = sa.run()
        if best < min_cost:
            min_cost = best
            cycle = [start] + curr_cycle 
    cycle.append(start)
    return min_cost, cycle
    # n = len(graph)
    # cap = 1
    # time_limit = time.time() + t  # 60 seconds
    # while time.time() < time_limit:
    #     curr_cycle = [start]
    #     current_cost = 0
    #     item = start
    #     random.shuffle(curr_permut)

    #     worse_counter = 0
    #     while worse_counter < cap:
    #         curr_cycle = [start]
    #         current_cost = 0

    #         # calculates the total cost of the current cycle
    #         for index in curr_permut:
    #             current_cost += graph[item][index]
    #             item = index
    #             curr_cycle.append(index)
    #         current_cost += graph[item][start]

    #         # checks if the current cost of the cycle is lower than the current min cost
    #         if current_cost < min_cost:
    #             cycle = deepcopy(curr_cycle)
    #             min_cost = current_cost
    #         else:
    #             ind1 = random.randrange(2, n -1)
    #             ind2 = random.randrange(2, n -1)
    #             temp = curr_permut[ind1]
    #             curr_permut[ind1] = curr_permut[ind2]
    #             curr_permut[ind2] = temp
    #             worse_counter += 1
    # cycle.append(start)
    # return min_cost, cycle


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("timing", type=int, nargs='?', default=30, help="timing argument")
    args = parser.parse_args()
    timing = int(args.timing)
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


class SA:
    def __init__(self, iterations, temp, graph, permut, gamma):
        self.iterations = iterations
        self.temp = temp
        self.permut = permut
        self.graph = graph
        self.gamma = gamma

    def total_distance(self, curr_permut):
        current_cost, item = 0, 0
        for index in curr_permut:
            current_cost += self.graph[item][index]
            item = index
        current_cost += self.graph[item][0]
        return current_cost

    @staticmethod
    def cooling_temp(gamma, temp):
        return gamma*temp

    @staticmethod
    def check_accept(temp, new_solution, current_solution):
        x = (current_solution - new_solution) / temp
        if x > 0:
            prob = 1
        else:
            prob = math.exp(x)
            prob = min(prob, 1)
        if prob > random.uniform(0, 1):
            return True
        return False

    @staticmethod
    def swap_elements(curr_permut):
        swapped = curr_permut.copy()
        swap_list_indx = range(0, len(curr_permut) - 1)
        i = random.randint(swap_list_indx[0], swap_list_indx[-1])
        j = random.randint(swap_list_indx[0], swap_list_indx[-1])
        if i == j:
            while i == j:
                j = random.randint(swap_list_indx[0], swap_list_indx[-1])
        swapped[i], swapped[j] = swapped[j], swapped[i]
        return swapped

    def run(self):
        temp = self.temp
        gamma = self.gamma
        permut = self.permut
        current = self.total_distance(self.permut)
        best = self.total_distance(self.permut)
        best_permut = permut
        for i in range(self.iterations):
            swapped = self.swap_elements(permut)
            new = self.total_distance(swapped)
            if new < best:
                best_permut = deepcopy(swapped)
                best = new
            if self.check_accept(temp, new, current):
                permut = swapped.copy()
                current = new
            temp = self.cooling_temp(gamma, temp)
        return best, best_permut


if __name__ == "__main__":
    main()
