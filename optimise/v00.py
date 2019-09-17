import sys
from math import gcd


# TODO the name of the function is a b it weird, calculate what?
# (Also, it not only calculates -- but also prints.)
# ((TODO Maybe just inline it?))
def calculate(N):
    combinations = 0
    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if gcd(gcd(x, y), z) == 1 and\
                   x ** 2 + y ** 2 == z ** 2 and x < y < z:
                    combinations += 1
    print(combinations)


for line in sys.stdin:
    calculate(int(line[:-1]))  # TODO line.rstrip() might be more pythonic?
