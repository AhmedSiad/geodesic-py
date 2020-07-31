import random
from copy import deepcopy

class Node:
    def __init__(self, gameState, color, parent, move):
        self.gameState, self.color = gameState, color
        self.parent = parent
        self.children = []
        self.move = move

        self.wins = 0
        self.trials = 0

    def expand_node(self):
        color = "black"
        if self.color == "black":
            color = "white"
        else:
            color = "black"
        for i in self.gameState.legalMoves:
            state = deepcopy(self.gameState)
            state.processMove(i, self.color)
            nc = Node(self.gameState, color, self, i)
            self.children.append(nc)


    def simulate(self):
        state = deepcopy(self.gameState)
        winner = "none"
        color = self.color
        while winner == "none":
            pick = random.choice(state.legalMoves)
            state.processMove(pick, color)
            color = "white" if color == "black" else "black"
            winner = state.findWinner(pick)
        return winner
