import sys
from math import gcd


for line in sys.stdin:
    N = int(line[:-1])
    combinations = 0
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if x < y < z and x * x + y * y == z * z and\
                   gcd(gcd(x, y), z) == 1:
                        combinations += 1
    print(combinations)
