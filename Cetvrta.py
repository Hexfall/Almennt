n = int (input())
for k in range(n):
    x = input()
    y = input()
    s = ""
    for i in range(len(x)):
        if x[i:i + 1] == y[i:i + 1]:
            s += "."
        else:
            s += "*"
    print(s)
