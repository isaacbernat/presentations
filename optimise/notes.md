Measure timings and check correctness of results:
- v0 Baseline. The code could be improved but it is not horrible, right? I mean, it even uses a counter with the result instead adding the triplets to a list and returning the length.

- v1 Don't reinvent the wheel. If the functionality needed can be found in a trusted library it's probably a good idea to try that first before reimplementing it (and not just for performance reasons):
    before)
        def euclidean_gcd(a, b):
            while (b != 0):
                t = b
                b = a % b
                a = t
            return a

        def simplified_euclidean_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    after)
        from math import gcd

- v2 Function specialisation. Overly generic functions tend to be more expensive than specific ones. Exponentiation is generic and expensive. Squaring is specific and cheap:
    before) "x ** 2 + y ** 2 == z ** 2"
    after) "x * x + y * y == z * z"
# TODO Maybe display some disassembly snippets to show that the generated code is quite different?
#
#    @@ -82,16 +82,16 @@
#                  74 COMPARE_OP               2 (==)
#                  76 POP_JUMP_IF_FALSE       54
#
#    - 12          78 LOAD_FAST                2 (x)
#    -             80 LOAD_CONST               3 (2)
#    -             82 BINARY_POWER
#    + 11          78 LOAD_FAST                2 (x)
#    +             80 LOAD_FAST                2 (x)
#    +             82 BINARY_MULTIPLY
#                  84 LOAD_FAST                3 (y)
#    -             86 LOAD_CONST               3 (2)
#    -             88 BINARY_POWER
#    +             86 LOAD_FAST                3 (y)
#    +             88 BINARY_MULTIPLY
#                  90 BINARY_ADD
#                  92 LOAD_FAST                4 (z)
#    -             94 LOAD_CONST               3 (2)
#    -             96 BINARY_POWER
#    +             94 LOAD_FAST                4 (z)
#    +             96 BINARY_MULTIPLY
#                  98 COMPARE_OP               2 (==)
#                 100 POP_JUMP_IF_FALSE       54
#                 102 LOAD_FAST                2 (x)

- v3 Short-circuit evaluation. Arrange parameters so the ones more likely to fail (and/or cheaper to compute) are evaluated first (last in case of OR chains). Keep in mind that it may affect branch prediction on modern CPUs. Reference: (https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not)
    before) if gcd(gcd(x, y), z) == 1 and x * x + y * y == z * z and x < y < z:
    after) if x < y < z and x * x + y * y == z * z and gcd(gcd(x, y), z) == 1:

- v4 Search space reduction. Avoid going through ranges we know won't satisfy the condition and enforce restrictions earlier (4b is a tiny refactor):
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

- v5 Function calls vs inline code. Python BYTECODE implementation may change, but apparently this has been true at least since 2014 (python 2.7 see https://stackoverflow.com/questions/21107131/why-mesh-python-code-slower-than-decomposed-one ) and is still true today (current version of python 3.7.4). Variables in functions load faster, and this makes the extra function call overhead negligible. Always measure instead of relying only in intuitions:

    before)
        for line in sys.stdin:
            N = int(line[:-1]) + 1
            combinations = 0
            ...

    after)
        def process(N):
            combinations = 0
            ...

        for line in sys.stdin:
            process(int(line[:-1]) + 1)

# TODO explain, introduce and/or refer to docs on "dis" for diassembling function calls and not just "main" code, etc. `python -m dis v05.py > v05_no.py.dis`
    before BYTECODE excerpt)
        STORE_NAME
        LOAD_NAME
        LOAD_NAME

    after BYTECODE excerpt)
        STORE_FAST
        LOAD_FAST
        LOAD_FAST

- v6 Code hoisting. Move results of known calculations outside loops.
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

# TODO Visualize this? Maybe some table/plot with "primitive pythagorean triplets" and "visited" values?
- v7 Code specialisation (problem-specific). We save 6/8 computations. Numbers must be coprimes. At most one number in the triplet can be pair. This let's us increment loops by 2 to keep variables either pair or odd as required.
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

- C/C++ interlude. Compilers... and (basic) optimisation flags :D
# TODO: make the C++ code more idiomatic
    v01.py)
        def process(N):
            combinations = 0
            for x in range(N + 1):
                for y in range(N + 1):
                    for z in range(N + 1):
                        if gcd(gcd(x, y), z) == 1 and\
                           x ** 2 + y ** 2 == z ** 2 and x < y < z:
                            combinations += 1

    v01.c) c++17 has gcd on numeric package. We'll use it here.
        int process(int N){
            int combinations = 0;
            for(int x=1; x < N; x++){
                for(int y=1; y < N; y++){
                    for(int z=1; z < N; z++){
                        if(std::gcd(std::gcd(x, y), z) == 1 &&
                           std::pow(x, 2) + std::pow(y, 2) == std::pow(z, 2) &&
                           x < y && y < z){
                                combinations += 1; }}}}}

- v8 Paradigm shift. Significant speedups can be achieved using non-incremental approaches. In this case we use a calculation based on Euclid's formula to generate primitive pythagorean triples.
    # a*a + b*b = c*c
    # a=(x*x)-(y*y); b=2x*y; c=(x*x)+(y*y)

    for x in range(1, N):
        for y in range(x + 1, N, 2):
            if gcd(x, y) != 1:
                continue
            if x * x + y * y > N:
                break
            combinations += 1

# TODO Maybe motivate/explain.
- v9 Avoid useless calculations. Don't need to go all the way through N:
    before)
        for x in range(1, N):
            for y in range(x + 1, N, 2):
                ...
    after)
        max_iter = int(sqrt(N)) + 1
        for x in range(1, max_iter):
            for y in range(x + 1, max_iter + 1, 2):
                ...

- v10 Expensive vs cheap ops. A few SQRTs can save many squares here.
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

- v11 Types exist! Avoid int to float castings in the loop. Even if it quacks like a duck, there are different kinds of ducks (i.e. implicit conversions).
    before)
        xxN = sqrt(N - x * x)
            ...
            if y > xxN:  # N -> z
    after)
        xxN = int(sqrt(N - x * x))
        ...
        if y > xxN:  # N -> z

- Profilers interlude:
    Previous speedup was... modest (<1%). Time measurement doesn't need to be a black box. Let's profile the code to see what to optimise next (maybe introduce Amdah'ls law here? And gustafson-barsis instead of a longer theoretical intro?). (talk about statistical vs deterministic profilers?)

- v12 Memoisation (without r, no typo here). Storing the result of calculations that are going to be needed again (soon and/or often). Useful for expensive function calls:
    before)
        def process(N):
            ...
                    if gcd(x, y) != 1:
                        continue
    after)
        @lru_cache(maxsize=None)
        def GCD(x, y):
            return gcd(x, y)

        def process(N):
            ...
                    if GCD(x, y) != 1:
                        continue

    ... but wait, in this case the lru_cache was actually more expensive than calculating it each time! Remember to measure!

- v13 Reuse results. The program calculates many Ns. Many computations for a given N are the same as with previous Ns.
    before):
        def process(N):
            ...
                    combinations += 1
            print(combinations)

        for line in sys.stdin:
            process(int(line[:-1]))

    after):
        RESULT = defaultdict(int)
        def preprocess(N=1048576):
            ...
                    RESULT[xx + y * y] += 1
            for i in range(1, MAXN + 1):
                RESULT[i] += RESULT[i - 1]

        preprocess()
        for line in sys.stdin:
            print(RESULT[int(line[:-1])])

- TODO: other noteworthy optimisations: loop unrolling, function inlining, conditional move, branch predictions, rematerialisation (vs hoisting), etc.