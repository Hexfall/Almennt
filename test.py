def fibo (n):
    x = [1, 1]
    for i in range(n):
        x.append(x[i]+x[i+1])
        print(x[i])


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
fibo(n)