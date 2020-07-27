# Game File

import node
import network

class Game:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = [node.Node(i, self.graph) for i in range(len(self.graph))]

        self.groupings = []

        self.bMoves = []
        self.wMoves = []
        self.legalMoves = [i for i in range(len(self.graph))]

        self.bAgent = None
        self.wAgent = None

        self.network = network.Network(self.graph)

    def run(self, ptb, ptw):
        currentMove = "black"

        if ptb == "human":
            self.bAgent = Agent("black", "human")
        else:
            self.bAgent = Agent("black", "random")
        if ptw == "human":
            self.wAgent = Agent("white", "human")
        else:
            self.wAgent = Agent("white", "random")


        while True:
            self.network.draw(self.nodes)

            if currentMove == "black":
                decision = self.bAgent.decisionFunction(self)
                self.processMove(decision, "black")
            else:
                decision = self.wAgent.decisionFunction(self)
                self.processMove(decision, "white")

        # Finish Game
        self.network.draw(self.nodes)
        input("Press any key to close application")

    def processMove(self, location, player):
        newStone = self.nodes[location]
        #self.groupings.append([newStone])  # Creates new set

        if player == "black":
            self.bMoves.append(location)
            newStone.color = "black"
        else:
            self.wMoves.append(location)
            newStone.color = "white"

        self.legalMoves.remove(location)

        for i in newStone.neighbors:
            nb = self.nodes[i]
            if nb.color != newStone.color:
                continue

            nbRoot = self.findRoot(nb)
            nb.parent = newStone.id  # Set parent of neighbor to new stone
            nbRoot.parent = newStone.id
            newStone.edges |= nbRoot.edges  # Bitwise OR to update edges


    def findWinner(self, location):
        # whenever someone plays a new stone
        # either that stone won the game, or it didn't
        # if they won the game, then the group of the new stone will touch all three sides
        # to check who won, just check if the group of the new stone touches all three sides
        if self.nodes[location].edges == 0b111:
            return self.nodes[location].color
        return "none"

    def findRoot(self, node):
        if node.parent != node.id:
            node.parent = self.findRoot(self.nodes[node.parent]).id
        return self.nodes[node.parent]

    def findIndexOfNode(self, node):  # Find which group a node resides in
        for i in range(len(self.groupings)):
            if node in self.groupings[i]:
                return i
        return -1



