def Factorial(x):
    "Returns the factorial of an integer"
    n = 1
    for i in range(1, int(x) + 1):
        n *= i
    return n
