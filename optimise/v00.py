import sys


def euclidean_gcd(a, b):
    while (b != 0):
        t = b
        b = a % b
        a = t
    return a


for line in sys.stdin:
    N = int(line[:-1])
    combinations = 0
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if euclidean_gcd(euclidean_gcd(x, y), z) == 1 and\
                   x ** 2 + y ** 2 == z ** 2 and x < y < z:
                    combinations += 1
    print(combinations)
