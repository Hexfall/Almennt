fjo, spurn = [int(i) for i in input().split()]
vinir = {}
for i in range(1, fjo + 1):
    vinir[i] = set([i])
for i in range(spurn):
    inp = [int(j) for j in input().split()]
    if inp[0] == 1:
        vinir[inp[1]].update(vinir[inp[2]])
        vinir[inp[2]].update(vinir[inp[1]])
    else:
        print(len(vinir[inp[1]]) - 1)