from sys import stdin
import re
from collections import defaultdict, deque, Counter
from itertools import permutations, product
from heapq import heappush, heappop
from time import time

def pos_gi(line):
    return list(map(int, re.findall(r"\d+", line)))
def gi(line):
    #(?:(?<!\d)-)?\d+
    return list(map(int, re.findall(r"-?\d+", line)))
def GI(line):
    return int(re.findall(r"-?\d+", line)[0])
def gf(line):
    return list(map(float, re.findall(r"-?\d+(?:\.\d+)?", line)))
def pos_gf(line):
    return list(map(float, re.findall(r"\d+(?:\.\d+)?", line)))
def gs(line):
    return re.findall(r"[a-zA-Z]+", line)
def neigh4(x, y, H, W):
    for nx, ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)
def neigh8(x, y, H, W):
    for nx, ny in (x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1):
        if 0 <= nx < H and 0 <= ny < W:
            yield (nx, ny)

OUTPUT = 1
if OUTPUT:
    file = open("day7.txt", "r")
    input = [i.strip() for i in file.readlines()]
    #input = file.read().rstrip().split("\n\n")
else:
    """ctrl-d for EOF"""
    input = [i.strip() for i in stdin.readlines()]
    #input = stdin.read().rstrip().split("\n\n")

dir_sz = defaultdict(int)
path = ["/"]
pt = 0
while pt < len(input):
    if input[pt] == "$ ls":
        pt += 1
        # Walk through files
        while pt < len(input) and input[pt][0] != "$":
            a, b = input[pt].split()
            if "dir" not in a:
                for i, d in enumerate(path,1):
                    dir_sz["/".join(path[:i])] += int(a)
            pt += 1
    else:
        # cd command
        _, tok, a = input[pt].split()
        if ".." in a:
            path.pop()
        elif "/" not in a:
            path.append(a)
        else:
            path = ["/"]
        pt += 1

space = dir_sz["/"] - 40000000

# Part 1
print(sum(i for i in dir_sz.values() if i < 10**5))

# Part 2
print(min(i for i in dir_sz.values() if i >= space))