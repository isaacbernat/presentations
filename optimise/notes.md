Measure timings and check correctness of results:

cat input_sample.txt | time python3 v00.py | tee current_output.txt > /dev/null && diff output_sample.txt current_output.txt

From v00 to v01
---------------
- The code could be improved but is not horrible, right? I mean, it even uses gcd from math instead of naively implementing it.
22x speedup (todo check speedup if not linear curve, etc.). From
python3 v00.py  1.57s user 0.03s system 97% cpu 1.632 total
python3 v01.py  0.07s user 0.01s system 93% cpu 0.094 total

- Exponentiation is expensive. Squaring is cheap:
    before) "x ** 2 + y ** 2 == z ** 2"
    after) "x * x + y * y == z * z"

- Fail fast. Arrange parameters to evaluate first the cheaper to compute so one may fail faster.
    before) if gcd(gcd(x, y), z) == 1 and x ** 2 + y ** 2 == z ** 2 and x < y < z:
    after) if x < y < z and x ** 2 + y ** 2 == z ** 2 and gcd(gcd(x, y), z) == 1 :

- Enforce restrictions earlier. Avoid going through ranges we now won't satisfy the condition:
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

- Small cleanup (add the +1 to N so we don't do it every time on the range function)


From v01 to v02
---------------
TODO
