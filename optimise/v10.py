import sys
from math import gcd
from math import sqrt


def process(N):
    combinations = 0
    max_iter = int(sqrt(N)) + 1
    for x in range(1, max_iter):
        xxN = sqrt(N - x * x)
        for y in range(x + 1, max_iter + 1, 2):
            if gcd(x, y) != 1:
                continue
            if y > xxN:  # N -> z
                break
            combinations += 1
    print(combinations)


for line in sys.stdin:
    N = int(line)
    process(N)
