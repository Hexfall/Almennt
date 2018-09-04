n = int(input("Input a number between 0 and 999: "))
for i in range(n):
    summa = 0
    for k in str(i):
        summa += int(k)**len(str(i))
    if summa == i:
        print(i)