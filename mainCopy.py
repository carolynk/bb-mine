from graph import Node, Graph
import unittest as ut
import matplotlib.pyplot as plt

class BB:

    def __init__(self, g, m, s, e):
        self.graph = g
        self.min_items = m
        self.start_node = s
        self.end_node = e

    # calculate cost
    def calc_cost(self, v, path_from_start):
        return 0

    # select from F the (v,path_from_start) where the cost between s and v is the lowest
    def select_v_with_lowest_cost(self,f):
        minCost =0
        for node in f.keys():
            if minCost < f[node][1]:
                minNode = node

        return minNode


    # expand configuration
    def expand(self,node,f):
        bathFromStart = f[node]
        configration =[]
        for neighbour in self.graph[node].keys():
            configration.append(list.copy(bathFromStart).append(neighbour))

        return configration

    # return distance of edges in path
    def calculateDistane(self,path):
        distances =[]
        for i in len(path):
            distances.append(self.graph[path[i]][path[i+1]])

        return distances






    def shortestPath(self):
        F = {self.start_node:[[],0]} #contains {v:path_from_start,cost}
        b = {}
        visited = {} #contains {v:[path_from_start,cost]}
        while F is not None:
            # select from F the (v,path_from_start) where the cost between s and v is the lowest
            minv = self.select_v_with_lowest_cost(f)
            # check if this node visited before or not

            # Expand
            configurations=self.expand(minv,F)
            if minv not in visited[minv]:
                visited[minv]=[]
                visited[minv].append(F[minv][0]) # add bathFromStart
                visited[minv].append(F[minv][1]) # add cost

            for bathFromStart in configurations:
                # calculate cost for v
                c = self.calc_cost(bathFromStart)
                lastNodeInBathFromStart = bathFromStart[-1]
                if visited[lastNodeInBathFromStart][1] < c :
                    check ="dead end"
                elif lastNodeInBathFromStart is self.end_node and len(path_from_start) >= self.min_items:
                    check = "solution found"
                else:
                    check = "continue"

                if check is "solution found":
                    if c < b[2]:
                        b = {bathFromStart[-1], path_from_start, c}
                    else:
                        # discard configuration
                if check is "dead end":
                        # discard configuration

                else:
                    if self.lowerBound(lastNodeInBathFromStart, path_from_start) <= b[2]:
                        F[lastNodeInBathFromStart] = [path_from_start, c]
                    else:
                        # discard configuration

        return b

    def lowerBound(self, v, path_from_start):
        all_edge_weights = self.calculateDistane(path_from_start)
        total_distance = sum(all_edge_weights)
        items = len(path_from_start)
        cost = total_distance/items
        return cost

class Experiments:
    def exp(self):
        pass

    def createSamples(self, size):
        pass

    # function to do the time analysis
    def timer(self, sample_set):
        timer_on = time.time()
        # calculate shortest path for sample set

        timer_off = time.time()
        return timer_off - timer_on

    # function to plot
    def plotting(x, y, title, x_axis, y_axis):
        # setup the plot
        plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)

        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(title)
        plt.show()

class BBTest(ut.TestCase):
    def test(self):
        pass

def main:
    graph = {"a": {"b":2,"c":1},
             "b": {"d":1},
             "c": {"a":1,"b":1,"d":3,"e":7},
             "d": {"f":2,"c":3},
             "e": {"c":7}
            }
    min = 4
    start = "a"
    end = "f"
    bb = BB(graph, min, start, end)
    bb.shortestPath()

if __name__ == "__main__":
  main()