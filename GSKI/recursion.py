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

def length(inp):
    if inp == "":
        return 0
    return 1 + length(inp[1:])

def binary_search(lis, find):
    half = int(len(lis)/2)
    if len(lis) == 0 or (len(lis) == 1 and lis[0] != find):
        return False
    elif lis[half] == find:
        return True
    elif lis[half] < find:
        return binary_search(lis[half + 1:], find)
    else:
        return binary_search(lis[:half], find)

def x_ish(word, x):
    def is_in(word, letter):
        if word == "":
            return False
        if word[0] == letter:
            return True
        return is_in(word[1:], letter)
    if x == "":
        return True
    elif not is_in(word, x[0]):
        return False
    return x_ish(word, x[1:])

print(x_ish("gagnaskipan", "da"))