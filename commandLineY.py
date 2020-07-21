import graph as grph
import node as nde
import game as gm

# finding graph size

def graphSize(n):
    if n < 2:
        print('   Error: base must be an integer greater than 1')
    else:
        spaces = int((n ** 2 - n) * (3 / 2))
        print('   Your board of base ' + str(n) + " has " + str(spaces) + " spaces")
        global g
        g = grph.generateNSizedGraph(n)

# startup

bList = []
wList = []

print('Welcome to Command Line Y!')
n = int(input('Please enter the base size of the board: '))
graphSize(n)
spaces = int((n ** 2 - n) * (3 / 2))


# node creation
game = gm.Game(g)
game.run()


# gameplay