import heapq as H
from typing import List, Dict, Set, Tuple

SEPARATOR: str = "\t"
MAXINT: int = 10**6


class Graph:
    def __init__(self, n: int, mat: List[List[int]], src: int = 0):
        """
        Create the adjacency list for the given matrix
        :param n: no of nodes
        :param mat: given matrix (m x 3)
        Values initialized:
        adj_list: adjacency list storing nbr info in a map
        S: set of vertices for which minimum distance has already been found
        Q: min-priority queue keyed by their shortest-path estimate values
        D: shortest-path estimate values for each vertex
        retrace: predecessor of the vertex in the shortest-path estimate
        """
        self.adj_list: List[Dict[int, int]] = [{} for _ in range(n)]
        self.adj_list_creator(mat)
        self.S: Set[int] = set()
        self.Q: List[Tuple[int, int]] = []
        self.src: int = src
        self.D: List[int] = [MAXINT] * n
        self.retrace: List[int] = [-1] * n

    def adj_list_creator(self, mat: List[List[int]]):
        """
        Creates the adjacency map for given matrix in the format:
        [{vertex: weight, vertex: weight, vertex: weight}, {vertex: weight, vertex: weight, ...}, ...]
        where the index is the vertex and the list at that index has the neighbor vertices with respective weights.
        :param mat: given matrix (m x 3)
        """
        for i in range(len(mat)):
            v1, v2, w = mat[i]
            self.adj_list[v1][v2] = w
            self.adj_list[v2][v1] = w

    def wt(self, u: int, v: int) -> int:
        """
        Returns the weight from vertex u to v
        :param u: Vertex u
        :param v: Vertex v
        :return: weight
        """
        return self.adj_list[u][v]

    def relax(self, v: int, u: int):
        """
        Relaxes the vertex v if there exists another vertex u which provides lesser cumulative weight than the existing
        Also sets the retrace list to the corresponding vertex to trace the previous vertex which would lead all the
        way back to the source.
        :param v: destination vertex
        :param u: intermediate vertex
        """
        if self.D[v] > self.D[u] + self.wt(u, v):
            self.D[v] = self.D[u] + self.wt(u, v)
            # new shortest path estimate would be the sum of
            # weights of path from source -> u and u -> u
            self.retrace[v] = u
            H.heappush(self.Q, (self.D[v], v,))

    def Dijkstra(self):
        """
        Iterative approach for Dijkstra's Algorithm
        """
        initial_wt = 0    # Since there would be no self loops (given)
        H.heappush(self.Q, (initial_wt, self.src,))
        self.D[self.src] = initial_wt
        while self.Q:
            wt, curr_vertex = H.heappop(self.Q)
            if curr_vertex not in self.S:
                for nbr in self.adj_list[curr_vertex].keys():
                    if nbr not in self.S:
                        self.relax(nbr, curr_vertex)
                self.S.add(curr_vertex)


A = 6
B = [
    [0, 4, 9],
    [3, 4, 6],
    [1, 2, 1],
    [2, 5, 1],
    [2, 4, 5],
    [0, 3, 7],
    [0, 1, 1],
    [4, 5, 7],
    [0, 5, 1]
]
C = 0
G = Graph(A, B, C)
print("Adjacency map: {}".format(G.adj_list))
G.Dijkstra()
print("DIJKSTRA:")
for vertex, level in enumerate(G.D):
    print("{}NODE-> {} SHORTEST DISTANCE-> {}".format(SEPARATOR, vertex, level if level!=MAXINT else "Not Connected"))

for vertex, predecessor in enumerate(G.retrace):
    if vertex == C:
        print("{} is the source".format(C))
    elif predecessor == -1:
        print("{} is not connected to the source".format(vertex))
    else:
        print("{} leads to {}".format(predecessor, vertex))

A = 6
B = [
    [3, 4, 6],
    [1, 2, 1],
    [2, 5, 1],
    [0, 1, 1],
    [0, 5, 1]
]
# C = 0
G = Graph(A, B, C)
print("Adjacency map: {}".format(G.adj_list))
G.Dijkstra()
print("DIJKSTRA:")
for vertex, level in enumerate(G.D):
    print("{}NODE-> {} SHORTEST DISTANCE-> {}".format(SEPARATOR, vertex, level if level!=MAXINT else "Not Connected"))

for vertex, predecessor in enumerate(G.retrace):
    if vertex == C:
        print("{} is the source".format(C))
    elif predecessor == -1:
        print("{} is not connected to the source".format(vertex))
    else:
        print("{} leads to {}".format(predecessor, vertex))
