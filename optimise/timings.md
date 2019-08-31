# Specs
## As run under MacBook Pro (Retina, Mid 2012):

Model Identifier:   MacBookPro10,1
  Processor Name:   Intel Core i7
  Processor Speed:  2,3 GHz
  Number of Processors: 1
  Total Number of Cores:    4
  L2 Cache (per Core):  256 KB
  L3 Cache: 6 MB
  Hyper-Threading Technology:   Enabled
  Memory:   16 GB

# Times (python)
N*2 -> t*8 (double the size of N -> multiply by 8 required time).
Run once for several N and then estimated the total time for N=2^20.

## v00
v00.py took 0.04 for N = 16.
v00.py took 0.09 for N = 32.
v00.py took 0.42 for N = 64.
v00.py took 3.17 for N = 128.
v00.py took 24.92 for N = 256.
v00.py took 201.92 for N = 512.
v00.py took 1651.86 for N = 1024.

ETA N=1.05M -> 1771674009600s -> 20.505.486 days -> 56.179 years
Total speedup    1x
Incr. speedup    1x

## v01
v01.py took 0.02 for N = 16.
v01.py took 0.04 for N = 32.
v01.py took 0.17 for N = 64.
v01.py took 1.18 for N = 128.
v01.py took 9.55 for N = 256.
v01.py took 76.88 for N = 512.
v01.py took 627.51 for N = 1024.

ETA N 1.05M -> 673772994560s -> 7.798.298 days -> 21.365 years
Total speedup    2.63x
Incr. speedup    2.63x

## v02
v02.py took 0.03 for N = 16.
v02.py took 0.03 for N = 32.
v02.py took 0.05 for N = 64.
v02.py took 0.25 for N = 128.
v02.py took 1.81 for N = 256.
v02.py took 15.39 for N = 512.
v02.py took 126.63 for N = 1024.
v02.py took 1058.20 for N = 2048.

ETA N 1.05M -> 142029199768s -> 1.643.856 days -> 4.503 years
Total speedup    12.47x
Incr. speedup     4.74x

## v03
v03b.py took 0.04 for N = 16.
v03b.py took 0.04 for N = 32.
v03b.py took 0.05 for N = 64.
v03b.py took 0.12 for N = 128.
v03b.py took 0.70 for N = 256.
v03b.py took 5.81 for N = 512.
v03b.py took 46.56 for N = 1024.
v03b.py took 392.83 for N = 2048.

ETA N 1.05M -> 52724750088s -> 610.240 days -> 1.672 years
Total speedup    33.60x
Incr. speedup     2.69x

## v04
v04.py took 0.03 for N = 16.
v04.py took 0.02 for N = 32.
v04.py took 0.03 for N = 64.
v04.py took 0.07 for N = 128.
v04.py took 0.39 for N = 256.
v04.py took 3.15 for N = 512.
v04.py took 25.13 for N = 1024.
v04.py took 199.71 for N = 2048.
v04.py took 1593.89 for N = 4096.

ETA N 1.05M -> 26741036808s -> 309.502 days -> 848 years
Total speedup    66.25x
Incr. speedup     1.97x

## v05
v05.py took 0.03 for N = 16.
v05.py took 0.04 for N = 32.
v05.py took 0.04 for N = 64.
v05.py took 0.05 for N = 128.
v05.py took 0.13 for N = 256.
v05.py took 0.85 for N = 512.
v05.py took 6.45 for N = 1024.
v05.py took 50.48 for N = 2048.
v05.py took 401.71 for N = 4096.

ETA N 1.05M -> 6739575439s -> 78.004 days -> 214 years
Total speedup   262.87x
Incr. speedup     3.97x

------------------------------------------------------

## pypy interlude
### v00 pypy
v00.py took 0.17 for N = 16.
v00.py took 0.18 for N = 32.
v00.py took 0.22 for N = 64.
v00.py took 0.58 for N = 128.
v00.py took 3.48 for N = 256.
v00.py took 27.47 for N = 512.
v00.py took 221.88 for N = 1024.
v00.py took 1877.11 for N = 2048.

ETA N 1.05M -> 251941439400s -> 2.915.989 days -> 7.989 years
Total speedup       7.03x
PyPy  speedup       7.03x

### v01 pypy
v01.py took 0.17 for N = 16.
v01.py took 0.19 for N = 32.
v01.py took 0.24 for N = 64.
v01.py took 0.59 for N = 128.
v01.py took 3.96 for N = 256.
v01.py took 37.12 for N = 512.
v01.py took 259.78 for N = 1024.

ETA N 1.05M -> 278936651038s -> 3.228.433 days -> 8.845 years
Total speedup       6.35x
PyPy  speedup       2.41x
v00py speedup       0.90x
v01 is slower than v00(!) PyPy can optimise x ** 2 better than x*x


### v05 pypy
v05.py took 0.49 for N = 16.
v05.py took 0.15 for N = 32.
v05.py took 0.16 for N = 64.
v05.py took 0.16 for N = 128.
v05.py took 0.16 for N = 256.
v05.py took 0.19 for N = 512.
v05.py took 0.30 for N = 1024.
v05.py took 0.96 for N = 2048.
v05.py took 5.70 for N = 4096.
v05.py took 41.18 for N = 8192.
v05.py took 314.58 for N = 16384.

ETA N 1.05M ->   82465259s -> 954 days -> 2.61 years
Total speedup ->  21483x
PyPy  speedup ->     81.72x

------------------------------------------------------

## C interlude
## g++ v00.c -o v00 -std=c++17
v00 took 0.00 for N = 16.
v00 took 0.00 for N = 32.
v00 took 0.04 for N = 64.
v00 took 0.37 for N = 128.
v00 took 3.14 for N = 256.
v00 took 26.53 for N = 512.
v00 took 230.09 for N = 1024.

ETA N 1.05M -> 247057256284s -> 2.859.458 days -> 7.834 years
Total speedup       7.17x
PyPy  speedup       1.02x

## g++ v00.c -O3 -o v00 -std=c++17
v00 took 0.00 for N = 16.
v00 took 0.00 for N = 32.
v00 took 0.01 for N = 64.
v00 took 0.06 for N = 128.
v00 took 0.51 for N = 256.
v00 took 4.58 for N = 512.
v00 took 40.65 for N = 1024.
v00 took 358.02 for N = 2048.

ETA N 1.05M -> 48052630978s -> 556.164 days -> 1.523 years
Total speedup      36.87x
PyPy  speedup       5.24x
O0    speedup       5.14x

## g++ v01.c -o v01 -std=c++17
v01 took 0.00 for N = 16.
v01 took 0.00 for N = 32.
v01 took 0.02 for N = 64.
v01 took 0.14 for N = 128.
v01 took 1.27 for N = 256.
v01 took 10.94 for N = 512.
v01 took 98.49 for N = 1024.
v01 took 864.08 for N = 2048.

ETA N 1.05M -> 115974854410s -> 1.342.301 days -> 3.677 years
Total  speedup       15.27x
py3 v1 speedup        5.81x
PyPyv0 speedup        2.17x <- !!
PyPyv1 speedup        2.40x
Cv0 O0 speedup        2.13x
Cv0 O3 speedup        0.41x

## g++ v01.c -O3 -o v01 -std=c++17
v01 took 0.00 for N = 16.
v01 took 0.00 for N = 32.
v01 took 0.00 for N = 64.
v01 took 0.05 for N = 128.
v01 took 0.48 for N = 256.
v01 took 4.24 for N = 512.
v01 took 37.43 for N = 1024.
v01 took 325.33 for N = 2048.

ETA N 1.05M -> 43665053450s -> 505.382 days -> 1.384 years
Total speedup       40.57x
py3 v1 speedup      15.43x
PyPyv0 speedup       5.77x <- !!
PyPyv1 speedup       6.39x
Cv0 O0 speedup       5.66x
Cv0 O3 speedup       1.10x <- !!
Cv1 01 speedup       2.65x

-----------------------------------------------------

## v06
N*2 -> t*2 (double the size of N -> multiply by 2 required time).
v06.py took 0.04 for N = 16.
...
v06.py took 0.05 for N = 8192.
v06.py took 0.06 for N = 16384.
v06.py took 0.08 for N = 32768.
v06.py took 0.12 for N = 65536.
v06.py took 0.18 for N = 131072.
v06.py took 0.33 for N = 262144.
v06.py took 0.65 for N = 524288.
v06.py took 1.22 for N = 1048576.

N 1.05M -> 1.22s ->
Total speedup       1.373.390.705.116x
Incr. speedup (v5)      5.224.477.084x
Incr. speedup (v5 pypy)
There was a total refactor, so the comparison
with v5 it really does not make a lot of sense.
Time here seems to increase 2N -> 2T

Too fast to continue measuring just on N=1M.
Need to find another strategy. X numbers between 0 and 1M
We assume each base calculation is 41.83% of the time N=1.05M for each random element <= 1.05M (1373390705116 * 539.71 / 1771674009600 / 1000 = 0.4183798449611553)
Base 1000 elems time = 741232697458156s -> 8.579.082.146 days -> 23.504.334 years -> 23.5M years

v06.py took 1.21 for N = 1048576
v06.py took 5.78 for 10 elements, N <= 1048576
v06.py took 57.50 for 100 elements, N <= 1048576
v06.py took 539.71 for 1000 elements, N <= 1048576

Total speedup N=1000      1.373.390.705.116x
Incr. speedup (v5)            5.224.477.084x

## v07
v07.py took 0.09 for N = 1048576.
v07.py took 0.36 for 10 elements, N <= 1048576
v07.py took 3.19 for 100 elements, N <= 1048576
v07.py took 29.64 for 1000 elements, N <= 1048576
v07.py took 297.88 for 10000 elements, N <= 1048576

Total speedup N=1000    2488360069350x
Incr. speedup (v6)              18.21x
pypy speedup  (v7)               2.96x
v07.pypy took 100.62 for 10000 elements, N <= 1048576

## v08
v08.py took 0.07 for N = 1048576.
v08.py took 0.26 for 10 elements, N <= 1048576
v08.py took 2.45 for 100 elements, N <= 1048576
v08.py took 22.80 for 1000 elements, N <= 1048576
v08.py took 226.72 for 10000 elements, N <= 1048576

Total speedup N=1000    2488360069350x
Incr. speedup (v7)              1.31x
pypy speedup  (v8)              2.54x
v08.pypy took 89.12 for 10000 elements, N <= 1048576
