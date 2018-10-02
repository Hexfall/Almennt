import random

def get_word_string(fName):
    try:
        f = open(fName, "r")
        s = ""
        for i in f:
            for j in i:
                if j != "\n":
                    s += j
                else:
                    s += " "
        return s
    except:
        print("File", fName, "not found")
        exit()

def scramble_string(initStr):
    s = ""
    for i in initStr.split():
        if not i[-1].isalpha():
            punc = 1
        else:
            punc = 0
        if len(i) - punc > 3:
            l = list(i[1:-1-punc])
            random.shuffle(l)
            s += i[0]
            for j in l:
                s += j
            if punc == 1:
                s += i[-2:] + " "
            else:
                s += i[-1] + " "
        else:
            s += i + " "
    return s

random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)