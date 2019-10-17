import sys
from math import gcd


for line in sys.stdin:
    N = int(line)
    combinations = 0
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if gcd(gcd(x, y), z) == 1 and\
                   x * x + y * y == z * z and x < y < z:
                    combinations += 1
    print(combinations)
