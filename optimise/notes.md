Measure timings and check correctness of results:
- v0 Baseline. The code could be improved but is not horrible, right? I mean, it even uses gcd from math instead of naively implementing it.

- v1 Specific and cheap over generic and expensive. Exponentiation is expensive and square is cheap:
    before) "x ** 2 + y ** 2 == z ** 2"
    after) "x * x + y * y == z * z"

- v2 Fail fast. Arrange parameters to evaluate first the cheaper to compute so one may fail faster.
    before) if gcd(gcd(x, y), z) == 1 and x * x + y * y == z * z and x < y < z:
    after) if x < y < z and x * x + y * y == z * z and gcd(gcd(x, y), z) == 1:

- v3a Enforce restrictions earlier. Avoid going through ranges we now won't satisfy the condition:
    before)
        for x in range(N + 1):
            for y in range(N + 1):
                for z in range(N + 1):
                    if x < y < z and ...
    after)
        for x in range(2, N + 1):
            for y in range(x + 1, N + 1):
                for z in range(y + 1, N + 1):
                    if ...

- v4 Code hoisting. Move results of known calculations outside loops.
    before)
        for x in range(2, N):
            for y in range(x + 1, N):
                for z in range(y + 1, N):
                    if x * x + y * y == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1
    after)
        for x in range(2, N):
            xx = x * x
            for y in range(x + 1, N):
                yy = y * y
                for z in range(y + 1, N):
                    if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1

- v5a Code specialisation (problem-specific). We save 6/8 computations
    before)
        for x in range(2, N):
            xx = x * x
            for y in range(x + 1, N):
                yy = y * y
                for z in range(y + 1, N):
                    if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1
    after)
        for x in range(2, N, 2):
            xx = x * x
            for y in range(x + 1, N, 2):
                yy = y * y
                for z in range(y + 2, N, 2):
                    if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1

        for x in range(3, N, 2):
            xx = x * x
            for y in range(x + 1, N, 2):
                yy = y * y
                for z in range(y + 1, N, 2):
                    if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1

- Pypy interlude. Let compilers do the heavy lifting
    before)
        python v00.py
        python v05.py
    after)
        pypy 00.py  ( 7x speedup)
        pypy 05.py  (82x speedup)

- v6 Paradigm shift. Complete refactor of "calculations":

    for x in range(1, N):
        for y in range(x + 1, N, 2):
            if gcd(x, y) != 1:
                continue
            if x * x + y * y > N:  # N -> z
                break
            combinations += 1

- v7 Avoid useless calculations. Don't need to go all the way through N:
    before)
        for x in range(1, N):
            for y in range(x + 1, N, 2):
                ...
    after)
        max_iter = int(sqrt(N / 2)) + 1
        for x in range(1, max_iter):
            for y in range(x + 1, max_iter + 1, 2):
                ...



- Memoisation. Save results of calculations which are going to be needed again.

- other noteworthy optimisations: loop unrolling. Leal, etc.
