import sys
from math import gcd


for line in sys.stdin:
    N = int(line) + 1
    combinations = 0
    for x in range(2, N):
        xx = x * x
        for y in range(x + 1, N):
            yy = y * y
            for z in range(y + 1, N):
                if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                    combinations += 1
    print(combinations)
