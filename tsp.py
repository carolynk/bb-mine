import math

class convert:
    def __init__(self, g):
        self.graph = g
        self.len = len(self.graph.keys())
        self.matrix = [[0] * (self.len) for i in range(self.len)]

    def convert_adjlist_to_matrix(self):
        keys = self.graph.keys()
        print (keys)
        i ,j =0,0
        for node1 in keys:
            for node2 in keys:
                if node2 in self.graph[node1].keys():

                    self.matrix[i][j] = self.graph[node1][node2]
                j += 1
            j = 0
            i += 1




if __name__ == '__main__':

    graph = {"a": {"b":2,"c":1},
                 "b": {"d":1},
                 "c": {"a":1,"b":1,"d":3,"e":7},
                 "d": {"f":2,"c":3},
                 "e": {"c":7},
                 "f": {"d": 2}
                }
    c = convert(graph)
    c.convert_adjlist_to_matrix()
    print(graph)
    print (c.matrix)
