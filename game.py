# Game File

import node


class Game:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = [node.Node(i, self.graph) for i in range(len(self.graph))]

        self.groupings = []

        self.bMoves = []
        self.wMoves = []

    def run(self):
        currentMove = "black"
        while True:
            winner = self.findWinner()
            if winner != "none":
                print(winner + " has won the game!")
                break

            if currentMove == "black":
                try:
                    bMove = int(input('Please enter a black move: '))
                    if self.bMoves.count(bMove) > 0 or self.wMoves.count(bMove) > 0:
                        print("   Error: this space is already taken")
                        currentMove = "black"
                    elif bMove >= len(self.nodes) or bMove < 0:
                        print("   Error: this space does not exist on this board")
                        currentMove = "black"
                    else:
                        self.processMove(bMove, "black")
                        print('   Black = ' + str(self.bMoves))
                        print('   White = ' + str(self.wMoves))
                        self.nodes[bMove].color = "black"
                        currentMove = "white"
                except ValueError:
                    print("   Error: please input an integer")
                    currentMove = "black"

            if currentMove == "white":
                try:
                    wMove = int(input('Please enter a white move: '))
                    if self.bMoves.count(wMove) > 0 or self.wMoves.count(wMove) > 0:
                        print("   Error: this space is already taken")
                        currentMove = "white"
                    elif wMove >= len(self.nodes) or wMove < 0:
                        print("   Error: this space does not exist on this board")
                        currentMove = "white"
                    else:
                        self.processMove(wMove, "white")
                        print('   Black = ' + str(self.bMoves))
                        print('   White = ' + str(self.wMoves))
                        self.nodes[wMove].color = "white"
                        currentMove = "black"
                except ValueError:
                    print("   Error: please input an integer")
                    currentMove = "white"

    def processMove(self, location, player):
        newStone = self.nodes[location]
        self.groupings.append([newStone])  # Creates new set

        if player == "black":
            self.bMoves.append(location)
            newStone.color = "black"
        else:
            self.wMoves.append(location)
            newStone.color = "white"

        for i in newStone.neighbors:
            nb = self.nodes[i]
            if nb.color != newStone.color:
                continue

            nb.parent = newStone.id  # Set parent of neighbor to new stone
            newStone.edges |= nb.edges  # Bitwise OR to update edges

            indexNb = self.findIndexOfNode(nb)
            indexS = self.findIndexOfNode(newStone)
            if indexNb != -1 and indexS != indexNb:
                # Merge two sets if they are neighbors
                self.groupings[-1] += self.groupings[indexNb]
                del self.groupings[indexNb]  # Get rid of old set

    def findWinner(self):
        for group in self.groupings:
            current = group[0]
            while current.parent != current.id:
                current = self.nodes[current.parent]  # Find the top parent
            if current.edges == 0b111:  # Win condition
                return current.color
        return "none"

    def findIndexOfNode(self, node):  # Find which group a node resides in
        for i in range(len(self.groupings)):
            if node in self.groupings[i]:
                return i
        return -1



