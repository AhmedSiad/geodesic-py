import node

class Game:
  def __init__(self, graph):
    self.graph = graph
    self.nodes = [Node(i, self.graph) for i in range(len(self.graph))]

    self.groupings = []

    self.bMoves = []
    self.wMoves = []

  def processMove(location, player):
    newStone = self.nodes[location]
    self.groupings.append([newStone])

    if player == "black":
      self.bMoves.append(location)
      newStone.color = "black"
    else:
      self.wMoves.append(location)
      newStone.color = "white"

    for nb in newStone.neighbors
      if nb.color != newStone.color: continue

      nb.parent = newStone.id
      newStone.edges |= nb.edges

      index = self.findIndexOfNode(nb)
      if index != -1:
        self.groupings[-1] += self.groupings[index]
        del self.groupings[index]

  def findIndexOfNode(node):
    for i in range(len(self.groupings)):
      if node in self.groupings[i]: return i
    return -1
