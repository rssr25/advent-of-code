#part 1
inp = []
with open("input.txt", 'r') as data:
    inp = data.readlines()

inp = [int(i[:-1]) for i in inp]

increased = 0

for i in range(1, len(inp)):
    if(inp[i] > inp[i-1]):
        increased += 1

print(increased)


#part 2
windowIncreased = 0
windowSum = []

for i in range(1, len(inp)):
    if i+1 >= len(inp):
        break
    sum = inp[i-1] + inp[i] + inp[i+1]
    windowSum.append(sum)

for i in range(1, len(windowSum)):
    if(windowSum[i] > windowSum[i-1]):
        windowIncreased += 1

print(windowIncreased)