import graph as grph
import node as nde
import game as gm

# finding graph size

def graphSize(n):
    if n < 2:
        print('   Error: base must be an integer greater than 1')
    else:
        spaces = 3 * (n ** 2 - n) // 2
        print('   Your board of base ' + str(n) + " has " + str(spaces) + " spaces")
        return grph.generateNSizedGraph(n)

# startup

print('Welcome to Command Line Y!')
while True:
    try:
        n = int(input('Please enter the base size of the board: '))
        break
    except:
        print('   Error: base must be an integer greater than 1')
        continue
g = graphSize(n)


# node creation
game = gm.Game(g)
game.run()


# gameplay