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
        break
    except:
        print('   Error: base must be an integer greater than 1')
        continue
g = graphSize(n)


# choosing player types

while True:
    try:
        ptb = str(input('Please enter the player type for black (human or AI): '))
        if ptb == "human" or ptb == "AI":
            break
        else:
            print('   Error: player type must be a string reading \"human\" or \"AI\"')
            continue
    except:
        print('   Error: player type must be a string reading \"human\" or \"AI\"')
        continue

while True:
    try:
        ptw = str(input('Please enter the player type for white (human or AI): '))
        if ptw == "human" or ptw == "AI":
            break
        else:
            print('   Error: player type must be a string reading \"human\" or \"AI\"')
            continue
    except:
        print('   Error: player type must be a string reading \"human\" or \"AI\"')
        continue

playertype(ptb, ptw)

# level selecting

if ptb == "AI":
    while True:
        bLevelInput = input('Please enter the difficulty level, 1 to 5, for the black AI (type \"help\" to learn more): ')
        if bLevelInput.isdigit() and 1 <= int(bLevelInput) <= 5:
            bLevel = int(bLevelInput)
            print("   The AI difficulty for black is set to level " + str(bLevel))
            break
        elif bLevelInput.isdigit() and ( int(bLevelInput) < 1 or int(bLevelInput) > 5 ):
            print('   Error: AI level must be an integer between 1 and 5')
            continue
        elif bLevelInput == "help":
            print("   Levels 1 and 2 are easy, levels 3 and 4 are medium, and level 5 is hard. The higher the level, the longer the AI takes to make decisions")
            continue
        else:
            print('   Error: AI level must be an integer between 1 and 5')
            continue
else:
    bLevel = 1   # placeholder level if human

if ptw == "AI":
    while True:
        wLevelInput = input('Please enter the difficulty level, 1 to 5, for the white AI (type \"help\" to learn more): ')
        if wLevelInput.isdigit() and 1 <= int(wLevelInput) <= 5:
            wLevel = int(wLevelInput)
            print("   The AI difficulty for white is set to level " + str(wLevel))
            break
        elif wLevelInput.isdigit() and ( int(wLevelInput) < 1 or int(wLevelInput) > 5 ):
            print('   Error: AI level must be an integer between 1 and 5')
            continue
        elif wLevelInput == "help":
            print("   Levels 1 and 2 are easy, levels 3 and 4 are medium, and level 5 is hard. The higher the level, the longer the AI takes to make decisions")
            continue
        else:
            print('   Error: AI level must be an integer between 1 and 5')
            continue
else:
    wLevel = 1   # placeholder level if human



# node creation
game = gm.Game(g)
game.run(ptb, ptw, bLevel, wLevel)


# gameplay
