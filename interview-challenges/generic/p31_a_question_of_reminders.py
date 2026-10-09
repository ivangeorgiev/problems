"""
Brute-force solution
"""

def get_numbers():
    requirements = {i: i-1 for i in range(3,10)}
    num = 9
    while True:
        is_compliant = True
        for divisor, reminder in requirements.items():
            is_compliant = (num % divisor) == reminder
            if not is_compliant:
                break
        if is_compliant:
            yield num
        num += 10


numbers = get_numbers()
for _ in range(3):
    print(next(numbers))


"""
Optimized solution

For each digit $N mod n = n - 1$. Thus $N + 1 mod n = 0$ for any
digit.

Since we are given already one number $N0 = 2519$, next number could 
be $N1 = N0 + (N0 + 1)$, thus $Nk = N0 + k*(N0 + 1)$.

By definition N0+1 is divisible by 2..9, thus k*(N0 + 1) is divisible by
2..9 and thus k*(N0 + 1) - 1 has a reminder of d - 1 for any d in 2..9.
"""

def get_numbers(count=3):
    initial = 2520
    num = 0
    for _ in range(count):
        num += initial
        yield num - 1

def is_valid(n):
    return all(n % d == d - 1 for d in range(2, 10))

for n in get_numbers(3):
    print(n, is_valid(n))
