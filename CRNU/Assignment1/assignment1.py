from math import sqrt

primes = [2, 3]

def primes_upto(num):
    i = primes[-1]
    while primes[-1] < num:
        i += 2
        p = 1
        while primes[p] <= sqrt(i):
            if i % primes[p] == 0:
                break
            p += 1
        else:
            primes.append(i)

def find_gcd(a, b):
    primes_upto(max(a, b))
    a_div = []
    b_div = []
    for num in range(2):
        for p in primes:
            if p > [a, b][num]:
                break
            if [a, b][num] % p == 0:
                power = 1
                while [a, b][num] % p**power == 0:
                    power += 1
                [a_div, b_div][num] += [p for i in range(power - 1)]
    prod = 1
    a_point = 0
    b_point = 0
    while a_point < len(a_div) and b_point < len(b_div):
        if a_div[a_point] == b_div[b_point]:
            prod *= a_div[a_point]
            a_point += 1
            b_point += 1
        elif a_div[a_point] < b_div[b_point]:
            a_point += 1
        else:
            b_point += 1
    return prod

def gcd(a, b):
    if a == 0 or b == 0:
        return (a + b, a if a == 0 else 1, b if b == 0 else 1)
    great = find_gcd(a, b)
    u, v = 1, 0
    while True:
        v = (great - u * a) / b
        if v == int(v):
            return (great, u, int(v))
        u += 1

def square_and_multiply(g, A, N):
    # Ret g^A % N
    g = g % N
    dic = {1: g}
    i = 1
    while i < A:
        dic[i*2] = (dic[i]**2) % N
        i *= 2
    prod = 1
    binA = bin(A)[2:]
    for point in range(len(binA)):
        if binA[len(binA) - 1 - point] == "1":
            prod = prod * dic[2**point] % N
    return prod
