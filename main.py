from graph import Graph
import unittest as ut
import matplotlib.pyplot as plt
import sys
from collections import defaultdict
import time
import numpy as np
import math


class BB:

    def __init__(self, g, m, s, e):
        self.graph = g
        self.min_items = m
        self.start_node = s
        self.end_node = e

    # calculate cost
    def calc_cost(self, path_from_start):
        if path_from_start is not None:
            return self.lower_bound(path_from_start[-1], path_from_start)
        else:
            return 0

    # select from F the (v,path_from_start) where the cost between s and v is the lowest
    def select_v_with_lowest_cost(self, f):
        min_node = None
        min_cost = sys.maxsize
        for node in f.keys():
            if min_cost > f[node][1]:
                min_node = node
                min_cost = f[node][1]
        return min_node

    # expand configuration
    def expand(self, node, f):

        if f[node][0] is None:
            path_from_start = []
        else:
            path_from_start = f[node][0]

        configuration = []
        for neighbour in self.graph[node].keys():
            temp = list.copy(path_from_start)
            if node not in temp:
                temp.insert(0, node)
            if neighbour not in path_from_start:
                temp.append(neighbour)
                configuration.append(temp)
        return configuration

    # return distance of edges in path
    def calculate_distance(self, path):
        distances = []
        for i in range(len(path) - 1):
            distances.append(self.graph[path[i]][path[i + 1]])

        return distances

    def shortest_path(self):
        f = defaultdict(lambda: [])  # contains {v:path_from_start, cost}
        f[self.start_node] = [[], 1.0]
        b = ["", [], sys.maxsize]  # [lastNode, path_from_start,cost]}
        visited = defaultdict(lambda: [])  # contains {v:[path_from_start, cost]}
        while f is not None:
            # print("f====",f)
            # select from f the (v,path_from_start) where the cost between s and v is the lowest
            min_v = self.select_v_with_lowest_cost(f)
            # print(min_v)
            # Expand
            configurations = self.expand(min_v, f)
            # print(configurations)
            # if we arrived to dead end
            if not configurations:
                del f[min_v]

            for path_from_start in configurations:
                last_node_in_path_from_start = path_from_start[-1]
                # check if this node visited before or not
                if min_v not in visited.keys():
                    visited[min_v] = []
                    visited[min_v].append(f[min_v][0])  # add path_from_start
                    visited[min_v].append(f[min_v][1])  # add cost
                    # print("visited", visited)

                # delete it because we dont want it to expand again
                if min_v in f.keys():
                    del f[min_v]
                # calculate cost for v
                c = self.calc_cost(path_from_start)

                if visited[last_node_in_path_from_start] != [] and visited[last_node_in_path_from_start][1] < c:
                    # print("visit cost ,", last_node_in_path_from_start, " ", visited[last_node_in_path_from_start][1])
                    check = "dead end"
                elif last_node_in_path_from_start is self.end_node and len(path_from_start) >= self.min_items:
                    check = "solution found"
                else:
                    check = "continue"
                    # update the node
                    # visited[last_node_in_path_from_start] = [path_from_start,c]
                # print(path_from_start)

                if check == "solution found":
                    # print("check", check)
                    # if c < b[2]:
                    #     b = [last_node_in_path_from_start, path_from_start, c]
                    # F = None
                    return path_from_start
                elif check == "dead end":
                    # discard configuration
                    configurations.remove(path_from_start)
                else:
                    # print("lower bound",self.lowerBound(last_node_in_path_from_start, path_from_start))
                    if self.lower_bound(last_node_in_path_from_start, path_from_start) < b[2]:
                        cost = self.lower_bound(last_node_in_path_from_start, path_from_start)
                        # if last_node_in_path_from_start not in F.keys():
                        f[last_node_in_path_from_start] = [path_from_start, cost]
                # print ("==================================================")
        return b

    def lower_bound(self, v, path_from_start):
        all_edge_weights = self.calculate_distance(path_from_start)
        total_distance = sum(all_edge_weights)
        items = len(path_from_start)
        cost = total_distance / items
        return cost


class Experiments:
    def __init__(self):
        self.totalTime = []

    def test_tiny_graph(self, min):
        g2 = Graph()
        g2.add_edge_undirected("a", "b", 3)
        g2.add_edge_undirected("a", "c", 5)
        g2.add_edge_undirected("b", "d", 1)
        g2.add_edge_undirected("b", "e", 3)
        g2.add_edge_undirected("c", "a", 5)
        g2.add_edge_undirected("c", "e", 3)
        g2.add_edge_undirected("d", "f", 2)
        g2.add_edge_undirected("d", "e", 1)
        g2.add_edge_undirected("d", "b", 1)
        g2.add_edge_undirected("e", "c", 3)
        g2.add_edge_undirected("e", "b", 2)
        g2.add_edge_undirected("e", "d", 1)
        g2.add_edge_undirected("e", "f", 4)
        g2.add_edge_undirected("f", "g", 1)
        g2.add_edge_undirected("g", "f", 1)

        g2.create_adjacency_list()
        # value = {k: g2.adjacency_list[k] for k in set(g2.adjacency_list) }
        # print(graph2)
        # print(g2.adjacency_list)
        # print(g2.adjacency_list == graph2)
        start = "a"
        end = "g"
        # print(type(g2.adjacency_list))
        # g3 = dict.copy(g2.adjacency_list)
        # b = BB(graph2, min, start, end)
        # print("graph",b.shortestPath())
        b = BB(g2.adjacency_list, min, start, end)
        return b
        # print("adjacency_list", b.shortestPath())

    def trials(self, n):
        """ Takes number of trials and expierment"""
        for i in range(1, n):
            self.test_tiny_graph(2)

    def timer(self, bb):
        """
        Time analysis

        Takes in a bb object, and calculates the time to run
        the shortest path on it once

        :type bb: BB
        :param bb:
        :return: float
        """
        timer_on = time.time()
        bb.shortest_path()
        timer_off = time.time()
        self.totalTime.append(timer_off - timer_on)
        timer_off = time.time()

        return timer_off - timer_on

    def plot_by_min(self, mins, t):
        """
        :param mins: List
            list of mins
        :param t: int
            num of trials
        :return: None, but prints plots
        """

        all_data = []
        for min_ in mins:
            runtimes = []
            for i in range(0, t):
                b = self.test_tiny_graph(min_)
                runtimes.append(self.timer(b))
            all_data.append(runtimes)
        means = []
        sd = []
        for x in all_data:
            means.append(sum(x) / t)
            sd.append(np.std(x))  # get standard deviations

        plt.errorbar(mins, means, sd, linestyle='-', marker='^')
        plt.xlabel('Min')
        plt.ylabel('Runtime')
        plt.title('BB')

        # plt.legend()
        plt.show()


class BBTests(ut.TestCase):
    def test(self):
        pass


def main():
    graph = {"a": {"b": 2, "c": 1},
             "b": {"d": 1},
             "c": {"a": 1, "b": 1, "d": 3, "e": 7},
             "d": {"f": 2, "c": 3},
             "e": {"c": 7},
             "f": {"d": 2}
             }
    min_ = 4
    start = "a"
    end = "f"

    bb = BB(graph, min_, start, end)
    get_time = Experiments()
    get_time.timer(bb)
    # print(bb.shortestPath())
    # print("Time", get_time.totalTime)
    test = Experiments()

    test.trials(10)
    test.plot_by_min([1, 2, 3, 4], 10)


if __name__ == "__main__":
    main()
    num_of_nodes = 3
    num_of_edges = int(num_of_nodes * math.log(num_of_nodes, 2))
