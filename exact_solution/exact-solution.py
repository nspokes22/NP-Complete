"""
    name:  Nick Spokes & Abdallah Derbala

    Source: https://www.guru99.com/travelling-salesman-problem.html
"""
from itertools import permutations


def tsp(graph, start):
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
        min_cost = min(min_cost, current_cost)
    path.append(start)
    return min_cost, path


def main():
    size, start = [int(item) for item in input().split()]
    items = [[int(item) for item in input().split()] for _ in range(size)]
    min_cost, path = tsp(items, start)
    print(f"{min_cost}\n{path}")


if __name__ == "__main__":
    main()
