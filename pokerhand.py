cards = [i[0] for i in input().split()]
dic = {}
for i in cards:
    try:
        dic[i] += 1
    except:
        dic[i] = 1
print(max(dic.values()))