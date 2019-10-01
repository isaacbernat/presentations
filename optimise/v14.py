import sys
from math import gcd
from math import sqrt
from collections import defaultdict


RESULT = defaultdict(int)
MAXN = 1048576


def preprocess():
    max_iter = int(sqrt(MAXN)) + 1
    for x in range(1, max_iter):
        xx = x * x
        xxN = int(sqrt(MAXN - xx))
        for y in range(x + 1, max_iter + 1, 2):
            if gcd(x, y) != 1:
                continue
            if y > xxN:
                break
            RESULT[(xx + y * y - 1) // 4] += 1
    for i in range(1, int(MAXN / 4) + 1):
        RESULT[i] += RESULT[i - 1]


preprocess()


for line in sys.stdin:
    N = (int(line) - 1) // 4
    print(RESULT[N])
