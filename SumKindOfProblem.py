n = int(input())
for asdf in range(n):
    x, y = [int(i) for i in input().split()]
    pos = int((1 + y) * (y / 2))
    eve = pos * 2
    odd = eve - y
    print(x, pos, odd, eve)
