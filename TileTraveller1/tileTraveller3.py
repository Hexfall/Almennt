# https://github.com/Hexfall/Almennt/tree/master/TileTraveller1
# x = 1
# y = 1
# prenta You can travel: (N)orth.
# while x != 3 and y != 3:
#    strengur_inntak = input().lower()
#    ef inntak er valid:
#      færa character
#      prenta mögulegar áttir
#    annars:
#      prenta Invalid
# prenta Sigur
def nyjarLeidir (x, y):
    if x == 1 and y == 1:
        return "N"
    elif x == 1 and y == 2:
        return "NES"
    elif x == 1 and y == 3:
        return "ES"
    elif x == 2 and y == 1:
        return "N"
    elif x == 2 and y == 2:
        return "SW"
    elif x == 2 and y == 3:
        return "EW"
    elif x == 3 and y == 1:
        return ""
    elif x == 3 and y == 2:
        return "NS"
    elif x == 3 and y == 3:
        return "SW"

def validAtt (inntak, leid):
    for i in leid:
        if i == inntak:
            return True
    return False

def prentaAttir(leid):
    if leid != "":
        print("You can travel: ", end="")
        for i in range(len(leidir)):
            if i != 0:
                print(" or ", end="")
            if leidir[i] == "N":
                print("(N)orth", end="")
            elif leidir[i] == "E":
                print("(E)ast", end="")
            elif leidir[i] == "S":
                print("(S)outh", end="")
            elif leidir[i] == "W":
                print("(W)est", end="")
        print(".")

def coinCheck(x, y):
    if (x == 1 and y == 2) or (x == 2 and (y == 2 or y == 3)) or (x == 3 and y == 2):
        pull = input("Pull a lever (y/n): ")
        if pull.lower() == "y":
            print("You received 1 coins, your total is now " + str(coins + 1) + ".")
            return 1
    return 0

playAgain = "y"
while playAgain.lower() == "y":
    x = 1
    y = 1
    coins = 0
    leidir = "N"
    print("You can travel: (N)orth.")
    while not (x == 3 and y == 1):
        inntak = input("Direction: ").upper()
        if validAtt(inntak, leidir):
            if inntak == "N":
                y += 1
            elif inntak == "E":
                x += 1
            elif inntak == "S":
                y -= 1
            elif inntak == "W":
                x -= 1
            coins += coinCheck(x, y)
            leidir = nyjarLeidir(x, y)
            prentaAttir(leidir)
        else:
            print("Not a valid direction!")
    print("Victory!")
    playAgain = input("Play again (y/n): ")