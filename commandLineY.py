import graph as grph
import node as nde
import game as gm

# finding graph size

def graphSize(n):
    spaces = 3 * (n ** 2 - n) // 2
    print('   Your board of base ' + str(n) + " has " + str(spaces) + " spaces")
    return grph.generateNSizedGraph(n)

# human or AI

def playertype(ptb, ptw):
    if ptb == "human":
        ptbString = "a human"
    else:
        ptbString = "an AI"
    if ptw == "human":
        ptwString = "a human"
    else:
        ptwString = "an AI"
    print("   Black is controlled by " + ptbString + " and white is controlled by " + ptwString)

# startup

print('Welcome to Command Line Y!')
while True:
    try:
        n = int(input('Please enter the base size of the board: '))
        if n >= 2:
            break
        if n < 2:
            print('   Error: base must be an integer greater than 1')
    except:
        print('   Error: base must be an integer greater than 1')
g = graphSize(n)


# choosing player types

while True:
    try:
        ptb = str(input('Please enter the player type for black (human or AI): '))
        if ptb == "human" or ptb == "AI":
            break
        else:
            print('   Error: player type must be a string reading \"human\" or \"AI\"')
    except:
        print('   Error: player type must be a string reading \"human\" or \"AI\"')

while True:
    try:
        ptw = str(input('Please enter the player type for white (human or AI): '))
        if ptw == "human" or ptw == "AI":
            break
        else:
            print('   Error: player type must be a string reading \"human\" or \"AI\"')
    except:
        print('   Error: player type must be a string reading \"human\" or \"AI\"')

playertype(ptb, ptw)

# AI type selecting

if ptb == "AI":
    while True:
        try:
            bTypeInput = str(input('Please enter the type of AI for black — random, negamax, or montecarlo (type \"help\" to learn more): '))
            if bTypeInput == "random":
                ptb = "random"
                print("   Black is controlled by a random AI")
                break
            elif bTypeInput == "negamax":
                ptb = "negamax"
                print("   Black is controlled by a negamax AI")
                break
            elif bTypeInput == "montecarlo":
                ptb = "montecarlo"
                print("   Black is controlled by a montecarlo tree search AI")
                break
            elif bTypeInput == "help":
                print("   The random AI makes its moves randomly. The negamax AI makes its moves based on what it evaluates as the best. The montecarlo AI is a learned tree search that makes its moves based on previous winning moves")
            else:
                print('   Error: AI type must be \"random,\" \"negamax,\" or \"montecarlo\"')
        except:
            print('   Error: AI type must be a string reading \"random,\" \"negamax,\" or \"montecarlo\"')

if ptw == "AI":
    while True:
        try:
            wTypeInput = str(input('Please enter the type of AI for white — random, negamax, or montecarlo (type \"help\" to learn more): '))
            if wTypeInput == "random":
                ptw = "random"
                print("   White is controlled by a random AI")
                break
            elif wTypeInput == "negamax":
                ptw = "negamax"
                print("   White is controlled by a negamax AI")
                break
            elif wTypeInput == "montecarlo":
                ptw = "montecarlo"
                print("   White is controlled by a montecarlo tree search AI")
                break
            elif wTypeInput == "help":
                print("   The random AI makes its moves randomly. The negamax AI makes its moves based on what it evaluates as the best. The montecarlo AI is a learned tree search that makes its moves based on previous winning moves")
            else:
                print('   Error: AI type must be \"random,\" \"negamax,\" or \"montecarlo\"')
        except:
            print('   Error: AI type must be a string reading \"random,\" \"negamax,\" or \"montecarlo\"')


# level selecting for negamax

if ptb == "negamax":
    while True:
        bLevelInput = input('Please enter the difficulty level, 1 to 5, for the black AI (type \"help\" to learn more): ')
        if bLevelInput.isdigit() and 1 <= int(bLevelInput) <= 5:
            bLevel = int(bLevelInput)
            print("   The AI difficulty for black is set to level " + str(bLevel))
            break
        elif bLevelInput.isdigit() and ( int(bLevelInput) < 1 or int(bLevelInput) > 5 ):
            print('   Error: AI level must be an integer between 1 and 5')
        elif bLevelInput == "help":
            print("   Levels 1 and 2 are easy, levels 3 and 4 are medium, and level 5 is hard. The higher the level, the longer the AI takes to make decisions")
        else:
            print('   Error: AI level must be an integer between 1 and 5')
else:
    bLevel = 1   # placeholder level if human

if ptw == "negamax":
    while True:
        wLevelInput = input('Please enter the difficulty level, 1 to 5, for the white AI (type \"help\" to learn more): ')
        if wLevelInput.isdigit() and 1 <= int(wLevelInput) <= 5:
            wLevel = int(wLevelInput)
            print("   The AI difficulty for white is set to level " + str(wLevel))
            break
        elif wLevelInput.isdigit() and ( int(wLevelInput) < 1 or int(wLevelInput) > 5 ):
            print('   Error: AI level must be an integer between 1 and 5')
        elif wLevelInput == "help":
            print("   Levels 1 and 2 are easy, levels 3 and 4 are medium, and level 5 is hard. The higher the level, the longer the AI takes to make decisions")
        else:
            print('   Error: AI level must be an integer between 1 and 5')
else:
    wLevel = 1   # placeholder level if human



# node creation
game = gm.Game(g)
game.run(ptb, ptw, bLevel, wLevel)


# gameplay
