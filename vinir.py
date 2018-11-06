fjo, spurn = [int(i) for i in input().split()]
vinir, done = [], []
for _ in range(spurn):
    inp = [int(i) for i in input().split()]
    if inp[0] == 1:
        a, b = inp[1], inp[2]
        if not a in done and not b in done:
            vinir.append(set([a, b]))
            done += [a, b]
        elif a in done and b in done:
            place1, place2 = -1, -1
            for i in range(len(vinir)):
                if a in vinir[i]:
                    place1 = i
                if b in vinir[i]:
                    place2 = i
                if place1 != -1 and place2 != -1:
                    break
            if place1 != place2:
                vinir[place1] = vinir[place1] | vinir[place2]
                vinir.pop(place2)
        else:
            if b in done:
                c = a
                a = b
                b = c
            done.append(b)
            for i in vinir:
                if a in i:
                    i.add(b)
                    break
    else:
        if inp[1] in done:
            for i in vinir:
                if inp[1] in i:
                    print(len(i) - 1)
                    break
        else:
            print(0)