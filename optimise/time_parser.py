import pandas as pd
from math import log
from itertools import tee

MAXN = 1048576
MAX_ITERS = 100000
df = pd.read_csv("times.csv").drop(columns=['machine', 'date'])
# get rows with tests > 1 second
df = df[(df.runtime >= 1)]  # FIXME: if the fastest is <1 but there are >1?
# group by "run type"
group_df = df.groupby(['file_name', 'maxN', 'entries', 'runner'])
# get the fastest of each run type only, slower times are overhead
min_dict = group_df.min().to_dict()["runtime"]

summary_dict = {v: {} for v in sorted(set(df["file_name"]))}

# TODO: I should probably look more into pandas ^_^U
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

for k_file, v_file in summary_dict.items():
    for k_runner, v_runner in v_file.items():
        maxN_lt_MAX_k = sorted(v_runner.get(1, {}).keys())
        maxN_lt_MAX_v = sorted(v_runner.get(1, {}).values())
        if maxN_lt_MAX_k and maxN_lt_MAX_k[-1] < MAXN:
            small, big = tee(maxN_lt_MAX_k)
            next(big)
            for s, b in zip(small, big):
                assert(s * 2 == b)
            small, big = tee(maxN_lt_MAX_v)
            next(big)
            time_size_ratio = [b / s for s, b in zip(small, big)]
            tsr_lt.append(time_size_ratio)
            v_runner["ts_ratio"] = sum(time_size_ratio) / len(time_size_ratio)
            v_runner["eta_MAX"] = (MAXN / maxN_lt_MAX_k[-1])\
                ** log(v_runner["ts_ratio"], 2)\
                * maxN_lt_MAX_v[-1]
            v_runner["eta_MAX_y"] = v_runner["eta_MAX"] / 3600 / 24 / 365
            v_runner["eta_MAX_iter"] = v_runner["eta_MAX"] * MAX_ITERS

        maxN_lt_MAX_v = sorted(v_runner.get(MAXN, {}).values())
        maxN_lt_MAX_k = sorted(v_runner.get(MAXN, {}).keys())
        if maxN_lt_MAX_k:
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

for tsr in tsr_lt:
    # Versions that follow this basic algorithm (v00-05) are O(n^3).
    assert(6.5 < tsr < 9)  # 2n -> 8x
    # Other paradigm algorithms are too fast to be here (<1s) on the machine I
    # ran (e.g. v06 is close to O(n)). Could happen on slower machines, so take
    # this assertion with a grain of salt, rather than a truth that must hold.


# TODO scripts to do for each csv timing:
#  - calculate speedups with previous version(s)
#  - ratio time/problem size increase for N increase
#  - ratio time/problem size increase for entries increase
#  - estimate time for N = 2^20
#  - estimate time for 1000 entries, 1 < N <= 2^20
#  - estimate time for 100.000 entries, 1 < N <= 2^20
#  - plotting charts?
