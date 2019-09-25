from math import sqrt


def find(lis, search):
    half = len(lis) // 2
    if lis == []:
        return 0
    if lis[half] <= search:
        return half + 1 + find(lis[half + 1:], search)
    return find(lis[:half], search)


def ordered_insert(lis, num):
    place = find(lis, num)
    lis.insert(place, num)


men = []
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    ordered_insert(men, sqrt(x ** 2 + y ** 2))
    
for _ in range(int(input())):
    target = int(input())
    print(find(men, target))
