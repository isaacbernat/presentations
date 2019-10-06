# From 1 > billion years to < 1 second

"An algorithm must be seen to be believed" - *Donald Knuth, 1968*

<div style="text-align: center"><img src="./images/img_timeline.png" width="80%" height="80%"/></div>

---

<embed style="margin-left:-2rem" src="outline.html" width="110%" height="100%"></embed>

???
- This is how the presentation is structured.
- The timing is quite tight, so let's not waste more here?
- Within each section I will advance **chronologically**.


### 12% Part 1 Problem definition.
### 27% Part 2 Optimisations I (0-7).
### 10% Part 3 Compilers.
### 13% Part 4 Optimisations II (8-11).
###  6% Part 5 Profilers.
### 11% Part 6 Optimisations III (12-14).
### 21% Part 7 Recap and closing remarks.

The % is the approximate relative duration.

- 3.5m Part 1 Problem definition.
- 8.0m Part 2 Optimisations I (0-7).
- 2.5m Part 3 Python vs PyPy vs C++.
- 4.0m Part 4 Optimisations II (8-11).
- 1.5m Part 5 Profiling.
- 3.5m Part 6 Optimisations III (12-14).
- 6.5m Part 7 Recap and closing remarks.

---

## Problem definition.

<div style="margin-left:-4rem" ><img src="./images/img_problem_definition.png" width="110%"/></div>

---

## Solution samples.

<div style="margin-left:-4rem" ><img src="./images/img_solutions.py.png" width="95%"/></div>

---

## Time measurements.
#### Timing
- Code is run using python3.7 using this **2012 laptop**.
- Best of **5 runs** for each algorithm and input.
- Increase problem size until set takes **>600 seconds**.
- **Discard** problem sizes with time **< 0.15 seconds**.
- Calculate **ETA using** time complexity estimation of **biggest 3 inputs**.
- e.g. `if size*2 -> time*8 then complexity=O(n^3)` because (2^3 -> 8).

#### Sources
- `github.com/isaacbernat/presentations/tree/master/optimise`
- Specific timings at `times.csv`.
- Summary, ratios and more at `timings.md`.

???

- The laptop **specs** can be found in the **github url**. Just a **new laptop** would probably be a **good speedup** ;D.
- Best of 5 runs (extra time is overhead from OS, etc).
- 600s should be big enough to provide robust numbers.
- Small times have higher variablity non dependent on algorithm.
- We don't have billions of years to wait and get result, but we want to compare different algorithms that are much faster and can't use the same input.

- Feel free to replicate the experiments. If on a different machine they may vary accordingly, but I think should be within the same order of magnitude?
optimise time, vs memory, a specific shared resource, etc.

---

## How good are you at estimating speedups?.
## https://tinyurl.com/pycon2019
### Results from the above form will be published in a few days.
### How fast code is compared to the previous version?
#### current_time / previous_time.
#### E.g. if the code now takes half the time it is 2x (1/0.5). If it takes 75% the original time it is 1.33x (1/0.75).
### Compare Python to Python but also PyPy to PyPy for extra fun!

---

## v0 Baseline.
### `ETA N=2^20:` 98.263 years `; ETA 100k N<=2^20:` >1 Bn

<div style="margin-left:-4rem" ><img src="./images/img_v00i.py.png" width="110%"/></div>

???

## TODO embed/remind the original problem again!

A naive solution would be something like the one above. One could have used a set and put all triplets in it instead of making x < y < z (to avoid repetitions) and then returning the length of the set. It felt more natural to me to add the check and use a counter, since only the amount is needed.

But before we evaluate how good/bad the code is... let's see how gcd is calculated, that's important too!

---

## v0 Baseline.

<div ><img src="./images/img_v00ii.py.png" height="100%"/></div>

???

Well known Euclidean algorithm that does the job. The first version would probably be good enough and look reasonable for most cases, but it can be further simplified as we see below (and use less variables, assignments, etc).

---

## v1 Don't reinvent the wheel.

<div ><img src="./images/img_v01.py.png" height="100%"/></div>

???

### ASK ABOUT TIME ESTIMATING SPEEDUP

Well known algorithm that does the job. The first version would probably be good enough for most cases, but it can be further simplified as we see below.

If the functionality needed can be found in a trusted library it's probably a good idea to try that first before reimplementing it (and not just for performance reasons).

---

## v2 Peephole optimization/strength reduction.
### V1 vs V0 speedup: 1.61x

<div style="margin-left:-4rem" ><img src="./images/img_v02i.py.png" width="110%"/></div>

???
### ETA V1 N=2^20: 60.943 years

---

## v2 Peephole optimization/strength reduction.

<div ><img src="./images/img_v02ii.py.png" width="100%"/></div>

???

Overly generic functions tend to be more expensive than specific ones.
- Exponentiation is generic and expensive.
- Squaring is specific and cheap.
- We can see the difference in CPython bytecode (more on that later)
- Peephole usually consists on replacing a few instructions for equivalent ones that are cheaper for a given architecture (e.g. `y = x * 15` -> `y = (x << 4) - x`)
- Strength reduction is a more generic name for a process of replacing expensive operations for equivalent ones that are cheaper, but that usually involves transforming nested loops, looking at induction variables and invariants.

---

## v3 Short-circuit evaluation.
### V2 vs V1 speedup: 2.19x

<div style="margin-left:-4rem" ><img src="./images/img_v03i.py.png" width="110%"/></div>

???
### ETA V2 N=2^20: 27.714 years

Arrange parameters so the ones more likely to fail (and/or cheaper to compute) are evaluated first (last in case of OR chains). Keep in mind that it may affect branch prediction on modern CPUs.

Further references: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

---

## v3 Short-circuit evaluation.

<div style="margin-left:-4rem" ><img src="./images/img_v03ii.py.png" width="110%"/></div>

---

## v4 Search space reduction.
### V3 vs V2 speedup: 2.58x

<div style="margin-left:-4rem" ><img src="./images/img_v04i.py.png" width="110%"/></div>


???
### ETA V3 N=2^20: 10.717 years

Avoid going through ranges we know won't satisfy the condition and enforce restrictions earlier (4b is a tiny refactor):

---

## v4 Search space reduction.

<div style="margin-left:-4rem" ><img src="./images/img_v04ii.py.png" width="110%"/></div>

---

## v5 Code hoisting.
### V4 vs V3 speedup: 3.56x

<div style="margin-left:-4rem" ><img src="./images/img_v05i.py.png" width="110%"/></div>

???
### ETA V4 N=2^20: 3012 years

Moving results of known calculations (invariants) outside loops.

---

## v5 Code hoisting.

<div style="margin-left:-4rem" ><img src="./images/img_v05ii.py.png" height="95%" width="95%"/></div>

---

## v6 Function calls vs inline code.
### V5 vs V4 speedup: 1.83x

<div style="margin-left:-4rem" ><img src="./images/img_v06i.py.png" height="100%" width="100%"/></div>

???
### ETA V5 N=2^20: 1647 years

This may not hold true in newer Python versions, but variables in functions load faster, and this makes the extra function call overhead negligible. Always measure instead of relying only in intuitions.

---

## v6 Function calls vs inline code.

<div style="margin-left:-4rem" ><img src="./images/img_v06ii.py.png" height="110%"/></div>

---

## v6 Function calls vs inline code.

<div style="margin-left:-4rem" ><img src="./images/img_v06iii.py.png" width="110%"/></div>

???

They make no guarantees that the transformation from Python code to the intermediate bytcode used by CPython will be compatible/the same between versions (implementation may change), so, use it at your own risk.

Apparently this behaviour has been true at least since 2014 in python 2.7 and is still true today (current version of python 3.7.4).

References:
- https://stackoverflow.com/questions/21107131/why-mesh-python-code-slower-than-decomposed-one
- https://docs.python.org/3/library/dis.html (the official disassembler package)

---

## v7 Code specialisation
### V6 vs V5 speedup: 2.03x

<div style="margin-left:-4rem" ><img src="./images/img_v07i.py.png" width="110%"/></div>

???
### ETA V6 N=2^20: 811 years

Problem-specific. We save 6/8 computations. Numbers must be coprimes. At most one number in the triplet can be pair. This let's us increment loops by 2 to keep variables either pair or odd as required.

---

<div style="margin-left:-4rem" ><img src="./images/img_v07ii.py.png" height="110%"/></div>

???

---

## Interlude: Compilers
### V7 vs V6 speedup: 4.15x

### PyPy
- JIT (just in time). Can take into account usage data be more efficient.
- Replace `"python3"` with `"pypy3"`
- Many other "python-based" options are avialable: e.g. Numba, Cython...

### C++ 17
- Can be close to the machine.
- Tried to be faithful when porting Python to make comparisons fair.
- `g++` (from GNU Compiler Collection) the standard open source compiler.
- Flags used `"-O0"` and `"-O3"`.

???
### Definition
Compilers translate a source language (python) into another (bytecode). They also can apply optimisations, analysing the whole source code and how it behaves.

PyPy is just one of many tools to speedup python.
### Numba didn't like gcd
### Cython converts "python" code to C. Needs to define data types to be really effective.
### there are others, but the presentation is already quite long as it is.

## C++
- Tried to be as faithful as possible when porting code to the original python source. Some idioms are not available and forced it to make it differently, of course.
- But I ported it to C++ 17, so I could use the built-in gcd library and compare it with the first optimisation (i.e. don't reinvent the wheel!).
- g++ (from GNU Compiler Collection) is a production-grade compiler used and relied upon by many. We'll use it in our tests.
- I used -O0 and -O3 optimisation levels. But many more useful optimisation flags exist (e.g. march) that may increase speedup even more.


---
<!-- <object type="text/html" width="100%" height="100%", data="timing7.html"/> -->
<embed style="margin-left:-2rem" src="plot_eta7.html" width="110%" height="100%"></embed>


???


---
<embed style="margin-left:-2rem" src="plot_speedup7.html" width="110%" height="100%"></embed>


???


---
<embed style="margin-left:-2rem" src="plot_size_complexity7.html" width="110%" height="100%"></embed>


???

---

## v8 Paradigm shift.

<div style="margin-left:-4rem" ><img src="./images/img_v08i.py.png" height="90%" width="90%"/></div>

???
### ETA V7 N=2^20: 195 years. v0 was 98.263. That's >500x total!

Significant speedups can be achieved using non-incremental approaches. In this case we use a calculation based on Euclid's formula to generate primitive pythagorean triples.

Didn't know if I should call it "paradigm shift", "do research", or "full rewrite".

People get attached to code, and there is this sunk cost fallacy which prevents people from discarding and recognised the "wasted effort" when that would be the more effective approach.

Significant speedups can be achieved using non-incremental approaches. In this case we use a calculation based on Euclid's formula to generate primitive pythagorean triples.

---

## v9 Early loop termination.
### V8 vs V7 speedup: 9 172 593 998x; N=2^20: 1.1s (v7 ETA 195years)

<div style="margin-left:-4rem" ><img src="./images/img_v09i.py.png" width="100%"/></div>

???
### V8 ETA 100k N>=2^20: 67.165s
### `sqrt(N) * sqrt(N) = N`
### Adding anything to N will make it > N. Therefore invalid as we see in line 17. Let's save those computations. Don't need to go all the way through N.

---

## v9 Early loop termination.

<div style="margin-left:-4rem" ><img src="./images/img_v09ii.py.png" width="110%"/></div>

---

## v10 Expensive vs cheap ops.
### V9 vs V8 speedup: 14.82x

<div style="margin-left:-4rem" ><img src="./images/img_v10i.py.png" width="100%"/></div>

???
### V9 ETA 100k N>=2^20: 4531s

A few SQRTs can save many squares here.

---

## v10 Expensive vs cheap ops.

<div style="margin-left:-4rem" ><img src="./images/img_v10ii.py.png" width="110%"/></div>

---

## v11 Mind types.
### V10 vs V9 speedup: 1.28x

<div style="margin-left:-4rem" ><img src="./images/img_v11i.py.png" width="100%"/></div>

???
### V10 ETA 100k N>=2^20: 3531s

Avoid int to float castings in the loop. Even if it quacks like a duck, there are different kinds of ducks (i.e. implicit conversions).

---

## v11 Mind types.

<div style="margin-left:-4rem" ><img src="./images/img_v11ii.py.png" width="110%"/></div>

---

## Interlude: Profiling
### V11 vs V10 speedup: 1.01x

#### Amdahl's law*
- The non-optimised part sets an upper bound on speedup.
- Fragments which take 1/3 of time will NEVER be faster than 1.5x.
- Useful to choose where to focus on and the potential upside.

<div style="margin-left:-4rem" ><img src="./images/img_profilingi.png" height="100%"/></div>


???
## DO ask to write previous speedup!

Previous speedup was... modest (<1%). Time measurement doesn't need to be a black box. Let's profile the code to see what to optimise next

### Amdahl's law
- Added the * because he referred to parallellisable code. Not exactly the same context here, I know.
- Mention Amdahl's law vs Gustafson's law? That only applied to parallel computing though...

References: Amdahl's law http://demonstrations.wolfram.com/AmdahlsLaw/

### pprofile
- it allows line-by-line (cProfile, python's standard granularity is functions)
- is deterministic (good for tasks that take few seconds)
- easy to install with pip and easy to use
- the image shown in next screen is a simplified output

---

## Interlude: Profiling

### `github.com/vpelletier/pprofile`

<div style="margin-left:-4rem" ><img src="./images/img_profilingii.png" width="110%"/></div>

???

### statistical vs deterministic profilers?
- det: overhead (can't be used in prod)
### about 50x slower
### 2.73s vs ~0.06s; N=1024*1024
### 154s  vs  3.26s; 100 of 0 < N <= 1024*1024
- implemented in python. There may be less portable C versions with smaller overhead

- stat: needs long run time to be reliable
this profiles also supports statistical mode

---

## v12 Memoisation (without r, no typo here).

<div style="margin-left:-4rem" ><img src="./images/img_v12i.py.png" width="100%"/></div>

???
### V11 ETA 100k N>=2^20: 3513s

Avoid int to float castings in the loop. Even if it quacks like a duck, there are different kinds of ducks (i.e. implicit conversions).

---

## v12 Memoisation.

<div style="margin-left:-4rem" ><img src="./images/img_v12ii.py.png" height="110%"/></div>

---

## v13 Reuse results.
### V12 vs V11 speedup: 0.81x

<div style="margin-left:-4rem" ><img src="./images/img_v13i.py.png" width="100%"/></div>

???
### V12 ETA 100k N>=2^20: 4297s

... but wait, in this case the lru_cache was actually more expensive than calculating it each time! We won't be adding that "optimisation" (also always remember to measure!)

---

<div style="margin-left:-4rem" ><img src="./images/img_v13ii.py.png" height="85%" width="85%"/></div>


---

## v14 Reduce memory footprint.
### V13 vs V12 speedup: 3978.92x

<div style="margin-left:-4rem" ><img src="./images/img_v14i.py.png" width="100%"/></div>

???
### V13 ETA 100k N>=2^20: 1.08s

... but wait, in this case the lru_cache was actually more expensive than calculating it each time! We won't be adding that "optimisation" (also always remember to measure!)

---

## v14 Reduce memory footprint.

<div style="margin-left:-4rem" ><img src="./images/img_v14ii.py.png" height="85%" width="85%"/></div>

???

---

## The end? (V14 vs V13 speedup: 1.77x)

<div style="margin-left:-4rem" ><img src="./images/img_v15i.py.png" height="95%" width="95%"/></div>

???
### V14.py ETA 100k N>=2^20: 0.61s
### V13.py ETA 100k N>=2^20: 1.08s
### V13.c  ETA 100k N>=2^20: 0.05s

... but wait, in this case the lru_cache was actually more expensive than calculating it each time! We won't be adding that "optimisation" (also always remember to measure!)


---
<embed style="margin-left:-2rem" src="plot_eta14.html" width="110%" height="100%"></embed>


???


---
<embed style="margin-left:-2rem" src="plot_speedup14.html" width="110%" height="100%"></embed>


???


---
<embed style="margin-left:-2rem" src="plot_size_complexity14.html" width="110%" height="100%"></embed>


???

---
<embed style="margin-left:-2rem" src="plot_speedup_vs14.html" width="110%" height="100%"></embed>


???

---

## v1337 The end is just another beginning

- `v14.py` vs `1337.cpp`
    - 0.6 Kib vs  15 Kib
    - 30 lines vs 140 lines
    - Readability, maintainability, portability... not easily measured.

### Noteworthy C++ optimisations:
- vectorisation
- memoisation of `GCD` (43x on v12)
- smaller memory footprint (e.g. `chars` for `gcd(m, n) == 1`)
    - bithacks and masks has even smaller footprint!
- `struct union` to reuse all memory allocated for `GCD == 1` for results, even when they have different data types.
    - 4 `char` -> 1 `int`, so it fits!
- read input entries while calculating the results in parallel (using threads).
- do so in bulk (128 entries at a time)
- reading/writing on a shared memory buffer simulataneously for a smaller memory footprint.


???
Many other interesting techniques
- threads (for calculations too, splitting a big task)
- branch predictions (especially important on pipeline processors)
- conditional move (both computed, but hit rate independent)
- loop unrolling (space-time tradeoff). Beware of data dependencies.
- function inlining
- rematerialisation (vs code hoisting)
- pre-compute vs do it on demand
- bit hacks
- loop fusion/fission
- and many more! (for fun check LEA for multiplications on x86)

### V1337.c  ETA 100k N>=2^20: 0.02s
### V9001.c  ETA 100k N>=2^20: 0.03s

### non-noteworthy (compiler should do):
- do while (vs for loop)
- preincrement (vs postincrement, e.g. ++i vs i++)

---

## Typical pitfalls
#### Not considering Amdahl's law*
#### Optimising code still in development.
#### Not measuring time/resources properly.
#### Not checking result correctness.
#### Including more than 1 optimisation at once.
#### Ignoring usage constraints (e.g. cache size, IO).
#### Not knowing when to stop.

???
#### Amdahl: If the code optimised takes only 1% of time, even if it's n^3 to n optimisation speedup will be <1%

#### Still dev: code may change. Optimisations may not even apply after the refactored version with the correct logic is delivered. That's wasted effort/development time.

#### Proper measurement. Timings should be taken several times to avoid outliers, also the machine load and state should be as close as possible as the state that is compared with. Usage should be as close to production/reality as possible. That includes other programs running.

#### One may forget to be thorough on results, just looking at time.

#### Hard to know the effects of each specific one. Maybe one actually makes the code slower, but when put together is not noticeable.

#### Knowing cache sizes to avoid misses (e.g. by accessing matrixes in bocks) can have a big impact on performance. On a higher level, handling slow resources (e.g. disk IO, HTTP requests) asyncronously (if possible). This can go undetected if only measuring CPU time too.

#### Good enough is good enough. Performance requirements are important. E.g. if we only want numbers < 50 the code for v00.py is perfectly fine. In fact is faster than v13.py .

---

## Methodology
### `WHILE` not is_acceptable(performance):
#### 0. Analyze performance of current code.
#### 1. Apply ONE optimization.
#### 2. Check correctness of results.
#### 3. Analyze performance of the new version.
#### 4. Decide if the optimization should be included.

---

## Specials thanks: `github.com/isaacbernat`
### Mattias Johansson, Ivbar, LOGEX Group; `github.com/folkol`
### David Garcia Villalba, Zhilabs, Samsung; `github.com/dagavi`

"Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should **forget about small efficiencies, say about 97% of the time**: premature optimization is the root of all evil. Yet we should **not pass** up our opportunities in **that critical 3%"** - *Knuth, 1974*

"It is often a mistake to make **a priori judgements** about what parts of a program are really critical..." - *Knuth, 1974*

"In established engineering disciplines **a 12 % improvement**, easily obtained, **is never considered marginal** and I believe the same viewpoint should prevail in software engineering" - *Knuth, 1974*

["Structured Programming with go to Statements"](https://web.archive.org/web/20131023061601/http://cs.sjsu.edu/~mak/CS185C/KnuthStructuredProgrammingGoTo.pdf) (page 8 of the pdf)

???
### For once I have not highlighted the most (in)famous part of the quote about "premature optimization is the root of all evil". I think he meant that one should focus on bottlenecks when doing **incremental optimisations**. Note that he talks about "small efficiencies". I think optimisations which change time complexity, say from N^3 to N^2 won't be in the same league and should be considered (considered != automatically applied, for small Ns the difference won't probably matter, there are also setup times, etc. and keep in mind Amdahl!).
### So... always measure! I hope writing down and checking speedups helped you see how much off one may be!
### All quotes above taken from here. GOTO statements are not a hot topic anymore, but there are yet more still valid quotes in that paper surrounding the topic of code optimisation.
### 12% improvement on what? A specific routine? The whole system? Just so you see I am not a Knuth fanboy I added a quote on optimisation I disagree with. I think software engineering is special in that "waiting two years for a more powerful computer to become available" or more recently "scaling up on instances" might be seen as a legit improvement by many. Bigger and easier than 12% for sure... He goes on that he wouldn't probably bother for such optimisations on one-time-jobs, but wouldn't deny them to prepare quality software. On that second part I do agree :D
A good article on the topic: http://www.joshbarczak.com/blog/?p=580