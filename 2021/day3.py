import numpy as np
import sys


def gammaRate(binData) -> str:
    signalLength = len(binData[0])
    gammaSignal = ""

    for i in range(signalLength):
        count1 = 0
        count0 = 0

        column = binData[:, i]
        for num in column:
            if num == "1":
                count1 += 1
            
            if num == "0":
                count0 += 1
            
        if count1 > count0: 
            gammaSignal += '1'
        else:
            gammaSignal += '0'
    
    return gammaSignal


def epsilonRate(gammaRate) -> str:
    
    epsilonRate = list(gammaRate)
    for i in range(len(epsilonRate)):

        if epsilonRate[i] == '1':
            epsilonRate[i] = '0'
        elif epsilonRate[i] == '0':
            epsilonRate[i] = '1'
    
    epsilon = "".join(epsilonRate)
    
    return epsilon


def partTwo(binData)->int:
    signalLength = len(binData[0])
    filteredValues = binData.copy()

    #for oxygen value
    for i in range(signalLength):
        count1 = 0
        count0 = 0

        if len(filteredValues) == 1:
            break
        column = filteredValues[:, i]
        for num in column:
            if num == "1":
                count1 += 1
            
            if num == "0":
                count0 += 1
            
        if count1 > count0:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '1')]
        elif count0 > count1:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '0')]
        else:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '1')]
        
    oxygenValue = filteredValues[0]

    #for co2 value
    filteredValues = binData.copy()
    for i in range(signalLength):
        count1 = 0
        count0 = 0

        if len(filteredValues) == 1:
            break
        column = filteredValues[:, i]
        for num in column:
            if num == "1":
                count1 += 1
            
            if num == "0":
                count0 += 1
            
        if count1 > count0:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '0')]
        elif count0 > count1:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '1')]
        else:
            filteredValues = filteredValues[np.where(filteredValues[:, i] == '0')]
    
    co2Value = filteredValues[0]

    oxygenValue = int("".join(oxygenValue), base=2)
    co2Value = int("".join(co2Value), base=2)

    print(oxygenValue*co2Value)


           
    

if __name__ == "__main__":

    binData = []
    with open("day3.txt", 'r') as data:

        binData = data.readlines()
    binData = [i[:-1] for i in binData]

    #creating matrix
    binData = [list(i) for i in binData]
    binData = np.array(binData)


    test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    test = [list(i) for i in test]
    test = np.array(test)
    #gamma = gammaRate(binData)
    #epsilon = epsilonRate(gamma)

    #print(int(gamma, base=2) * int(epsilon, base=2))
    partTwo(binData)


