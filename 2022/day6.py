#day 6

from utils import getData

def part1(signal) -> int:
    
    signal = list(signal)
    for i in range(0, len(signal)):
        four = signal[i:i+14]
        
        if len(set(four)) == len(four):
            return i+14


if __name__  == "__main__":

    allData = getData("day6.txt")
    test = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    signal = allData[0][:-1]
    print(part1(signal))
    