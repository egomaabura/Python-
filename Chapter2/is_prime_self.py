import math

def is_prinme(n):
    if n <= 1:
        return []
    
    primes = [2]
    limit = int(math.sqrt(n))
    odds = [x for x in range(3, n) if x % 2 == 1]

    while limit >= odds[0]:
        primes.append(odds[0])
        odds = [x for x in odds if x % odds[0] != 0]

    return primes + odds


print(*is_prinme(200))
