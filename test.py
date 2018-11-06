import math
for _ in range(int(input())):
    v, a, x, h1, h2 = [float(i) for i in input().split()]
    h1, h2 = h1 + 1, h2 - 1
    if h2 - h1 < 0:
        print("Not Safe")
        continue
    t = x / (math.cos(a/180*math.pi) * v)
    y = v * t * math.sin(a/180*math.pi) - 9.81* t ** 2 / 2
    if h1 < y < h2:
        print("Safe")
    else:
        print("Not Safe")