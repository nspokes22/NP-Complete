"""
    name:  Abdallah Derbala
    
"""
from collections import defaultdict
def dist_formula(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**(1/2)


def dfs_label(graph, v, labels, currentLabel):
    bag = [v]
    while bag: # while bag is not empty
        u = bag.pop()
        if labels[u] == -1:
            labels[u] = currentLabel
            for w in graph[u]:
                bag.append(w)


def count_and_label(graph):
    labels = [-1 for _ in range(len(graph))] # Initially all labels are 0
    count = -1
    for v in range(len(graph)): # for each vertex
        if labels[v] == -1: # if v is not visited
            count += 1
            dfs_label(graph, v, labels, count)
    return count+1, labels


def add_all_safe_edges(w, f, count, labels):
    safe = [(None, None, None)] * count
    for u in range(len(w)):
        for v in range(u + 1, len(w)):
            if labels[u] != labels[v]:
                weight = w[u][v]
                if safe[labels[u]][2] == None or weight < safe[labels[u]][2]:
                    safe[labels[u]] = (u, v, weight)
                if safe[labels[v]][2] == None or weight < safe[labels[v]][2]:
                    safe[labels[v]] = (u, v, weight)
    for i in range(count):
        f[safe[i][0]].add(safe[i][1])
        f[safe[i][1]].add(safe[i][0])


def boruvka(n, w):
    f = [set() for _ in range(n)]
    count, labels = count_and_label(f)
    total = 0
    while count > 1:
        add_all_safe_edges(w, f, count, labels)
        count, labels = count_and_label(f)
    return f


# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    arb2num, num2arb, count, ending = {}, {}, 0, ' '
    qty_v, qty_e = [int(item) for item in input().split()]
    items = [[None] * qty_v for _ in range(qty_v)]
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

    checker = set()
    f = boruvka(qty_v, items)
    total = 0
    for i in range(qty_v):
        for j in f[i]:
            if (j,i) not in checker:
                checker.add((i,j))
                total += items[i][j]
    print(total)

    


if __name__ == "__main__":
    main()