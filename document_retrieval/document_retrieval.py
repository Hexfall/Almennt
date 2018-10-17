import string

def  fileReader(fileName):
    try:
        openFile = open(fileName, "r")
        return openFile
    except:
        print("Documents not found.")
        exit()

def stringList(fileName):
    fileName.readline()
    l = [i.strip() for i in fileName.read().split('<NEW DOCUMENT>')]
    return l

def promptSelect():
    print()
    print("What would you like to do?")
    print("1. Search Documents")
    print("2. Print Document")
    print("3. Quit Program")
    return input("> ")

def makeSearch(toCheck):
    searchTerms = input("Enter search words: ").split()
    dic = {}
    for i in searchTerms:
        matches = set([j for j in range(len(toCheck)) for k in toCheck[j].split() if k.lower().strip().strip(string.punctuation) == i.lower()])
        dic[i] = matches
    consistent = list(dic.values())[0]
    for i in dic.values():
        consistent = consistent & i
    if len(consistent) != 0:
        print("Documents that fit search:", end = " ")
        for i in consistent:
            print(str(i), end = " ")
    else:
        print("No match.", end = "")
    print()

def printDoc(l):
    x = int(input("Enter document number: "))
    print("Document #" + str(x))
    print(l[x])

fill = fileReader(input("Document collection: "))
text = stringList(fill)
selection = "1"
while selection == "1" or selection == "2":
    selection = promptSelect()
    if selection == "1":
        makeSearch(text)
    elif selection == "2":
        printDoc(text)
print("Exiting program.")