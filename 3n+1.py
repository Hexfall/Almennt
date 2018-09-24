while True:
    n = int(input("Integer to check: "))
    print(bin(n))
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        print(bin(int(n)))
        count += 1
    print(count)