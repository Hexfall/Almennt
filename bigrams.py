import string
import operator

def makeWordList(fileName):
    megaString = fileName.read()
    megaList = [i.lower().strip().strip(string.punctuation) for i in megaString.split()]
    return megaList

def dicCount(words):
    dic = {}
    for i in range(len(words) - 1):
        try:
            dic[(words[i], words[i + 1])] += 1
        except:
            dic[(words[i], words[i + 1])] = 1
    return dic

fill = open(input("Enter name of file: "), 'r')
wordList = makeWordList(fill)
wordDic = dicCount(wordList)
sortedList = sorted(wordDic.items(), key=operator.itemgetter(1))[::-1]
print(sortedList[:10])