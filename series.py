n = int(input("Initial value: "))
step = int(input("Step: "))
summa = [0]
while sum(summa) < 100:
    print(n, end=" ")
    summa.append(n)
    n += step
print()
print("Sum of series:", sum(summa))