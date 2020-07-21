import graph as grph

# finding graph size

def graphSize(n):
    if n < 2:
        print('   Error: base must be an integer greater than 1')
    else:
        spaces = int((n ** 2 - n) * (3 / 2))
        print('   Your board of base ' + str(n) + " has " + str(spaces) + " spaces")
        g = graph.generateNSizedGraph(n)


# node class

class Node:
    def __init__(self, key, graph):
        self.id = key
        self.color = "empty"
        self.neighbors = graph[key]

# startup

bList = []
wList = []

print('Welcome to Command Line Y!')
n = int(input('Please enter the base size of the board: '))
graphSize(n)
spaces = int((n ** 2 - n) * (3 / 2))


# node creation

nodeList = [Node(i) for i in range(0, spaces)]

# gameplay

currentMove = "black"
while True:
    if currentMove == "black":
        bMove = int(input('Please enter a black move: '))
        if bList.count(bMove) > 0 or wList.count(bMove) > 0:
            print("   Error: this space is already taken")
            currentMove = "black"
        elif bMove >= spaces or bMove < 0:
            print("   Error: this space does not exist on this board")
            currentMove = "black"
        else:
            bList.append(bMove)
            print('   Black = ' + str(bList))
            print('   White = ' + str(wList))
            nodeList[bMove].color = "black"
            currentMove = "white"
    
    if currentMove == "white":
        wMove = int(input('Please enter a white move: '))
        if bList.count(wMove) > 0 or wList.count(wMove) > 0:
            print("   Error: this space is already taken")
            currentMove = "white"
        elif wMove >= spaces or wMove < 0:
            print("   Error: this space does not exist on this board")
            currentMove = "white"
        else:
            wList.append(wMove)
            print('   Black = ' + str(bList))
            print('   White = ' + str(wList))
            nodeList[wMove].color = "white"
            currentMove = "black"