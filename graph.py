import unittest as ut
import random
import math


class Node:
    """
    A class used to represent a Node

    ...

    Attributes
    ----------
    id: int
        value contained in the node
    edges : [node]
        set of nodes connected by an edge
    """

    def __init__(self, id_):
        self.id = id_
        self.edges = {}

    # adds a neighbor node id
    def add_neighbor(self, nid, w):
        self.edges[nid] = w

    def has_neighbor(self, nid):
      return nid in self.edges.keys()

    def get_weight(self):
        pass


class Graph:
    """
    A class used to represent an Graph

    ...

    Attributes
    ----------
    adjlist : dictionary
        a dictionary of ids : nodes in the graph

    Methods
    -------
    add_node(id: int)
        Adds a node by ID
    get_node(id: int)
        Gets a node by ID
    add_edge(id1: int, id2: int)
        Takes 2 node ids and adds a directed edge
    add_edge_undirected(id: int, id: int)
        Takes 2 node ids and adds an undirected edge
    get_neighbors(self, id):

    get_all_neighbors(nodes: list of nodes)
        Returns a list of nodes
        List contains all neighbors of every node passed in

    """

    def __init__(self, nodes=None):
        """
        :type nodes: dictionary

        """
        if nodes is None:
            nodes = {}
        self.adjlist = nodes


    # Adds a node by id
    def add_node(self, id_):
        new_node = Node(id_)
        self.adjlist[id_] = (new_node)

    # Gets a node by id
    def get_node(self, id_):
        """ Gets a node by id """
        if id_ in self.adjlist.keys():
            return self.adjlist[id_]
        return None

    def add_edge(self, fr, to, w):
        """
        Adds a directed edge
        """
        if self.get_node(fr) is None:
            self.add_node(fr)
        if self.get_node(to) is None:
            self.add_node(to)
        self.get_node(fr).add_neighbor(to, w)

    def add_edge_undirected(self, id1, id2, w):
        self.add_edge(id1, id2, w)
        self.add_edge(id2, id1, w)

    def get_neighbors(self, id_):
        return self.get_node(id_).edges

    def edge_exists(self, id1, id2):
        if (self.get_node(id1) is None) or (self.get_node(id2) is None):
            return False
        else:
            return self.get_node(id1).has_neighbor(id2)

    def generate_graph(self, n, m, maxw):
        """ Generate an Erdős–Rényi random graph of n nodes, and m edges """

        for i in range(1, n + 1):
            self.add_node(i)

        for i in range(1, m + 1):
            w = random.randint(1, maxw)

        for i in range(1, m + 1):
            id1 = random.randint(1, n)
            id2 = random.randint(1, n)
            while id1 == id2 or self.edge_exists(id1, id2):
                redo = random.randint(1, 2)
                if redo == 1:
                    id1 = random.randint(1, n)
                else:
                    id2 = random.randint(1, n)
            self.add_edge_undirected(id1, id2, w)
        return self


class GraphTest(ut.TestCase):
    """ Test methods for Graph """

    def test_tiny_graph(self):
        g = Graph()
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        # undirected
        g.add_edge_undirected(1, 2, 17)
        g.add_edge_undirected(1, 3, 34)

        self.assertEqual(g.edge_exists(1, 2), True)
        self.assertEqual(g.edge_exists(2, 1), True)
        self.assertEqual(g.edge_exists(3, 2), False)
        self.assertEqual(g.get_neighbors(1), {2: 17, 3: 34})
        self.assertEqual(g.get_neighbors(2), {1: 17})

    def test_random_graph(self, n, m):
        """ Test methods for a random graph """

        g_rand = Graph()
        g_rand.generate_graph(n, m, 50)


if __name__ == '__main__':
    gt = GraphTest()
    gt.test_tiny_graph()

    # Random Graph Test
    num_of_nodes = 10
    num_of_edges = int(math.log(num_of_nodes, 2))
    gt.test_random_graph(num_of_nodes, num_of_edges)

    print("All tests passed")
