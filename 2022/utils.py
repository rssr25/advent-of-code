def getData(filePath)->list:

    with open(filePath, 'r') as data:

        allData = data.readlines()

    return allData
