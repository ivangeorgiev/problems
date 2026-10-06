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