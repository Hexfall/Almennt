def hreyfing (char, skipun):
    "Hreyfa character"
    if (char == 10 and skipun == "r") or (char == 1 and skipun == "l"):
        return char
    else:
        if skipun == "r":
            char += 1
        else:
            char -= 1
        return char

def geraSkipan ():
    "Búa til skipunina"
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    inpSkipan = input("Input your choice: ")
    if inpSkipan == "r" or inpSkipan == "l":
        return inpSkipan
    else:
        print("New position is:", n)
        exit()

n = int(input("Input a position between 1 and 10: "))
while True:
    skipan = geraSkipan()
    n = hreyfing(n, skipan)
    print("New position is:", n)