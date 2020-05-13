import unittest as ut
import random
import math
from scipy.special import comb


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

    def add_neighbor(self, nid, w):
        """ adds a neighbor node id """
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
    adjacency_list : dictionary
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
        self.nodes = nodes
        self.adjacency_list = {}

    def add_node(self, id_):
        """ Adds nodes by id """
        new_node = Node(id_)
        self.nodes[id_] = new_node

    def get_node(self, id_):
        """ Gets a node by id """
        if id_ in self.nodes.keys():
            return self.nodes[id_]
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

    def get_density(self):
        """ Calculate the density of a graph
        density = (actual number of edges)/(possible number of edges)
        possible number of edges = number of nodes choose 2

        returns: float
            density
        """
        possible_edges = comb(len(self.adjacency_list), 2, exact=True, repetition=False)
        # get actual number of edges
        edges = (sum([len(self.adjacency_list[x]) for x in self.adjacency_list])) / 2
        density = edges / possible_edges
        return density

    def generate_connected_graph(self, n, m, max_w):
        """ Generate an Erdős–Rényi random graph of n nodes, and m edges """
        if m < n - 1:
            print("m should be at at least n-1")
        max_edges = comb(n, 2, exact=True, repetition=False)
        if m > max_edges:
            print("too many edges")
        # add the first node
        self.add_node(1)

        for i in range(2, n + 1):
            self.add_node(i)
            # randomly choose an existing node to attach to
            nid = random.randint(1, i - 1)
            # choose a random weight between 1 and max_w
            w = random.randint(1, max_w)
            # create edge between node i and node(1... i = 1)

            self.add_edge_undirected(i, nid, w)

            current_num_nodes = n
        if m > n:
            for i in range(n, m + 1):
                # id2 = random.randint(1, current_num_nodes)
                w = random.randint(1, max_w)
                # checks
                needs_redo = True
                id1 = random.randint(1, n)
                id2 = random.randint(1, n)
                while needs_redo:
                    choose_redo = random.randint(1, 2)
                    if choose_redo == 1:
                        id1 = random.randint(1, n)
                    else:
                        id2 = random.randint(1, n)
                    if id1 == id2:
                        needs_redo = True
                    elif self.edge_exists(id1, id2):
                        needs_redo = True
                    else:
                        needs_redo = False
                self.add_edge_undirected(id1, id2, w)

    def create_adjacency_list(self):
        for id_ in self.nodes:
            self.adjacency_list[id_] = self.get_node(id_).edges
        # delete nodes with no connections
        for x in list(self.adjacency_list.keys()):
            if not self.adjacency_list[x]:
                del self.adjacency_list[x]


class GraphTest(ut.TestCase):
    """ Test methods for Graph """

    def test_tiny_graph(self):
        g = Graph()
        # undirected
        g.add_edge_undirected(1, 2, 17)
        g.add_edge_undirected(1, 3, 34)

        self.assertEqual(g.edge_exists(1, 2), True)
        self.assertEqual(g.edge_exists(2, 1), True)
        self.assertEqual(g.edge_exists(3, 2), False)
        self.assertEqual(g.get_neighbors(1), {2: 17, 3: 34})
        self.assertEqual(g.get_neighbors(2), {1: 17})
        g.create_adjacency_list()
        self.assertEqual(g.get_density(), 2 / 3)

        g.create_adjacency_list()
        self.assertEqual(g.adjacency_list, {1: {2: 17, 3: 34}, 2: {1: 17}, 3: {1: 34}})

        edge_num = int((sum([len(g.adjacency_list[x]) for x in g.adjacency_list])) / 2)
        self.assertEqual(edge_num, 2)

    def test_random_graph(self, n, m):
        """ Test methods for a random graph """

        g_rand = Graph()
        g_rand.generate_connected_graph(n, m, 50)
        g_rand.create_adjacency_list()
        print("adj list", g_rand.adjacency_list)
        print("n num of nodes", len(g_rand.adjacency_list))
        self.assertEqual(len(g_rand.adjacency_list), n)

        # self.assertEqual(len(g_rand.edges), m)
        edge_num = int((sum([len(g_rand.adjacency_list[x]) for x in g_rand.adjacency_list])) / 2)
        self.assertEqual(edge_num, m)


if __name__ == '__main__':
    gt = GraphTest()
    gt.test_tiny_graph()

    # Random Graph Test
    num_of_nodes = 5
    num_of_edges = 10
    # num_of_edges = int(math.log(num_of_nodes, 2)/2)
    gt.test_random_graph(num_of_nodes, num_of_edges)

    g5 = Graph()
    g5.generate_connected_graph(num_of_nodes, num_of_edges, 50)
    g5.create_adjacency_list()
    print(g5.adjacency_list)
    print("density", g5.get_density())
    print("All tests passed")
