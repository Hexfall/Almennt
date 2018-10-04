def read(Fill):
    inntak = []
    for i in Fill:
        inntak.append([j for j in i.split(',')])
    return inntak

def findIndexes(listi, leit):
    indexes = [0]
    for j in leit:
        for i in range(1, len(listi[0])):
            if j in listi[0][i]:
                indexes.append(i)
    return indexes

def sortInntak(tilSorts, leit):
    newL = []
    for i in range(len(tilSorts)):
        toAdd = []
        for j in leit:
            toAdd.append(tilSorts[i][j])
        newL.append(toAdd)
    return newL

def floatify(l):
    for i in range(1, len(l)):
        for j in range(1, len(l[i])):
            if l[i][j][-1] == '%':
                l[i][j] = float(l[i][j][:-1])
            else:
                l[i][j] = float(l[i][j])

def minMax(l):
    newL = []
    for i in range(1, len(l[0])):
        maxi = max([l[a][i] for a in range(1, len(l))])
        mini = min([l[a][i] for a in range(1, len(l))])
        for j in range(1, len(l)):
            if maxi == l[j][i]:
                maxIndex = j
            elif mini == l[j][i]:
                minIndex = j
        newL.append([l[0][i], l[minIndex][0], mini, l[maxIndex][0], maxi])
    return newL

def prentList(l):
    print("{:33s}".format("Indicator") + "{:33s}".format("Min") + "{:21s}".format("Max"))
    print("---------------------------------------------------------------------------------------")
    for i in range(len(l)):
        print("{:33s}".format(l[i][0] + ":") + "{:21s}".format(l[i][1]) + "{:6.1f}".format(l[i][2]) + "      " + "{:15s}".format(l[i][3]) + "{:6.1f}".format(l[i][4]))

search = ["Heart Disease Death Rate", "Motor Vehicle Death Rate", "Teen Birth Rate", "Adult Smoking", "Adult Obesity"]
try:
    fileName = input("Enter filename containing csv data: ")
    readFile = open(fileName, "r")
    inntak = read(readFile)
    indexes = findIndexes(inntak, search)
    sortedInntak = sortInntak(inntak, indexes)
    floatify(sortedInntak)
    sortedInntak = minMax(sortedInntak)
    prentList(sortedInntak)
except:
    print("Cannot find file " + fileName)
    print("{:33s}".format("Indicator") + "{:33s}".format("Min") + "{:21s}".format("Max"))
    print("---------------------------------------------------------------------------------------")
