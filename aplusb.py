input()
l = [int(i) for i in input().split()]
count = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] + l[j] in l:
            count += 1
print(count * 2)