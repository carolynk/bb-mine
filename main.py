from graph import Node, Graph
import unittest as ut
import matplotlib.pyplot as plt

class BB:

    def __init__(self, g, m, s, e):
        self.graph = g
        self.min_items = m
        self.start_node = s
        self.end_node = e

    #calculate cost
    def calc_cost(self, v, path_from_start):
        return 0

    def shortestPath(self):
        F = {}
        b = {}
        visited = [] #contains [v,path_from_start,cost]
        while F is not None:
            # select from F the (v,path_from_start) where the cost between s and v is the lowest
            # Expand
            configurations={}
            for state in configurations:
                visited.append(state)
                # calculate cost for v
                c = self.calc_cost(state)
                if visited[v][1] < c :
                    check ="dead end"
                elif v is self.end_node and len(path_from_start) >= self.min_items:
                    check = "solution found"
                else:
                    check = "continue"

                if check is "solution found":
                    if c < b[2]:
                        b = {v, path_from_start, c}
                    else:
                        # discard configuration
                if check is "dead end":
                        # discard configuration

                else:
                    if self.lowerBound(v, path_from_start) <= b[2]:
                        F[v] = [path_from_start, c]
                    else:
                        # discard configuration

        return b

    def lowerBound(self, v, path_from_start):
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

if __name__ == "__main__":
    mine = Graph()