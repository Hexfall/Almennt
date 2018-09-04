x = 10
while x < 100 and x**2 < 1000:
    if x == (x**2 % 100):
        print(x)
    x+=1