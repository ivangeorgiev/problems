import random

count = 0
N = 100000

for _ in range(N):
    x = random.uniform(0, 100)
    y = random.uniform(0, 100)

    if x + y > 120:
        count += 1

print(count / N)