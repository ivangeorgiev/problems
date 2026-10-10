"""
Solution 1: Incomplete
"""

# 1. Let's generate all prime numbers <= 100
primes = [2, 3, 5, 7]

x = primes[-1] + 1
for x in range(primes[-1]+1, 100):
    is_prime = True
    for d in primes:
        if x % d == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(x)

# 3. Let's find all sub-sequences (combinations) of prime numbers which add up to 100

from itertools import combinations

def get_numbers():
    for r in range(1, len(primes)):
        for factors in combinations(primes, r=r):
            if sum(factors) != 100:
                continue
            product = 1
            for n in factors:
                product *= n
            yield product
print(max(get_numbers()))



"""
Optimized solution.

"""

def largest_number_with_prime_sum(total):
    threes, remainder = divmod(total, 3)

    # If remainder is 1, convert one 3 into 2 + 2
    if remainder == 1:
        threes -= 1
        remainder = 4

    factors = [3] * threes + [2] * (remainder // 2)

    result = 1
    for p in factors:
        result *= p

    return result, factors


value, factors = largest_number_with_prime_sum(100)
print(value)     # 7412080755407364
print(factors)   # [3, 3, ..., 3, 2, 2]
print(sum(factors))  # 100