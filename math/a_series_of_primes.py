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
