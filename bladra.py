def find(lis, target):
    for i in range(len(lis)):
        if lis[i] == target:
            return i

toskur, taska = [int(i) for i in input().split()]
rod = [int(i) for i in input().split()]
nr = find(rod, taska)
if nr == 0:
    print('fyrst')
elif nr == 1:
    print('naestfyrst')
else:
    print('{} fyrst'.format(nr + 1))
