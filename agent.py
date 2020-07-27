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
        elif self.type == "human":
            self.decisionFunction = self.human

    def random(self, gameState):
        # Pick random move
        pick = random.randint(0, len(gameState.legalMoves) - 1)
        pick = gameState.legalMoves[pick]
        return gameState.nodes[pick].id

    def human(self, gameState):
        # Controlled by human
        while True:
            try:
                move = int(input('Please enter a ' + self.color + " move: "))
                if move in gameState.legalMoves:
                    return move
                elif move > len(gameState.nodes) or move < 0:
                    print("   Error: this space does not exist on this board")
                    continue
                else:
                    print("   Error: this space is already taken")
                    continue
            except ValueError:
                print("   Error: please input a positive integer")
                continue
