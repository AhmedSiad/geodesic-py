# node class

class Node:
    def __init__(self, key, graph):
        self.id = key
        self.color = "empty"
        self.neighbors = graph[key]
        self.edges = 0b0
        self.parent = self.id