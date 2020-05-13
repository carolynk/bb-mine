import math


class convert:
    def __init__(self, g):
        self.graph = g
        self.len = len(self.graph.keys())
        self.matrix = [[0] * (self.len) for i in range(self.len)]

    def convert_adjlist_to_matrix(self):
        keys = self.graph.keys()
        print(keys)
        i, j = 0, 0
        for node1 in keys:
            for node2 in keys:
                if node2 in self.graph[node1].keys():
                    self.matrix[i][j] = self.graph[node1][node2]
                j += 1
            j = 0
            i += 1


# This code is contributed by
# sanjeev2552
# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize

V = 4


# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path


# next_permutation implementation
def next_permutation(L):
    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = {
              0: {0:0,1:10,2:15,3:20},
              1: {0:10,1:0,2:35,3:25},
              2: {0:15,1:35,2:0,3:30},
              3: {0:20,1:25,2:30,3:0},

             }
    c = convert(graph)
    c.convert_adjlist_to_matrix()
    print(graph)
    print (c.matrix)

    # graph = [[0, 10, 15, 20], [10, 0, 35, 25],
    #          [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(c.matrix, s))


