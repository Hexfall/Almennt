try:
    for case in range(10000):
        depth = int(input())
        num = 3 ** depth
        cir = 3 / 2 ** depth
        totalCir = num * cir
        length = len(str(int(totalCir)))
        print("Case {}: {}".format(case + 1, length))
except:
    pass