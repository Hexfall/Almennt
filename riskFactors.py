def read(Fill):
    inntak = []
    for i in Fill:
        inntak.append([j for j in i.split(',')])
    return inntak

def sortInntak(listi, leit):
    indexes = [0]
    for i in range(1, len(listi[0])):
        for j in leit:
            if j in listi[0][i]:
                indexes.append(i)

search = ["Heart Disease Death Rate", "Motor Vehicle Death Rate", "Teen Birth Rate", "Adult Smoking", "Adult Obesity"]
try:
    fileName = input()
    readFile = open(fileName, "r")
    inntak = read(readFile)
    sortedInntak = sortInntak(inntak, search)
except:
    print("Cannot find file " + fileName)
    print("{:33s}".format("Indicator") + "{:33s}".format("Min") + "{:21s}".format("Max"))
    print("---------------------------------------------------------------------------------------")
