import pandas as pd
from math import log
from itertools import tee
from pprint import pformat
from copy import deepcopy

MAXN = 1048576
MAX_ITERS = 100000
FIRST = "v00"
ETA = "eta_MAX_iter"


def round_speedups(digits=2):
    rounded = {}
    for k, version in speedups.items():
        rounded[k] = {}
        for ratio, time in version.items():
            rounded[k][ratio] = round(time, digits)
    return rounded


def round_summary_dict(digits=2):
    for k, version in summary_dict.items():
        for lang, run_info in version.items():
            if not run_info.get(1048576):
                run_info["eta_MAXN"] = round(run_info["eta_MAXN"], digits)
                run_info["eta_MAXN_y"] = round(run_info["eta_MAXN_y"], digits)

            run_info["eta_MAX_iter"] = round(run_info["eta_MAX_iter"], digits)
            run_info["ts_ratio"] = round(run_info["ts_ratio"], digits)


df = pd.read_csv("times.csv").drop(columns=['machine', 'date'])
# get rows with tests >= 0.15 second
df = df[(df.runtime >= 0.15)]
# group by "run type"
group_df = df.groupby(['file_name', 'maxN', 'entries', 'runner'])
# get the fastest of each run type only, slower times are overhead
min_dict = group_df.min().to_dict()["runtime"]

summary_dict = {v: {} for v in sorted(set(df["file_name"]))}

# TODO: I should probably look more into pandas instead of doing this ^_^U
for k, v in min_dict.items():
    if not summary_dict[k[0]].get(k[3]):
        summary_dict[k[0]][k[3]] = {}
    if k[2] == 1:
        if not summary_dict[k[0]][k[3]].get(1):
            summary_dict[k[0]][k[3]][1] = {}
        summary_dict[k[0]][k[3]][1][k[1]] = v
    else:
        assert k[1] == MAXN
        if not summary_dict[k[0]][k[3]].get(MAXN):
            summary_dict[k[0]][k[3]][MAXN] = {}
        summary_dict[k[0]][k[3]][MAXN][k[2]] = v

# Time size ratios for a single calculation of size N <= 1048576
tsr_lt = []

# Reduce dictionary size removing smaller and less reliable Ns
for k_file, v_file in deepcopy(summary_dict).items():
    for k_runner, v_runner in v_file.items():
        maxN_lt_MAX_k = sorted(v_runner.get(1, {}).keys())[-3:]
        for k in v_runner.get(1, {}):
            if k not in maxN_lt_MAX_k:
                del summary_dict[k_file][k_runner][1][k]

        maxN_lt_MAX_k = sorted(v_runner.get(MAXN, {}).keys())[-3:]
        for k in v_runner.get(MAXN, {}):
            if k not in maxN_lt_MAX_k:
                del summary_dict[k_file][k_runner][MAXN][k]

# Calculate time_size_ratio + ETAs
for k_file, v_file in summary_dict.items():
    for k_runner, v_runner in v_file.items():
        maxN_lt_MAX_k = sorted(v_runner.get(1, {}).keys())
        maxN_lt_MAX_v = sorted(v_runner.get(1, {}).values())
        try:
            if maxN_lt_MAX_k and maxN_lt_MAX_k[-1] < MAXN:
                small, big = tee(maxN_lt_MAX_k)
                next(big)
                for s, b in zip(small, big):
                    assert(s * 2 == b)

                small, big = tee(maxN_lt_MAX_v)
                next(big)
                time_size_ratio = [b / s for s, b in zip(small, big)]
                tsr_lt += time_size_ratio
                ts = time_size_ratio
                v_runner["ts_ratio"] = sum(ts) / len(ts)
                v_runner["eta_MAXN"] = (MAXN / maxN_lt_MAX_k[-1])\
                    ** log(v_runner["ts_ratio"], 2)\
                    * maxN_lt_MAX_v[-1]
                v_runner["eta_MAXN_y"] = v_runner["eta_MAXN"] / 3600 / 24 / 365
                v_runner["eta_MAX_iter"] = v_runner["eta_MAXN"] * MAX_ITERS
        except Exception:
            # Probably `assert(s * 2 == b)` failed or got a divide by 0 on
            # `v_runner["ts_ratio"] = v_runner["ts_ratio"] = sum(ts) / len(ts)`
            # This may happen if there are too few times for different Ns or
            # that they are very close in value with the threshold set above at
            # `df = df[(df.runtime >= 0.3)]`. They can be safely ignored, but
            # if you want to play around with this and send a PR do.
            pass

        maxN_lt_MAX_k = sorted(v_runner.get(MAXN, {}).keys())
        maxN_lt_MAX_v = sorted(v_runner.get(MAXN, {}).values())
        if maxN_lt_MAX_k:
            if maxN_lt_MAX_k[0] > 1:
                v_runner["eta_MAXN"] = "N/A"  # TODO: not discard < 0.3s here?
            else:
                v_runner["eta_MAXN"] = maxN_lt_MAX_v[0]  # instead of estimate
            small, big = tee(maxN_lt_MAX_k)
            next(big)
            for s, b in zip(small, big):
                assert(s * 10 == b)
            small, big = tee(sorted(v_runner.get(MAXN, {}).values()))
            next(big)
            time_size_ratio = [b / s for s, b in zip(small, big)]
            v_runner["ts_ratio"] = sum(time_size_ratio) / len(time_size_ratio)
            v_runner["eta_MAX_iter"] = (MAX_ITERS / maxN_lt_MAX_k[-1])\
                ** log(v_runner["ts_ratio"], 10)\
                * maxN_lt_MAX_v[-1]

speedups = {k: {} for k in summary_dict.keys()}
python_1st = summary_dict[FIRST]["python3"][ETA]
pypy_1st = summary_dict[FIRST]["pypy3"][ETA]
cO0_1st = summary_dict[FIRST]["cO0"][ETA]
cO3_1st = summary_dict[FIRST]["cO3"][ETA]

for k, v in speedups.items():
    python = summary_dict[k].get("python3", {}).get(ETA)
    pypy = summary_dict[k].get("pypy3", {}).get(ETA)
    cO0 = summary_dict[k].get("cO0", {}).get(ETA)
    cO3 = summary_dict[k].get("cO3", {}).get(ETA)
    if python:
        v["total_python3"] = python_1st / python
        v["total_pypy3"] = pypy_1st / pypy
        v["total_vs_python3_pypy3"] = python_1st / pypy
        v["vs_python3_pypy3"] = python / pypy
    if cO0:
        v["total_cO0"] = cO0_1st / cO0
        v["total_cO3"] = cO3_1st / cO3
        v["total_vs_python3_cO3"] = python_1st / cO3
        v["vs_cO3_cO0"] = cO0 / cO3
        v["vs_python3_cO3"] = python / cO3

    if python and cO0:
        v["vs_cO0_pypy3"] = pypy / cO0
        v["vs_cO3_pypy3"] = pypy / cO3

previous, current = tee(speedups.keys())
next(current)

for pre, cur in zip(previous, current):
    cur_python3 = summary_dict[cur].get("python3", {}).get(ETA)
    cur_pypy3 = summary_dict[cur].get("pypy3", {}).get(ETA)
    pre_python3 = summary_dict[pre].get("python3", {}).get(ETA)
    pre_pypy3 = summary_dict[pre].get("pypy3", {}).get(ETA)
    cur_cO0 = summary_dict[cur].get("cO0", {}).get(ETA)
    cur_cO3 = summary_dict[cur].get("cO3", {}).get(ETA)
    pre_cO0 = summary_dict[pre].get("cO0", {}).get(ETA)
    pre_cO3 = summary_dict[pre].get("cO3", {}).get(ETA)

    if cur_python3:
        vs = speedups[cur]
        vs["prev_python3"] = pre_python3 / cur_python3
        vs["prev_pypy3"] = pre_pypy3 / cur_pypy3

    if cur_cO0 and pre_cO0:
        vs = speedups[cur]
        vs["prev_cO0"] = pre_cO0 / cur_cO0
        vs["prev_cO3"] = pre_cO3 / cur_cO3

speedups_2dec = round_speedups()
round_summary_dict()

print(f"""
Specifications
==============

Hardware
--------
- Model Name: MacBook Pro (Retina, Mid 2012)
- Model Identifier: MacBookPro10,1
- Processor Name: Intel Core i7
- Processor Speed: 2,3 GHz
- Number of Processors: 1
- Total Number of Cores: 4
- L2 Cache (per Core): 256 KB
- L3 Cache: 6 MB
- Hyper-Threading Technology: Enabled
- Memory: 16 GB

Timing
------
Best of ~5 runs. All values are times measured in seconds. For values of any
specific run see `times.csv`.

- First key: the script version that's run.
- Second key: the "interpreter" or in case of C++ the Optimisation level used.
- Third keys:
    - 1      : It means running the script just with 1 number.
               The subkeys are the value of N.
    - 1048576: It means running the script with numbers from 1 to 2^20,
               using a fixed seed so they are comparable.
               The subkeys are the amount of numbers given as input.

- eta_MAXN: estimated time to calculate N=2^20 with those settings.
- eta_MAX_y: estimated time to calculate N=2^20 with those settings in years.
- eta_MAX_iter: estimated time to calculate 100k entries with random N <= 2^20.
                the current results are pessimistic and an upper bound, but
                within the same order of magnitude of a realistic results.
                # TODO: calculate a more accurate upper bound.
- ts_ratio: aka "time-size ratio". This is used to calculate ETAs.
            How much the time increases when:
            - 1      : Size of N *= 2 (e.g. 8 -> O(n^3) complexity (2^3 -> 8).
            - 1048576: the ratio is how much time increases when N =* 10.

Speedup
-------
All ratios are calculated using "eta_MAX_iter".
When available it's a real value instead of an estimation.
Compare current script with chosen settings to
- prev_...    : ... equivalent previous script version.
- total_...   : ... equivalent of v00.
- total_vs... : ... equivalent with chosen settings of v00.
- vs_...      : ... other chosen settings.


Results summary
===============

Constants
---------
- MAXN={MAXN}
- MAX_ITERS={MAX_ITERS}

Timing
------
```
{pformat(summary_dict)}
```

Speedup
-------
```
{pformat(speedups_2dec)}
```
""")
