import game as gm
import random
import math
from copy import deepcopy

class Agent:
    def __init__(self, color, type):
        self.color = color
        self.type = type

        self.decisionFunction = None
        if self.type == "random":
            self.decisionFunction = self.minimax
        elif self.type == "negamax":
            self.decisionFunction = None # for now
        elif self.type == "human":
            self.decisionFunction = self.human

        self.maxDepth = 2

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

    def minimax(self, gameState):
        bestMove = self.negamax(gameState, self.maxDepth, self.color, None)
        return bestMove
    def negamax(self, gameState, depth, color, move):
        if move != None:
            initialVal = self.evaluateGameState(gameState, color, move)
            if math.isinf(initialVal) or depth == 0:
                return initialVal

        value = -math.inf
        bestMove = gameState.legalMoves[0]
        for i in gameState.legalMoves:
            currentGameState = deepcopy(gameState)
            currentGameState.processMove(i, color)

            oppositeColor = "white" if color == "black" else "black"
            oppositeVal = self.negamax(currentGameState, depth - 1, oppositeColor, i)
            childVal = -oppositeVal
            bestMove = i if childVal > value else bestMove
            value = max(value, childVal)
        if depth == self.maxDepth:
            return bestMove
        return value

    def evaluateGameState(self, gameState, color, move):
        winner = gameState.findWinner(move)
        if winner == color:
            return math.inf
        elif winner == "none":
            score = 0
            for i in gameState.nodes:
                if i.color == color and i.parent == i.id:
                    children = filter(lambda x: x.parent == i.id, gameState.nodes)
                    score += len(list(children))
            return score
        return -math.inf
