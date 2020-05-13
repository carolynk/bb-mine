import math
import time
import matplotlib.pyplot as plt
import numpy as np
from graph import Graph
from main import Experiments


class convert:
    def __init__(self, g):
        self.graph = g
        self.len = len(self.graph.keys())
        self.matrix = [[0] * (self.len) for i in range(self.len)]

    def convert_adjlist_to_matrix(self):
        keys = self.graph.keys()
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


tspTimer = []
bbTimer =[]


# timer for tsp
def timer(graph, start):
    timer_on = time.time()
    print("cost", travellingSalesmanProblem(graph, start))
    timer_off = time.time()
    tspTimer.append(timer_off - timer_on)


# Driver Code
if __name__ == "__main__":
    sizes = [10,140,190]
    test = Experiments()
    # time for bb
    for size in sizes:
        b = test.size_graph(size)
        time_bb = test.timer(b)
        bbTimer.append(time_bb)

    sizes = [10,140,190]
    # time for tsp
    for size in sizes:
        graph = test.size_graph(size,"graph")
        c = convert(graph)
        c.convert_adjlist_to_matrix()
        timer(c.matrix,int(size/2))

    y = bbTimer
    y2 = tspTimer
    x = sizes
    fig = plt.figure()
    ax = plt.subplot(111)
    ax.plot(x, y2, label='Branch and Bound')
    ax.plot(x, y, label='TSP')
    plt.xlabel('Size')
    plt.ylabel('Runtime')
    plt.title('Branch and Bound vs TSP')
    ax.legend()
    plt.show()
