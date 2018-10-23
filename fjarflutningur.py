gates = {}
gatesNum = int(input())
value = 1
for i in range(gatesNum):
    key = value
    value = int(input())
    gates[key] = value
testCases = int(input())
for i in range(testCases):
    start, stop = [int(j) for j in input().split()]
    done = [start]
    num = 1
    if stop not in gates.values():
        print('-1')
    else:
        while True:
            start = gates[start]
            if start == stop:
                print(num)
                break
            elif start in done:
                print('-1')
                break
            else:
                done.append(start)
            num += 1