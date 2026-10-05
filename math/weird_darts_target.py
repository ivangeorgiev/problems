import math
import random


def play_a_round(num_throws: int, is_hit: callable, x_limit=100, y_limit=100) -> bool:
    num_hits = 0
    num_misses = 0

    for _ in range(num_throws):
        x = math.floor(random.uniform(0, x_limit))
        y = math.floor(random.uniform(0, y_limit))
        
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
        "Entire target": lambda x, y: True,
        "x + y > 120": lambda x, y: x + y > 120,
    }

    num_wins = {func_name: 0 for func_name in functions }

    for _ in range(num_simulations):
        for name, hit_func in functions.items():
            if play_a_round(num_throws, hit_func):
                num_wins[name] += 1

    print(f"Results after {num_simulations} simulations with {num_throws} throws each:")
    for name, wins in num_wins.items():
        print(f"{name}: {wins} wins, probability of winning: {100.0 * wins / num_simulations:.4f}%")
