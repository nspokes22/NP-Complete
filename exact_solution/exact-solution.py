"""
    name:  Nick Spokes & Abdallah Derbala

    Source: https://www.guru99.com/travelling-salesman-problem.html
"""
from itertools import permutations


def tsp(graph):
    start = 0
    vertex, path = [], None
    min_cost = float('inf')
    for index in range(len(graph)):
        if index != start:
            vertex.append(index)
    all_perms = permutations(vertex)
    for curr_permut in all_perms:
        curr_path = [start]
        current_cost = 0
        item = start
        for index in curr_permut:
            current_cost += graph[item][index]
            item = index
            curr_path.append(index)
        current_cost += graph[item][start]
        if current_cost < min_cost:
            path = curr_path
            min_cost = current_cost
    path.append(start)
    return min_cost, path


def main():
    arb2num, num2arb, count, ending = {}, {}, 0, ' '
    qty_v, qty_e = [int(item) for item in input().split()]
    items = [[0] * qty_v for _ in range(qty_v)]
    for _ in range(qty_e):
        v1, v2, w = input().split()
        if v1 not in arb2num:
            arb2num[v1] = count
            num2arb[count] = v1
            count += 1
        if v2 not in arb2num:
            arb2num[v2] = count
            num2arb[count] = v2
            count += 1
        index1 = arb2num[v1]
        index2 = arb2num[v2]
        items[index1][index2] = int(w)
        items[index2][index1] = int(w)
    min_cost, path = tsp(items)
    print(min_cost)
    for index, item in enumerate(path):
        if index == len(path) - 1:
            ending = '\n'
        print(num2arb[item], end=ending)


if __name__ == "__main__":
    main()
