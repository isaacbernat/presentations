Measure timings and check correctness of results:
- v0 Baseline. The code could be improved but is not horrible, right? I mean, it even uses gcd from math instead of naively implementing it.

- v1 Function specialisation. Overly generic functions tend to be more expensive than specific ones. Exponentiation is generic and expensive. Squaring is specific and cheap:
    before) "x ** 2 + y ** 2 == z ** 2"
    after) "x * x + y * y == z * z"

- v2 Order matters. Arrange parameters so the ones more likely to fail (and/or cheaper to compute) are evaluated first (last in case of OR chains).
    before) if gcd(gcd(x, y), z) == 1 and x * x + y * y == z * z and x < y < z:
    after) if x < y < z and x * x + y * y == z * z and gcd(gcd(x, y), z) == 1:

- v3 Enforce restrictions earlier. Avoid going through ranges we know won't satisfy the condition. (3b is a tiny refactor):
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
    - Cpython vs pypy, and their speedups (see timings.md).
      Some manual optimisations are not useful here. Pypy is clever :)
    - Mention Cython, Numba... They are interesting but may require code
    conversions and not be effective with libraries (e.g. gcd from math)

- C interlude. Compilers... and (basic) optimisation flags :D
    v00.py)
        def calculate(N):
            combinations = 0
            for x in range(N + 1):
                for y in range(N + 1):
                    for z in range(N + 1):
                        if gcd(gcd(x, y), z) == 1 and\
                           x ** 2 + y ** 2 == z ** 2 and x < y < z:
                            combinations += 1

    v00.c) c++17 has gcd on numeric package. We'll use it here.
        int calculate(int N){
            int combinations = 0;
            for(int x=1; x < N; x++){
                for(int y=1; y < N; y++){
                    for(int z=1; z < N; z++){
                        if(std::gcd(std::gcd(x, y), z) == 1 &&
                           std::pow(x, 2) + std::pow(y, 2) == std::pow(z, 2) &&
                           x < y && y < z){
                                combinations += 1; }}}}}

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
        max_iter = int(sqrt(N)) + 1
        for x in range(1, max_iter):
            for y in range(x + 1, max_iter + 1, 2):
                ...

- v8 Expensive vs cheap ops. A few SQRTs can save many squares here. Modest speedup.
    before)
        for y in range(x + 1, max_iter + 1, 2):
            ...
            if x * x + y * y > N:  # N -> z
                break
    after)
        xxN = int(sqrt(N - x * x))
        for y in range(x + 1, max_iter + 1, 2):
            ...
            if y > xxN:  # N -> z
                break

- v8b. Types exist! Avoid implicit int to float castings in the loop. Even if it quacks like a duck, there are different kinds of ducks (very modest speedup here).
    before)
        xxN = sqrt(N - x * x)
            ...
            if y > xxN:  # N -> z
    after)
        xxN = int(sqrt(N - x * x))
        ...
        if y > xxN:  # N -> z


- Memoisation. Save results of calculations which are going to be needed again.

- TODO: other noteworthy optimisations: loop unrolling, Leal, function inlining, conditional move, etc.
