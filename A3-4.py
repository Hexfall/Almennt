n = int(input("Input a natural number: "))
x = 2
prime = True
while x < n:
    if n % x == 0:
        prime = False
    x+=1
if prime:
    print("Prime")
else:
    print("!Prime")