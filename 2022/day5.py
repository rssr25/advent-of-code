#day 5
from utils import getData

stackData = [['S', 'T', 'H', 'F', 'W', 'R'],
             ['S', 'G', 'D', 'Q', 'W'],
             ['B', 'T', 'W'],
             ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
             ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
             ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'], 
             ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
             ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
             ['L', 'G', 'B', 'W']]

testStack = [['Z', 'N'],
             ['M', 'C', 'D'],
             ['P']]

tm = [1, 3, 2, 1]
tf = [2, 1, 2, 1]
tt = [1, 3, 1, 2]


moveData = getData("day5.txt")
moveData = moveData[10:]
moveData = [i[:-1] for i in moveData]

m = []
f = []
t = []

for i in range(len(moveData)):
    moveData[i] = moveData[i].replace("move", '')
    moveData[i] = moveData[i].replace("from", '')
    moveData[i] = moveData[i].replace("to", '')
    moveData[i] = moveData[i].replace(' ', '')

for string in moveData:
    m.append(int(string[0]))
    f.append(int(string[1]))
    t.append(int(string[2]))

#moving is done here
for i in range(len(m)):
    move = m[i]
    frm = f[i]
    to = t[i]

    #for i in range(move):
        #print(frm - 1)
        #print(testStack[frm-1].pop())
    a = stackData[frm-1][-move:]
    a.reverse()
    stackData[to - 1] = stackData[to - 1] + a
    stackData[frm-1] = stackData[frm-1][:-move]
    
    for stack in stackData:
        print(stack)
        print("\n")

    print("\n\n")

tops = ""
for stack in stackData:
    if stack:
        tops = tops + stack.pop()

print(tops)



