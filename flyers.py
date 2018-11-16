def read_file_to_list(filename):
    returnList = []
    openFile = open(filename, 'r')
    for i in openFile:
        returnList.append([j.strip() for j in i.split()])
    return returnList

def list_to_dict(inList):
    returnDict = {}
    for i in inList:
        try:
            returnDict[i[0]].add(i[1])
        except:
            returnDict[i[0]] = set([i[1]])
    return returnDict

def most_travelled(inDict):
    curMax = 0
    curMaxName = ""
    for i in inDict.keys():
        try:
            if len(inDict[i]) > curMax:
                curMaxName = i
                curMax = len(inDict[i])
        except:
            curMaxName = i
            curMax = len(inDict[i])
    return curMaxName, curMax

flightList = read_file_to_list("flights.txt")
flightDict = list_to_dict(flightList)
for i in sorted(flightDict.keys()):
    print(i + ":")
    for j in sorted(flightDict[i]):
        print("\t" + j)
print()
mostTravelledPerson, mostTravelledNumber = most_travelled(flightDict)
print("{} has been to {} countries".format(mostTravelledPerson, mostTravelledNumber))