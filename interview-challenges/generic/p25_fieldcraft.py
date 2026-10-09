"""

In each section of the field, the farmer should go straight (after all he must minimize the time). 
Just the the direction will be under different angle (most likely bog - 90 degrees, but let's confirm).

Let's think about the farmer's travel like walking in two dimensions: x and y. 

On x axis:

* a - bog
* b - soil
* c - turf

$a + b + c = 600$

The distancies he walked in each section:

* bog - $100^2 + a^2$
* soil - $200^2 + b^2$
* turf - $300^2 + c^2$

The total time that we have to minimize is:

$t = \frac{100^2 + a^2}{2.5} + \frac{200^2 + b^2}{5} + \frac{300^2 + c^2}{10}$

$\frac{4 \times 100^2 + 2 \times 200^2 + 300^2}{10} + \frac{a^2 + b^2 + c^2}$
"""


from collections.abc import Iterable
import math


def section_distances() -> Iterable[tuple[int, int, int]]:
    for a in range(601):
        for b in range(601):
            if a + b > 600:
                continue
            c = 600 - a - b
            assert c >= 0
            yield (a, b, c)

def time_to_cross(x, y, speed):
    return math.sqrt(x*x + y*y)/speed

def compute_time(a, b, c):
    return time_to_cross(100, a, 2.5) + time_to_cross(200, b, 5) + time_to_cross(300, c, 10)

distances_shortest_time = min(section_distances(), key=lambda v: math.floor(compute_time(*v)))
print(distances_shortest_time, math.floor(compute_time(*distances_shortest_time)))
