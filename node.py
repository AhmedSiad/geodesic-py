# node class
from graph import getEdge
import math

class Node:
    def __init__(self, key, graph):
        self.id = key
        self.color = "empty"
        self.neighbors = graph[key]
        self.parent = self.id

        N = int((1/6) * (math.sqrt(24 * len(graph) + 9) + 3)) # Find N value, base size
        self.edges = getEdge(self.id, N)
