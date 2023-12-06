def getData(filePath, delimiter=None)->list:

    with open(filePath, 'r') as data:

        allData = data.readlines()
        allData = [i[:-1] for i in allData]

    return allData
