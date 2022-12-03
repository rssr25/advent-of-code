from utils import getData


if __name__ == "__main__":

    alps = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alps = list(alps)
    priorityDict = {}

    for i in range(len(alps)):
        priorityDict[alps[i]] = i + 1
    
    
    #get the data
    fullData = getData("day3.txt")
    fullData = [i[:-1] for i in fullData]
    #fullData = fullData[:-1]


    misplaced = []

    for string in fullData:
        
        length = len(string)
        firsthalf = set(string[:int(length/2)])
        secondhalf = set(string[int(length/2):])

        misplaced.append(list(firsthalf.intersection(secondhalf))[0])

    
    score = 0

    for letter in misplaced:
        score += priorityDict[letter]
    

    print(score)

    ###### PART 2 ######
    commons = []

    for i in range(0, len(fullData), 3):
        first = set(list(fullData[i]))
        second = set(list(fullData[i+1]))
        third = set(list(fullData[i+2]))

        common = set.intersection(first, second, third)
        commons.append(list(common)[0])

    
    score2 = 0
    for common in commons:
        score2 += priorityDict[common]
    
    print(score2)


