RANK, COUNTRY, RATING, BYEAR, NUM_ATTIBUTES = 0, 1, 2, 3, 4
def create_players_dict(inputFile):
    dic = {}

    def get_value_list():
        aList = [None]*NUM_ATTIBUTES
        aList[RANK], aList[COUNTRY], aList[RATING], aList[BYEAR] = int(rank), country, int(rating), int(byear)
        return aList

    try:
        fileVar = open(inputFile)
        for line in fileVar:
            rank, name, country, rating, byear = line.strip().split('; ')
            lastname, firstname = name.split(', ')
            key = "{} {}".format(firstname, lastname)
            valueList = get_value_list()
            dic[key] = valueList
        fileVar.close()
    except:
        pass
    return dic

def create_countries_dict(inList):
    dic = {}
    for i in inList.items():
        name, country = i[0], i[1][COUNTRY]
        try:
            dic[country].append(name)
        except:
            dic[country] = [name]
    return dic
    
def create_byear_dict(inList):
    dic = {}
    for i in inList.items():
        name, byear = i[0], i[1][BYEAR]
        try:
            dic[byear].append(name)
        except:
            dic[byear] = [name]
    return dic

def printByCountry(inDic, toPrint):
    print("Players by country:")
    print("-------------------")
    for i, j in sorted(inDic.items()):
        avg = sum([toPrint[k][RATING] for k in j]) / len(j)
        print("{} ({}) ({:.1f}):".format(i, len(j), avg))
        for k in j:
            print("{:>40s}{:>10d}".format(k, toPrint[k][RATING]))
            
def printByBYear(inDic, toPrint):
    print("Players by birth year:")
    print("-------------------")
    for i, j in sorted(inDic.items()):
        avg = sum([toPrint[k][RATING] for k in j]) / len(j)
        print("{} ({}) ({:.1f}):".format(i, len(j), avg))
        for k in j:
            print("{:>40s}{:>10d}".format(k, toPrint[k][RATING]))


filename = input("Enter filename: ")
dict_players = create_players_dict(filename)
dict_countries = create_countries_dict(dict_players)
dict_byear = create_byear_dict(dict_players)
printByCountry(dict_countries, dict_players)
printByBYear(dict_byear, dict_players)