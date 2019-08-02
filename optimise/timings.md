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

ETA N=1.05M -> 221.459.251.200s -> 2.563.185 days -> 7.022 years
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

ETA N 1.05M -> 84.221.624.320s -> 974.787 days -> 2.670 years
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

ETA N 1.05M -> 17.753.649.971s -> 205.482 days -> 563 years
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

ETA N 1.05M -> 6.590.593.761s -> 76.280 days -> 209 years
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

ETA N 1.05M -> 3.342.629.601s -> 38.688 days -> 106 years
Total speedup    66.25x
Incr. speedup     1.97x

## v05
v05.py took 0.03 for N = 16.
v05.py took 0.04 for N = 32.
v05.py took 0.04 for N = 64.
v05.py took 0.07 for N = 128.
v05.py took 0.26 for N = 256.
v05.py took 2.03 for N = 512.
v05.py took 16.05 for N = 1024.
v05.py took 124.52 for N = 2048.
v05.py took 981.06 for N = 4096.

ETA N 1.05M -> 2.057.431.941s -> 23.813 days -> 65.2 years
Total speedup     107.64x
Incr. speedup       1.63x

# Times (pypy)
N*2 -> t*8 (double the size of N -> multiply by 8 required time). For very small numbers < 8x

## v00pypy
v00.py took 0.17 for N = 16.
v00.py took 0.18 for N = 32.
v00.py took 0.22 for N = 64.
v00.py took 0.58 for N = 128.
v00.py took 3.48 for N = 256.
v00.py took 27.47 for N = 512.
v00.py took 221.88 for N = 1024.
v00.py took 1877.11 for N = 2048.

ETA N 1.05M -> 31.492.679.925s -> 364.498 days -> 998 year
Total speedup       7.03x
PyPy  speedup       7.03x

# v05pypy
v05.py took 0.14 for N = 16.
v05.py took 0.14 for N = 32.
v05.py took 0.15 for N = 64.
v05.py took 0.15 for N = 128.
v05.py took 0.15 for N = 256.
v05.py took 0.18 for N = 512.
v05.py took 0.36 for N = 1024.
v05.py took 1.68 for N = 2048.
v05.py took 12.00 for N = 4096.
v05.py took 93.95 for N = 8192.
v05.py took 746.35 for N = 16384.
v05.py took 6000.96 for N = 32768.

ETA N 1.05M -> 196.639.457s -> 2.276 days -> 6.23 years
Total speedup       1126.21x
PyPy  speedup         10.46x
