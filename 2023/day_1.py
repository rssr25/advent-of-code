#day1 of advent of code
from utils import getData
data = getData('input_1.txt')

#part 1

def part1(data):
    total = 0
    for string in data:
        nums = []
        for char in string:
            if char.isdigit():
                nums.append(char)
        total += int(nums[0] + nums[-1])
    return total

print(part1(data))

#part 2
numdict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six":6, "seven":7, "eight":8, "nine":9}
words = [k for k, v in numdict.items()]
print(words)

# for i in range(len(data)):
#     curString = data[i]
#     for w in words:
#         if w in curString:
#             curString = curString.replace(w, str(numdict[w]))
#     data[i] = curString

# print(data[:10])

mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
new_data = [[x if (x := "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) else line[i] for i in range(len(line))] for line in data]
print(part1(new_data))