from math import sqrt
men = []
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    men.append(sqrt(x ** 2 + y ** 2))
men.sort()
maximum = men[-1]
minimum = men[0]
for _ in range(int(input())):
    target = int(input())
    if target < minimum:
        print(0)
    elif target >= maximum:
        print(len(men))
    else:
        for i in range(1, len(men)):
            if men[i] > target:
                print(i)
                break