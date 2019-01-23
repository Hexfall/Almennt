def veldi(num, exponent):
    if exponent == 1:
        return num
    return num * veldi(num, exponent - 1)

def divmodsum(num):
    if len(str(num)) == 1:
        return num
    big, small = divmod(num, 10)
    return small + divmodsum(big)

def marg(num, mult):
    if mult == 1:
        return num
    return num + marg(num, mult - 1)

def fact(num):
    if num == 0:
        return 1
    return num * fact(num - 1)

def string(num):
    if num == 1:
        return str(num)
    return string(num - 1) + " " + str(num)

def fibo(num):
    if num == 0 or num == 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

print(ack(4, 4))