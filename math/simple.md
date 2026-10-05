
## P1

A two-digit number, read from left to right, is 4.5 time as large as the same number read from right to left.`

What is the number?

### Solution

Let our number has two digts $a$ and $b$ so that $ab = 4.5 \times ba$. This could be written in another way:

$$
10 \times a + b = 4.5 \times (10 \times b + a)
$$

$$
5.5 \times a = 44 \times b
$$

$$
a = 8 \times b
$$

Which could hold only if $a=8$ and $b=1$. So the number is: $81$



## P2

A girl has as many sisters as she has brothers. But each brother has twice as many sisters as brothers. How many brothers and sisters are there in the family?

### Solution

If the number of siters is $s$, and the number of brothers is $b$, then we are given that:

The number of sisters a girl has is the same as the number of brothers:

$$ s - 1 = b $$

and the number of sister a boy has is twice the number of brothers:

$$ 2(b - 1) = s $$

Solving above for brothers: $2b - 2 = b + 1$, $b = 3$

Now solving for sisters: $s - 1 = b = 3$, $s = 4$.

Let's verify: a girl has $4-1=3$ sisters and $3$ brothers. A boy has $3-1=2$ brothers and $4$ sisters.




## P3

A train leaves Edinburgh at 8.00 a.m. and travels to London at 60 mph. At 9.00 a.m. another train leaves London and travels towards Edinburg at 90 mph. Which train is nearer to London when they pass?


## P4

If a brick weights seven pounds plus half a brick, what is the weight of a brick and a half?



## P5

There are eight oranges in a box. How can you divide them between eight people so that each person gets one orange, and one orange is still left in the box?

The oragnes must not be peeled or cut.



## P6 / 9

If the only sister of your mother's only brother has an only child, what would be your relationship to that child?


## P7 / 60

**A series of primes**

I want you to find the least number of consecutive prime numbers that add up to 106,620.



### Solution

One of the possible solutions would be to generate a series of prime numbers between 2 and the target number.
Efficient method would be the *Sieve of Eratosphenes*.

We can further iterate over the series of primes to determine the sub-series of given sum. 
An optimization could be to use the two-pointer method.

```python
import time


def generate_primes(max_number: int) -> list[int]:
    primes_mask = [True] * (max_number + 1)
    primes = []
    for num in range(2, max_number + 1):
        if not primes_mask[num]:
            continue
        primes.append(num)
        for non_prime_num in range(num + num, max_number + 1, num):
            primes_mask[non_prime_num] = False
    return primes

target = 106620

start_time = time.time()

primes = generate_primes(target)

print(f"Generated {len(primes)} primes up to {target} in {time.time() - start_time:.3f} seconds")

found = False
for i in range(len(primes), 0, -1):
    for j in range(i, 0, -1):
        s = sum(primes[j:i])
        if s > target:
            break
        if s == target:
            print(f"Sum of primes from {primes[j:i]} is {s}")
            found = True
            break
    if found:
        break
if not found:
    print(f"No sum of consecutive primes found that equals {target}")


print(f"Execution time: {time.time() - start_time:.3f} seconds")
```

Sample output:

```
Generated 10158 primes up to 106620 in 0.010 seconds
sum of primes from [17747, 17749, 17761, 17783, 17789, 17791] is 106620
Execution time: 0.018 seconds
```


Let's get the complexity of the prime numbers generation:

For each number from $x = 2..n$, $\frac{n}{x}$ iterations are performed to update the primes mask (Sieve of Eratosphenes). Thus the total number of iterations is spproximately:

$$
n \left( \frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + ... + \frac{1}{n} \right) = n \times \sum_{p \le n} \frac{1}{p} = \theta(n \log \log n)
$$



## P8 - The Dice Race

You roll a fair six-sided die repeatedly.

You win if you roll a 6 before you roll a 1.

Question: What is the probability of winning?


### Solution

Analytical solution: 50%

Monte Carlo simulation:

```python
import random

wins = 0
num_simulations = 10000000


for _ in range(num_simulations):
    while True:
        roll = random.randint(1, 6)

        if roll == 6:
            wins += 1
            break

        if roll == 1:
            break

print(f"Won {wins} out of {num_simulations} simulations")
print(f"Probability of winning: {100.0*wins / num_simulations:.4f}%")
```

```
Won 4998339 out of 10000000 simulations
Probability of winning: 49.9834%

Won 5000626 out of 10000000 simulations
Probability of winning: 50.0063%

Won 5000205 out of 10000000 simulations
Probability of winning: 50.0020%

Won 4998102 out of 10000000 simulations
Probability of winning: 49.9810%
```

## P9 - Weird Darts Target

You are playing darts with target of size 100x100. On the target there is an aim shape. Each throw is a hit if it hits the target and miss if hits outside the target. Throws are normally distributed within the target. You win a game if the number of hits exceeds the number of misses.

Use simulation to determine the for a win if:

* the aim shape is a circle with radius 25
* the aim shape is a circle with radius 30
* the aim shape is a circle with radius 35
* the aim shape is a circle with radius 40
* the aim shape is a circle with radius 45
* the aim shape is a circle with radius 50
* the aim shape covers the entire target

How would you approach the problem if the shape is irregular?

### Solution

```python
import math
import random


def play_a_round(num_throws: int, is_hit: callable, x_limit=100, y_limit=100) -> bool:
    num_hits = 0
    num_misses = 0

    for _ in range(num_throws):
        x = math.floor(random.uniform(0, 1) * x_limit)
        y = math.floor(random.uniform(0, 1) * y_limit)
        
        if is_hit(x, y):
            num_hits += 1
        else:
            num_misses += 1
    return num_hits > num_misses
    
if __name__ == "__main__":
    num_simulations = 10000
    num_throws = 10
    functions = {
        "Circle with radius 25": lambda x, y: (x - 50) ** 2 + (y - 50) ** 2 <= 25 ** 2,
        "Circle with radius 30": lambda x, y: (x - 50) ** 2 + (y - 50) ** 2 <= 30 ** 2,
        "Circle with radius 35": lambda x, y: (x - 50) ** 2 + (y - 50) ** 2 <= 35 ** 2,
        "Circle with radius 40": lambda x, y: (x - 50) ** 2 + (y - 50) ** 2 <= 40 ** 2,
        "Circle with radius 50": lambda x, y: (x - 50) ** 2 + (y - 50) ** 2 <= 50 ** 2,
        "Entire target": lambda x, y: True
    }

    num_wins = {func_name: 0 for func_name in functions }

    for _ in range(num_simulations):
        for name, hit_func in functions.items():
            if play_a_round(num_throws, hit_func):
                num_wins[name] += 1

    print(f"Results after {num_simulations} simulations with {num_throws} throws each:")
    for name, wins in num_wins.items():
        print(f"{name}: {wins} wins, probability of winning: {100.0 * wins / num_simulations:.4f}%")
```

```
Results after 10000 simulations with 10 throws each:
Circle with radius 25: 53 wins, probability of winning: 0.5300%
Circle with radius 30: 356 wins, probability of winning: 3.5600%
Circle with radius 35: 1480 wins, probability of winning: 14.8000%
Circle with radius 40: 3778 wins, probability of winning: 37.7800%
Circle with radius 50: 9573 wins, probability of winning: 95.7300%
Entire target: 10000 wins, probability of winning: 100.0000%

Circle with radius 25: 51 wins, probability of winning: 0.5100%
Circle with radius 30: 368 wins, probability of winning: 3.6800%
Circle with radius 35: 1465 wins, probability of winning: 14.6500%
Circle with radius 40: 3884 wins, probability of winning: 38.8400%
Circle with radius 50: 9595 wins, probability of winning: 95.9500%
Entire target: 10000 wins, probability of winning: 100.0000%
```


## Simple Monte Carlo Darts

A dartboard is a 100 × 100 square with center at (50, 50).

Each throw lands at coordinates (x, y), where:

* $x \sim U(0,100)$
* $y \sim U(0,100)$
* $x$ and $y$ are independent

What is the probability that $x+y>120$?

_Note:_ $U(a,b)$ denotes variable with uniform distribution.

### Solution

```python

count = 0
N = 100000

for _ in range(N):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)

    if x + y > 120:
        count += 1

print(count / N)
```

```
0.31667

0.31893

0.32218
```


## Random Meeting Time

Two people agree to meet between 12:00 and 13:00.

* Each arrives at a random time uniformly distributed in that hour.
* Each waits for 10 minutes before leaving.

What is the probability they meet?

### Solution

Answer: $\approx 30.5 \%$

```python
import random

duration = 60
wait_interval = 10

N = 1000000

num_meetings = 0

for _ in range(N):
    time1 = random.uniform(0, duration)
    time2 = random.uniform(0, duration)

    if abs(time1 - time2) <= wait_interval:
        num_meetings += 1

print(num_meetings / N)
```

## Coin Toss Race

You repeatedly toss a fair coin.

* You win if you get 3 heads in a row.
* You lose if you get 2 tails in a row.

Estimate the probability of winning.


## Treasure in a Square

A treasure is hidden at a random location:

* $x \sim U(0,100)$
* $y \sim U(0,100)$

You search within a circle of radius 25 centimeters at (50, 50).

Estimate the probability of finding the treasure, using a simulation.


## Sum of Two Random Numbers

Generate:

* $x \sim U(0,100)$
* $y \sim U(0,100)$

Estimate:

$P(x + y > 120)$


## Closest Server

Three servers have random response times:

* $A \sim U(40,100)$
* $B \sim U(50,90)$
* $C \sim U(30,120)$

Estimate the probability that server $B$ is the fastest (response time), using simulation.


## Random Deployment Failure

A deployment consists of 20 independent steps.

Each steps succeeds with probability 98%.

Estimate the probability that the deployment completes with:

* no failures
* at most one failure

## Shared Cache Collision

100 users independently chose a cache key:

* $key \sim U(1,1000)$

Estimate the probability that at least on collision occurs, using simulation.

## Random Walk

A robot starts at position 0.

Each second:

* Move +1 with probability 50%
* Move -1 with probability 50%

After 100 steps, estimate the probability that the robot finishes more than 10 units away from the origin.


## Distributed System Availability

A service is available if at least 2 of 3 servers are running.

Server uptimes are:

* A = 99%
* B = 97%
* C = 95%

Estimate the overall service availability.


## Packet Retry Puzzle

A packet transmission succeeds with probability 30%.

The system retries until success or until 5 attempts have been made.

Estimate:

* Probability of eventual success
* Average number of attempts used



