Measure timings and check correctness of results:

cat input_sample.txt | time python3 v00.py | tee current_output.txt > /dev/null && diff output_sample.txt current_output.txt


- The code could be improved but is not horrible, right? I mean, it even uses gcd from math instead of naively implementing it.
22x speedup (todo check speedup if not linear curve, etc.). From
python3 v00.py  1.57s user 0.03s system 97% cpu 1.632 total
python3 v01.py  0.07s user 0.01s system 93% cpu 0.094 total

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
- v3b Cleanup (no real optimisation here).
    before)
        for line in sys.stdin:
            calculate(int(line[:-1]))
    after)
        for line in sys.stdin:
            calculate(int(line[:-1]) + 1)

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

- v5 Code specialisation (problem-specific). We save 3/8 computations?
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
            for y in range(x + 1, N):
                yy = y * y
                for z in range(y + 1, N):
                    if xx + yy == z * z and gcd(gcd(x, y), z) == 1:
                        combinations += 1







- Memoisation. Save results of calculations which are going to be needed again.

- other noteworthy optimisations: loop unrolling. Leal, etc.
