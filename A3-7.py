x = 1
scores = ["albatross", "eagle", "birdie", "par", "bogey", "double bogey", "triple bogey"]
while x <= 18:
    pStr = "Par of hole " + str(x) + ": "
    par = int(input(pStr))
    pStr = "Score on hole " + str(x) + ": "
    score = int(input(pStr))
    diff = score - par + 3
    if (diff < 0):
        print("invalid score")
    elif (diff > 6):
        print("bad hole")
    else:
        print(scores[diff])
    x+=1