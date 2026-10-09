"""

## Approach 1: Permutations

With this approach we could consider the problem made of two problems:

1. For a given set of digits, generate all permutations of the set. (6! = 720)
2. For each permutation, generate two numbers x and y so that digits of x and y concatenated give the permutation. (5)


Total count of numbers is (N-1)*N! = 3600

Complexity of this approach would be:
* O(N!) -- get permutations
  * O(N-1) -- generate pairs from given permutation

O((N+1)!) --> 720*6 = 4320

## Aproach 2: Sequential numbers

With this approach we iterate over all 6 digit numbers, filtering out numbers with digits not within {1..6}.

For each number we then generate two numbers x and y so that digit concatenation gives the number digits. 

The complexity of this approach would be:

N - number of digits
* Main loop O(10^(N+1))
  * Verify digits (compare two sets of length N) -- O(N)
    * Generate combinations: O(N-1)

O(10^(N+1)*(N^2)) --> 36,000,000



Comparing two approaches:

            (N+1)!
R(N) = ---------------
        10^(N+1)*(N^2)
    
R(N+1)        (N+2)!          10^(N+1)*(N^2)     (N+2)    N^2             N
------ = ------------------- ----------------- = ----- * ---------  --> -------  (with big N)
 R(N)     10^(N+2)*((N+1)^2)    (N+1)!             10     (N+1)^2         10

When N > 10, the ratio is greater than 1 and increases with N without bound. 

"""

from collections.abc import Iterator


def generate_pairs() -> Iterator:
    allowed_digits = {str(n) for n in range(1, 7)}
    for number in range(100000, 1000000):
        number_str = str(number)
        if set(number_str) == allowed_digits:
            for i in range(1,6):
                yield int(number_str[:i]), int(number_str[i:])


for pair in generate_pairs():
    print(pair)



# Permutations variant

from itertools import permutations

for digits in permutations("123456"):
    for i in range(1, 6):
        x = int(str("".join(digits[:i])))
        y = int(str("".join(digits[i:])))
        print(x, y)
