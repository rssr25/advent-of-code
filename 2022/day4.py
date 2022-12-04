#Day 4
from utils import getData

allData = getData("day4.txt")
allData = [i[:-1] for i in allData]
allData = [i.split(",") for i in allData]

#part 1
count = 0
overlaps = 0
assignment0 = []
assignment1 = []
for assign in allData:
    assignment0.append(assign[0].split("-"))
    assignment1.append(assign[1].split("-"))

for i in range(0, len(assignment0)):
    assignment0[i] = [int(assignment0[i][0]), int(assignment0[i][1])]
    assignment1[i] = [int(assignment1[i][0]), int(assignment1[i][1])]


for i in range(0, len(assignment0)):
    assignment0[i] = set([k for k in range(assignment0[i][0], assignment0[i][1] + 1)])
    assignment1[i] = set([k for k in range(assignment1[i][0], assignment1[i][1] + 1)])


for set1, set2 in zip(assignment0, assignment1):
    if set1.issubset(set2) or set2.issubset(set1):
        count += 1

print(count)

#PART 2
for set1, set2 in zip(assignment0, assignment1):
    if set1 & set2:
        overlaps += 1

print(overlaps)