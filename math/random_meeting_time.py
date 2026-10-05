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
