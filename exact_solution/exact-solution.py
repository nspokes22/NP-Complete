"""
    name:  Nick Spokes & Abdallah Derbala

    Source: https://www.guru99.com/travelling-salesman-problem.html
"""
from itertools import permutations


def tsp(graph, start):
    path = []
    vertex = []
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
        min_cost = min(min_cost, current_cost)
    path.append(start)
    print(path)
    return min_cost


def main():
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(tsp(graph, s))


if __name__ == "__main__":
    main()
