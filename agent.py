import game as gm
import random

class Agent:
    def __init__(self, color, type):
        self.color = color
        self.type = type

        self.decisionFunction = None
        if self.type == "random":
            self.decisionFunction = self.random
        elif self.type == "negamax":
            self.decisionFunction = None # for now


    def random(self, gameState):
        # Pick random move
        pick = random.randint(0, len(gameState.legalMoves) - 1)
        return gameState.nodes[pick]
