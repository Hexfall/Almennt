l = []
answers = []
time = 0
while(True):
    s = input()
    if s == "-1":
        break
    else:
        l.append(s)
        if s.split()[2] == "right" and not answers.__contains__(s.split()[1]):
            answers.append(s.split()[1])
for i in l:
    if answers.__contains__(i.split()[1]):
        if (i.split()[2] == "right"):
            time += int(i.split()[0])
            answers.remove(i.split()[1])
        else:
            time += 20
print(time)
        