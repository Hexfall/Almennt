from math import sqrt

def shanks(p, g, h):
    # Solve for g^x=h mod p.
    k = sqrt(p)//1
    results = {1: g % p}
    for n in range(2, k):
        results[n] = (results[n-1] * g) % p # Find all g^n mod p | 1 <= n < k
    