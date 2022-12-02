#find elf carrying the most calories


def caloriesByElf(calsByElf) -> int:
    totalCalsByElf = []

    for elfCals in calsByElf:
        totalCalsByElf.append(sum(elfCals))
    
    print(totalCalsByElf)
    print(max(totalCalsByElf))

    #top three
    totalCalsByElf = sorted(totalCalsByElf)
    print(sum(totalCalsByElf[-3:]))
        

if __name__ == "__main__":

    with open("day1.txt", 'r') as data:
        allCalories = data.readlines()
        separateData = []
        elfCalories = []

        for line in allCalories:
            if line != '\n':
                elfCalories.append(line)
            else:
                separateData.append(elfCalories)
                elfCalories = []
                continue
    
    for elfData in separateData:
        for i in range(len(elfData)):
            elfData[i] = int(elfData[i][:-1])

    caloriesByElf(separateData)