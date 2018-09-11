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

n = int(input("Input an position between 1 and 10: "))
while True:
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")
    skipan = input("Input your choice: ")
    if skipan == "r" or skipan == "l":
        n = hreyfing(n, skipan)
        print("New position is:", n)
    else:
        break