size, height, width = [int(i) for i in input().split()]
rows = []
for i in range(height):
    rows.append([i for i in input().split()])

order = []
for i in range(size):
    order.append(input())

for i in range(height):
    if order[width*i] == rows[i][0]:
        print('left')
    else:
        print('right')