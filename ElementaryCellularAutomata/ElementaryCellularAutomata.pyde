SCREEN_WIDTH = 1440
SCREEN_HEIGHT = SCREEN_WIDTH / 2

GEN_SIZE = SCREEN_WIDTH

curGen = [0] * GEN_SIZE
curGen[GEN_SIZE / 2] = 1

automataRuleNum = 77 # THIS IS WHERE YOU CHANGE WHAT YOU WANT
automataRule = [int(i) for i in list(format(automataRuleNum,'b'))]
diff = 8 - len(automataRule)
if diff > 0:
    starting = [0] * diff
    starting.extend(automataRule)
    automataRule = starting

black = color(0,0,0)
white = color(255, 255, 255)

numGens = 0

def setup():
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    frameRate(144)
 
def draw():
    # compute the next generation, the result is stored in curGen
    computeNextGen()
 
    # now we need to copy what's been drawn already, and move it a single pixel upwards
    copy(0, 1, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
 
    # now fill the bottom pixel row with the computed values
    global curGen
    global numGens
    loadPixels()
    for i in range(SCREEN_WIDTH * (SCREEN_HEIGHT - 1), SCREEN_WIDTH * SCREEN_HEIGHT):
        pixels[i] = black if curGen[i % GEN_SIZE] == 1 else white
    updatePixels()

    numGens += 1
    if numGens > (SCREEN_WIDTH / 2) - 1:
        noLoop()
        save("CellularAutomata.png")
    
 
def computeNextGen():
    newGen = [0] * GEN_SIZE
    
    # iterate through the current generation, ignore first and last pixels (they only have a single neighbor)
    global curGen
    for i in range(GEN_SIZE):
        if i == 0:
            newGen[i] = computeCellFromNeighbors(curGen[GEN_SIZE - 1], curGen[i], curGen[i+1])
        elif i == GEN_SIZE - 1:
            newGen[i] = computeCellFromNeighbors(curGen[i-1], curGen[i], curGen[0])
        else:
            newGen[i] = computeCellFromNeighbors(curGen[i-1], curGen[i], curGen[i+1])
 
    curGen = newGen
 
# this isn't done very well but it will do for now        
def computeCellFromNeighbors(left, middle, right):
    triple = (left, middle, right)
    global automataRule
    if (1, 1, 1) == triple: return automataRule[0]
    if (1, 1, 0) == triple: return automataRule[1]
    if (1, 0, 1) == triple: return automataRule[2]
    if (1, 0, 0) == triple: return automataRule[3]
    if (0, 1, 1) == triple: return automataRule[4]
    if (0, 1, 0) == triple: return automataRule[5]
    if (0, 0, 1) == triple: return automataRule[6]
    if (0, 0, 0) == triple: return automataRule[7]
    return 1
