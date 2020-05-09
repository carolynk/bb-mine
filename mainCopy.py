# TODO: the problem is when the best cost is less than the current and the best already expanded
# it will keep choosing the same node to expand

from graph import Node, Graph
import unittest as ut
import matplotlib.pyplot as plt
import sys
from collections import defaultdict
import time
class BB:

    def __init__(self, g, m, s, e):
        self.graph = g
        self.min_items = m
        self.start_node = s
        self.end_node = e

    # calculate cost
    def calc_cost(self,path_from_start):
        if path_from_start is not None:
            return self.lowerBound(path_from_start[-1],path_from_start)
        else:
            return 0

    # select from F the (v,path_from_start) where the cost between s and v is the lowest
    def select_v_with_lowest_cost(self,f):
        minNode = None
        minCost = sys.maxsize
        for node in f.keys():
            if minCost > f[node][1]:
                minNode = node
                minCost = f[node][1]


        return minNode


    # expand configuration
    def expand(self,node,f):

        if f[node][0] is None:
            pathFromStart = [a]
        else:
            pathFromStart = f[node][0]

        configration =[]
        for neighbour in self.graph[node].keys():
            temp = list.copy(pathFromStart)
            if node not in temp:
                temp.insert(0,node)
            if neighbour not in pathFromStart :
                temp.append(neighbour)
                configration.append(temp)
        return configration

    # return distance of edges in path
    def calculateDistane(self,path):
        distances =[]
        for i in range(len(path)-1):
            distances.append(self.graph[path[i]][path[i+1]])

        return distances






    def shortestPath(self):
        F = defaultdict(lambda :[]) #contains {v:path_from_start,cost}
        F[self.start_node] = [[],1.0]
        b = ["",[],sys.maxsize] # [lastNode,pathFromStart,cost]}
        visited = defaultdict(lambda :[]) #contains {v:[path_from_start,cost]}
        while F is not None:
            # select from F the (v,path_from_start) where the cost between s and v is the lowest
            minv = self.select_v_with_lowest_cost(F)

            # Expand
            configurations=self.expand(minv,F)
            # if we arrived to dead end
            if not configurations:
                F[minv][1]= sys.maxsize

            for pathFromStart in configurations:
                lastNodeInpathFromStart = pathFromStart[-1]
                # check if this node visited before or not
                if minv not in visited.keys():
                    visited[minv] = []
                    visited[minv].append(F[minv][0])  # add pathFromStart
                    visited[minv].append(F[minv][1])  # add cost

                    # print("visited", visited)

                # delete it became  dont want it to expand again
                if minv in F.keys():
                    del F[minv]
                # calculate cost for v
                c = self.calc_cost(pathFromStart)

                if visited[lastNodeInpathFromStart] != [] and visited[lastNodeInpathFromStart][1] < c :
                    # print("visit cost ,",lastNodeInpathFromStart," ",visited[lastNodeInpathFromStart][1])
                    check = "dead end"
                elif lastNodeInpathFromStart is self.end_node and len(pathFromStart) >= self.min_items:
                    check = "solution found"
                else:
                    check = "continue"
                    # update the node
                    visited[lastNodeInpathFromStart] = [pathFromStart,c]


                if check == "solution found":
                    print("check", check)
                    if c < b[2]:
                        b = [lastNodeInpathFromStart, pathFromStart, c]
                    F =None
                    return pathFromStart
                elif check == "dead end":
                    # discard configuration
                    configurations.remove(pathFromStart)


                else:
                    # print("lower bound",self.lowerBound(lastNodeInpathFromStart, pathFromStart))
                    if self.lowerBound(lastNodeInpathFromStart, pathFromStart) < b[2] :
                        cost = self.lowerBound(lastNodeInpathFromStart, pathFromStart)
                        F[lastNodeInpathFromStart]= [pathFromStart, cost]

                # print ("==================================================")

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

def main():
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
    print(bb.shortestPath())

if __name__ == "__main__":
  main()