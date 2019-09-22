import sys
from math import gcd


def process(N):
    combinations = 0
    for x in range(1, N):
        for y in range(x + 1, N, 2):
            if gcd(x, y) != 1:
                continue
            if x * x + y * y > N:  # N -> z
                break
            combinations += 1
    print(combinations)


for line in sys.stdin:
    N = int(line[:-1])
    process(N)
