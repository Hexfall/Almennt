n = int(input("Input an position between 1 and 10: "))
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")
skipan = input("Input your choice: ")
while skipan == "l" or skipan == "r":


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