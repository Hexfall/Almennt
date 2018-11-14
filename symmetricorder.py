size = int(input())
n = 1
while size != 0:
    odd, even = [], []
    for i in range(size):
        if i % 2:
            odd.append(input())
        else:
            even.append(input())
    print("SET {}".format(n))
    for i in even:
        print(i)
    for i in odd[::-1]:
        print(i)
    n += 1
    size = int(input())