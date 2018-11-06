x, y = [int(i) for i in input().split()]
if x == 0:
    if y < 125:
        x2 = 125*250/(250-y)
        print("{:.2f} {:.2f}".format(x2, 250 - x2))
    else:
        x2 = 125*250/(y)
        print("{:.2f} {:.2f}".format(x2, 0))
elif y == 0:
    if x < 125:
        y2 = 125*250/(250-x)
        print("{:.2f} {:.2f}".format(250 - y2, y2))
    else:
        y2 = 125*250/(x)
        print("{:.2f} {:.2f}".format(0, y2))
else:
    if y > 125:
        x2 = 250-(125*250/y)
        print("{:.2f} {:.2f}".format(x2, 0))
    else:
        y2 = 250-(125*250/x)
        print("{:.2f} {:.2f}".format(0, y2))