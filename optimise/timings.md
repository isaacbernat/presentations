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
Incr. speedup ->     81.72x
-----------------------------------------------------

## v06
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
