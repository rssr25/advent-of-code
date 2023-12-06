#addx and noop
from utils import getData


def getInterestingSignalStrengths(cycle, register):
    global interestingSignals
    interestingSignals.append(cycle * register)

def updateSprite(register, sprite):
    sprite[register] = '#'
    sprite[register-1] = '#'
    sprite[register+1] = '#'
    for i in range(40):
        if i in [register, register + 1, register -1]:
            continue
        sprite[i] = '.'
    
    return sprite

    

if __name__ == "__main__":

    #part1
    instructions = getData("day10.txt")
    instructions = [i.replace("addx ", "") for i in instructions]

    registerValue = 1
    cycles = 0
    interestingCycles = [20, 60, 100, 140, 180, 220]
    interestingSignals = []

    for ins in instructions:
        if ins == "noop":
            cycles += 1
            if cycles in interestingCycles:
                getInterestingSignalStrengths(cycles, registerValue)
        else:
            addValue = int(ins)
            cycles += 1
            if cycles in interestingCycles:
                getInterestingSignalStrengths(cycles, registerValue)
            cycles += 1
            if cycles in interestingCycles:
                getInterestingSignalStrengths(cycles, registerValue)
            registerValue += addValue
        
    print(sum(interestingSignals))


    #part 2
    register = 1
    sprite = ['.'] * 40
    sprite = updateSprite(register, sprite)
    cycles = 0

    crt = ['.']*240

    for ins in instructions:
        if ins == "noop":
            cycles += 1
            if cycles in [register]
            if cycles % 40 == 0:
                continue




