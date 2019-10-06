from bokeh.plotting import figure
from bokeh.models import FactorRange
from bokeh.io import show, output_file

# These 3 imports below are just needed for the outline
from bokeh.transform import cumsum
from math import pi
import pandas as pd


color_mapper = ["#1B9E77", "#D95F02", "#7570B3", "#E7298A", "#66A61E",
                "#E6AB02", "#A6761D", "#666666", "#FFFFFF"]

langs = ["cO0", "cO3", "pypy3", "python3"]
colors_by_lang = [color_mapper[l] for _ in range(10)
                  for l in range(len(langs))]

# data taken from timings.md (time_parser.py)
timing = {
    'v00': {'cO0': {1: {256: 2.59, 512: 21.63, 1024: 179.48},
                    'eta_MAXN': 286827022875.19,
                    'eta_MAXN_y': 9095.23,
                    'eta_MAX_iter': 2.8682702287519384e+16,
                    'ts_ratio': 8.32},
            'cO3': {1: {512: 4.31, 1024: 38.54, 2048: 341.58},
                    'eta_MAXN': 119977316154.07,
                    'eta_MAXN_y': 3804.46,
                    'eta_MAX_iter': 1.1997731615406542e+16,
                    'ts_ratio': 8.9},
            'pypy3': {1: {256: 3.64, 512: 28.87, 1024: 241.47},
                      'eta_MAXN': 311317829039.99,
                      'eta_MAXN_y': 9871.82,
                      'eta_MAX_iter': 3.113178290399926e+16,
                      'ts_ratio': 8.15},
            'python3': {1: {128: 4.52, 256: 35.87, 512: 299.12},
                        'eta_MAXN': 3098848073585.06,
                        'eta_MAXN_y': 98263.83,
                        'eta_MAX_iter': 3.098848073585063e+17,
                        'ts_ratio': 8.14}},
    'v01': {'cO0': {1: {256: 3.04, 512: 25.44, 1024: 211.12},
                    'eta_MAXN': 341072180331.29,
                    'eta_MAXN_y': 10815.33,
                    'eta_MAX_iter': 3.4107218033128636e+16,
                    'ts_ratio': 8.33},
            'cO3': {1: {512: 4.4, 1024: 39.04, 2048: 346.46},
                    'eta_MAXN': 118183005643.36,
                    'eta_MAXN_y': 3747.56,
                    'eta_MAX_iter': 1.181830056433571e+16,
                    'ts_ratio': 8.87},
            'pypy3': {1: {256: 3.37, 512: 26.35, 1024: 218.26},
                      'eta_MAXN': 249746960791.75,
                      'eta_MAXN_y': 7919.42,
                      'eta_MAX_iter': 2.4974696079174812e+16,
                      'ts_ratio': 8.05},
            'python3': {1: {128: 3.31, 256: 25.83, 512: 213.48},
                        'eta_MAXN': 1921924179705.58,
                        'eta_MAXN_y': 60943.82,
                        'eta_MAX_iter': 1.9219241797055837e+17,
                        'ts_ratio': 8.03}},
    'v02': {'cO0': {1: {256: 1.24, 512: 10.72, 1024: 92.54},
                    'eta_MAXN': 214224786250.93,
                    'eta_MAXN_y': 6793.02,
                    'eta_MAX_iter': 2.1422478625093428e+16,
                    'ts_ratio': 8.64},
            'cO3': {1: {512: 4.17, 1024: 36.72, 2048: 322.96},
                    'eta_MAXN': 102260168680.37,
                    'eta_MAXN_y': 3242.65,
                    'eta_MAX_iter': 1.0226016868036716e+16,
                    'ts_ratio': 8.8},
            'pypy3': {1: {256: 3.35, 512: 26.37, 1024: 218.67},
                      'eta_MAXN': 260005720623.93,
                      'eta_MAXN_y': 8244.73,
                      'eta_MAX_iter': 2.6000572062393276e+16,
                      'ts_ratio': 8.08},
            'python3': {1: {128: 1.56, 256: 12.3, 512: 100.11},
                        'eta_MAXN': 874018072785.71,
                        'eta_MAXN_y': 27714.93,
                        'eta_MAX_iter': 8.740180727857114e+16,
                        'ts_ratio': 8.01}},
    'v03': {'cO0': {1: {1024: 2.47, 2048: 19.72, 4096: 157.2},
                    'eta_MAXN': 2579145907.06,
                    'eta_MAXN_y': 81.78,
                    'eta_MAX_iter': 257914590706365.7,
                    'ts_ratio': 7.98},
            'cO3': {1: {2048: 3.31, 4096: 26.32, 8192: 209.53},
                    'eta_MAXN': 422873518.08,
                    'eta_MAXN_y': 13.41,
                    'eta_MAX_iter': 42287351807979.09,
                    'ts_ratio': 7.96},
            'pypy3': {1: {1024: 3.08, 2048: 23.17, 4096: 183.28},
                      'eta_MAXN': 2303923521.46,
                      'eta_MAXN_y': 73.06,
                      'eta_MAX_iter': 230392352146299.97,
                      'ts_ratio': 7.72},
            'python3': {1: {256: 3.6, 512: 29.2, 1024: 242.67},
                        'eta_MAXN': 337990550781.6,
                        'eta_MAXN_y': 10717.61,
                        'eta_MAX_iter': 3.379905507816048e+16,
                        'ts_ratio': 8.21}},
    'v04': {'cO0': {1: {2048: 3.6, 4096: 28.79, 8192: 230.35},
                    'eta_MAXN': 482712237.08,
                    'eta_MAXN_y': 15.31,
                    'eta_MAX_iter': 48271223708244.7,
                    'ts_ratio': 8.0},
            'cO3': {1: {2048: 1.43, 4096: 11.28, 8192: 89.75},
                    'eta_MAXN': 175795313.74,
                    'eta_MAXN_y': 5.57,
                    'eta_MAX_iter': 17579531374040.06,
                    'ts_ratio': 7.92},
            'pypy3': {1: {2048: 3.94, 4096: 30.13, 8192: 238.74},
                      'eta_MAXN': 413909895.89,
                      'eta_MAXN_y': 13.12,
                      'eta_MAX_iter': 41390989589397.98,
                      'ts_ratio': 7.79},
            'python3': {1: {256: 1.13, 512: 9.23, 1024: 74.79},
                        'eta_MAXN': 94995682417.6,
                        'eta_MAXN_y': 3012.29,
                        'eta_MAX_iter': 9499568241760338.0,
                        'ts_ratio': 8.14}},
    'v05': {'cO0': {1: {2048: 3.75, 4096: 30.13, 8192: 241.81},
                    'eta_MAXN': 520625227.88,
                    'eta_MAXN_y': 16.51,
                    'eta_MAX_iter': 52062522788156.68,
                    'ts_ratio': 8.03},
            'cO3': {1: {2048: 1.43, 4096: 11.26, 8192: 89.71},
                    'eta_MAXN': 175452729.91,
                    'eta_MAXN_y': 5.56,
                    'eta_MAX_iter': 17545272991061.91,
                    'ts_ratio': 7.92},
            'pypy3': {1: {2048: 3.02, 4096: 22.72, 8192: 179.73},
                      'eta_MAXN': 292904897.48,
                      'eta_MAXN_y': 9.29,
                      'eta_MAX_iter': 29290489747997.39,
                      'ts_ratio': 7.72},
            'python3': {1: {512: 6.06, 1024: 45.35, 2048: 386.37},
                        'eta_MAXN': 51952107958.34,
                        'eta_MAXN_y': 1647.39,
                        'eta_MAX_iter': 5195210795834112.0,
                        'ts_ratio': 8.0}},
    'v06': {'cO0': {1: {2048: 3.74, 4096: 29.42, 8192: 235.18},
                    'eta_MAXN': 463820004.27,
                    'eta_MAXN_y': 14.71,
                    'eta_MAX_iter': 46382000426526.76,
                    'ts_ratio': 7.93},
            'cO3': {1: {2048: 1.38, 4096: 10.92, 8192: 87.0},
                    'eta_MAXN': 173092162.69,
                    'eta_MAXN_y': 5.49,
                    'eta_MAX_iter': 17309216269203.18,
                    'ts_ratio': 7.94},
            'pypy3': {1: {4096: 18.88, 8192: 149.33, 16384: 1192.49},
                      'eta_MAXN': 300498934.49,
                      'eta_MAXN_y': 9.53,
                      'eta_MAX_iter': 30049893448980.14,
                      'ts_ratio': 7.95},
            'python3': {1: {512: 3.05, 1024: 24.37, 2048: 194.38},
                        'eta_MAXN': 25599760106.51,
                        'eta_MAXN_y': 811.76,
                        'eta_MAX_iter': 2559976010650566.0,
                        'ts_ratio': 7.98}},
    'v07': {'cO0': {1: {4096: 7.36, 8192: 58.93, 16384: 470.81},
                    'eta_MAXN': 123239755.57,
                    'eta_MAXN_y': 3.91,
                    'eta_MAX_iter': 12323975556632.53,
                    'ts_ratio': 8.0},
            'cO3': {1: {4096: 2.75, 8192: 21.87, 16384: 174.33},
                    'eta_MAXN': 44411167.6,
                    'eta_MAXN_y': 1.41,
                    'eta_MAX_iter': 4441116760176.71,
                    'ts_ratio': 7.96},
            'pypy3': {1: {4096: 4.95, 8192: 37.91, 16384: 299.91},
                      'eta_MAXN': 66756099.32,
                      'eta_MAXN_y': 2.12,
                      'eta_MAX_iter': 6675609931677.94,
                      'ts_ratio': 7.78},
            'python3': {1: {1024: 6.19, 2048: 48.98, 4096: 390.19},
                        'eta_MAXN': 6160810281.96,
                        'eta_MAXN_y': 195.36,
                        'eta_MAX_iter': 616081028196465.9,
                        'ts_ratio': 7.94}},
    'v08': {'cO0': {1048576: {100: 3.17, 1000: 33.32, 10000: 335.54},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 3452.92,
                    'ts_ratio': 10.29},
            'cO3': {1048576: {100: 2.06, 1000: 21.52, 10000: 216.92},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 2226.31,
                    'ts_ratio': 10.26},
            'pypy3': {1048576: {100: 5.36, 1000: 54.7, 10000: 550.21},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 5574.7,
                      'ts_ratio': 10.13},
            'python3': {1: {262144: 0.3, 524288: 0.56, 1048576: 1.1},
                        1048576: {10: 4.23, 100: 51.48, 1000: 531.21},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 67165.41,
                        'ts_ratio': 11.24}},
    'v09': {'cO0': {1048576: {100: 0.95, 1000: 9.93, 10000: 100.21},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 1029.37,
                    'ts_ratio': 10.27},
            'cO3': {1048576: {1000: 6.82, 10000: 68.56, 100000: 689.35},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 689.35,
                    'ts_ratio': 10.05},
            'pypy3': {1: {2: 0.44},
                      1048576: {1000: 13.41, 10000: 133.27, 100000: 1349.58},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 1349.58,
                      'ts_ratio': 10.03},
            'python3': {1048576: {100: 4.19, 1000: 43.84, 10000: 441.42},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 4531.59,
                        'ts_ratio': 10.27}},
    'v10': {'cO0': {1048576: {100: 0.94, 1000: 9.87, 10000: 99.51},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 1024.06,
                    'ts_ratio': 10.29},
            'cO3': {1048576: {1000: 6.69, 10000: 67.1, 100000: 675.46},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 675.46,
                    'ts_ratio': 10.05},
            'pypy3': {1: {2: 0.45},
                      1048576: {1000: 13.37, 10000: 133.27, 100000: 1342.05},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 1342.05,
                      'ts_ratio': 10.02},
            'python3': {1048576: {100: 3.26, 1000: 33.89, 10000: 343.85},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 3531.64,
                        'ts_ratio': 10.27}},
    'v11': {'cO0': {1048576: {100: 0.94, 1000: 9.89, 10000: 99.83},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 1029.01,
                    'ts_ratio': 10.31},
            'cO3': {1048576: {1000: 6.66, 10000: 67.19, 100000: 675.97},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 675.97,
                    'ts_ratio': 10.07},
            'pypy3': {1: {131072: 0.31},
                      1048576: {1000: 13.34, 10000: 133.25, 100000: 1340.49},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 1340.49,
                      'ts_ratio': 10.02},
            'python3': {1048576: {100: 3.26, 1000: 33.8, 10000: 342.66},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 3513.29,
                        'ts_ratio': 10.25}},
    'v12': {'cO0': {1048576: {1000: 0.6, 10000: 5.93, 100000: 59.45},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 59.45,
                    'ts_ratio': 9.95},
            'cO3': {1048576: {1000: 0.16, 10000: 1.54, 100000: 15.46},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 15.46,
                    'ts_ratio': 9.83},
            'pypy3': {1: {2: 0.45, 524288: 0.33, 1048576: 0.41},
                      1048576: {100: 3.84, 1000: 35.01, 10000: 327.67},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 3027.1,
                      'ts_ratio': 9.24},
            'python3': {1048576: {100: 4.35, 1000: 42.88, 10000: 431.46},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 4297.23,
                        'ts_ratio': 9.96}},
    'v13': {'cO0': {1048576: {1000: 0.03, 10000: 0.03, 100000: 0.07},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 0.07,
                    'ts_ratio': 1.67},
            'cO3': {1048576: {1000: 0.02, 10000: 0.02, 100000: 0.05},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 0.05,
                    'ts_ratio': 1.75},
            'pypy3': {1: {262144: 0.51, 524288: 0.51, 1048576: 0.51},
                      1048576: {1000: 0.54, 10000: 0.56, 100000: 0.68},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 0.68,
                      'ts_ratio': 1.13},
            'python3': {1: {262144: 0.87, 524288: 0.87, 1048576: 0.87},
                        1048576: {1000: 0.87, 10000: 0.89, 100000: 1.08},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 1.08,
                        'ts_ratio': 1.12}},
    'v14': {'cO0': {1048576: {1000: 0.75, 10000: 0.76, 100000: 0.9},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 0.9,
                    'ts_ratio': 1.1},
            'cO3': {1048576: {1000: 0.16, 10000: 0.15, 100000: 0.22},
                    'eta_MAXN': 'N/A',
                    'eta_MAX_iter': 0.22,
                    'ts_ratio': 1.22},
            'pypy3': {1: {262144: 0.31, 524288: 0.31, 1048576: 0.31},
                      1048576: {1000: 0.34, 10000: 0.37, 100000: 0.49},
                      'eta_MAXN': 'N/A',
                      'eta_MAX_iter': 0.49,
                      'ts_ratio': 1.21},
            'python3': {1: {262144: 0.4, 524288: 0.41, 1048576: 0.4},
                        1048576: {1000: 0.41, 10000: 0.42, 100000: 0.61},
                        'eta_MAXN': 'N/A',
                        'eta_MAX_iter': 0.61,
                        'ts_ratio': 1.24}}}


speedup = {'v00': {'total_cO0': 1.0,
                   'total_cO3': 1.0,
                   'total_pypy3': 1.0,
                   'total_python3': 1.0,
                   'total_vs_python3_cO3': 25.83,
                   'total_vs_python3_pypy3': 9.95,
                   'vs_cO0_pypy3': 1.09,
                   'vs_cO3_cO0': 2.39,
                   'vs_cO3_pypy3': 2.59,
                   'vs_python3_cO3': 25.83,
                   'vs_python3_pypy3': 9.95},
           'v01': {'prev_cO0': 0.84,
                   'prev_cO3': 1.02,
                   'prev_pypy3': 1.25,
                   'prev_python3': 1.61,
                   'total_cO0': 0.84,
                   'total_cO3': 1.02,
                   'total_pypy3': 1.25,
                   'total_python3': 1.61,
                   'total_vs_python3_cO3': 26.22,
                   'total_vs_python3_pypy3': 12.41,
                   'vs_cO0_pypy3': 0.73,
                   'vs_cO3_cO0': 2.89,
                   'vs_cO3_pypy3': 2.11,
                   'vs_python3_cO3': 16.26,
                   'vs_python3_pypy3': 7.7},
           'v02': {'prev_cO0': 1.59,
                   'prev_cO3': 1.16,
                   'prev_pypy3': 0.96,
                   'prev_python3': 2.2,
                   'total_cO0': 1.34,
                   'total_cO3': 1.17,
                   'total_pypy3': 1.2,
                   'total_python3': 3.55,
                   'total_vs_python3_cO3': 30.3,
                   'total_vs_python3_pypy3': 11.92,
                   'vs_cO0_pypy3': 1.21,
                   'vs_cO3_cO0': 2.09,
                   'vs_cO3_pypy3': 2.54,
                   'vs_python3_cO3': 8.55,
                   'vs_python3_pypy3': 3.36},
           'v03': {'prev_cO0': 83.06,
                   'prev_cO3': 241.82,
                   'prev_pypy3': 112.85,
                   'prev_python3': 2.59,
                   'total_cO0': 111.21,
                   'total_cO3': 283.72,
                   'total_pypy3': 135.13,
                   'total_python3': 9.17,
                   'total_vs_python3_cO3': 7328.07,
                   'total_vs_python3_pypy3': 1345.03,
                   'vs_cO0_pypy3': 0.89,
                   'vs_cO3_cO0': 6.1,
                   'vs_cO3_pypy3': 5.45,
                   'vs_python3_cO3': 799.27,
                   'vs_python3_pypy3': 146.7},
           'v04': {'prev_cO0': 5.34,
                   'prev_cO3': 2.41,
                   'prev_pypy3': 5.57,
                   'prev_python3': 3.56,
                   'total_cO0': 594.2,
                   'total_cO3': 682.48,
                   'total_pypy3': 752.14,
                   'total_python3': 32.62,
                   'total_vs_python3_cO3': 17627.59,
                   'total_vs_python3_pypy3': 7486.77,
                   'vs_cO0_pypy3': 0.86,
                   'vs_cO3_cO0': 2.75,
                   'vs_cO3_pypy3': 2.35,
                   'vs_python3_cO3': 540.38,
                   'vs_python3_pypy3': 229.51},
           'v05': {'prev_cO0': 0.93,
                   'prev_cO3': 1.0,
                   'prev_pypy3': 1.41,
                   'prev_python3': 1.83,
                   'total_cO0': 550.93,
                   'total_cO3': 683.82,
                   'total_pypy3': 1062.86,
                   'total_python3': 59.65,
                   'total_vs_python3_cO3': 17662.01,
                   'total_vs_python3_pypy3': 10579.71,
                   'vs_cO0_pypy3': 0.56,
                   'vs_cO3_cO0': 2.97,
                   'vs_cO3_pypy3': 1.67,
                   'vs_python3_cO3': 296.1,
                   'vs_python3_pypy3': 177.37},
           'v06': {'prev_cO0': 1.12,
                   'prev_cO3': 1.01,
                   'prev_pypy3': 0.97,
                   'prev_python3': 2.03,
                   'total_cO0': 618.4,
                   'total_cO3': 693.14,
                   'total_pypy3': 1036.0,
                   'total_python3': 121.05,
                   'total_vs_python3_cO3': 17902.88,
                   'total_vs_python3_pypy3': 10312.34,
                   'vs_cO0_pypy3': 0.65,
                   'vs_cO3_cO0': 2.68,
                   'vs_cO3_pypy3': 1.74,
                   'vs_python3_cO3': 147.9,
                   'vs_python3_pypy3': 85.19},
           'v07': {'prev_cO0': 3.76,
                   'prev_cO3': 3.9,
                   'prev_pypy3': 4.5,
                   'prev_python3': 4.16,
                   'total_cO0': 2327.39,
                   'total_cO3': 2701.51,
                   'total_pypy3': 4663.51,
                   'total_python3': 502.99,
                   'total_vs_python3_cO3': 69776.33,
                   'total_vs_python3_pypy3': 46420.45,
                   'vs_cO0_pypy3': 0.54,
                   'vs_cO3_cO0': 2.77,
                   'vs_cO3_pypy3': 1.5,
                   'vs_python3_cO3': 138.72,
                   'vs_python3_pypy3': 92.29},
           'v08': {'prev_cO0': 3569146484.84,
                   'prev_cO3': 1994835571.1,
                   'prev_pypy3': 1197482765.67,
                   'prev_python3': 9172593998.95,
                   'total_cO0': 8306797232342.23,
                   'total_cO3': 5389072859686.84,
                   'total_pypy3': 5584474508517.77,
                   'total_python3': 4613755974051.53,
                   'total_vs_python3_cO3': 139192295551980.84,
                   'total_vs_python3_pypy3': 55587687110853.19,
                   'vs_cO0_pypy3': 1.61,
                   'vs_cO3_cO0': 1.55,
                   'vs_cO3_pypy3': 2.5,
                   'vs_python3_cO3': 30.17,
                   'vs_python3_pypy3': 12.05},
           'v09': {'prev_cO0': 3.35,
                   'prev_cO3': 3.23,
                   'prev_pypy3': 4.13,
                   'prev_python3': 14.82,
                   'total_cO0': 27864305290040.69,
                   'total_cO3': 17404412294779.93,
                   'total_pypy3': 23067756564263.89,
                   'total_python3': 68383174845652.1,
                   'total_vs_python3_cO3': 449531888530508.9,
                   'total_vs_python3_pypy3': 229615737754343.06,
                   'vs_cO0_pypy3': 1.31,
                   'vs_cO3_cO0': 1.49,
                   'vs_cO3_pypy3': 1.96,
                   'vs_python3_cO3': 6.57,
                   'vs_python3_pypy3': 3.36},
           'v10': {'prev_cO0': 1.01,
                   'prev_cO3': 1.02,
                   'prev_pypy3': 1.01,
                   'prev_python3': 1.28,
                   'total_cO0': 28008790151692.72,
                   'total_cO3': 17762312520958.37,
                   'total_pypy3': 23197185577287.93,
                   'total_python3': 87745220070904.95,
                   'total_vs_python3_cO3': 458775956175800.6,
                   'total_vs_python3_pypy3': 230904070160207.38,
                   'vs_cO0_pypy3': 1.31,
                   'vs_cO3_cO0': 1.52,
                   'vs_cO3_pypy3': 1.99,
                   'vs_python3_cO3': 5.23,
                   'vs_python3_pypy3': 2.63},
           'v11': {'prev_cO0': 1.0,
                   'prev_cO3': 1.0,
                   'prev_pypy3': 1.0,
                   'prev_python3': 1.01,
                   'total_cO0': 27873987398924.26,
                   'total_cO3': 17748911365011.08,
                   'total_pypy3': 23224181384418.58,
                   'total_python3': 88203657644416.22,
                   'total_vs_python3_cO3': 458429822859751.6,
                   'total_vs_python3_pypy3': 231172785592213.53,
                   'vs_cO0_pypy3': 1.3,
                   'vs_cO3_cO0': 1.52,
                   'vs_cO3_pypy3': 1.98,
                   'vs_python3_cO3': 5.2,
                   'vs_python3_pypy3': 2.62},
           'v12': {'prev_cO0': 17.31,
                   'prev_cO3': 43.72,
                   'prev_pypy3': 0.44,
                   'prev_python3': 0.82,
                   'total_cO0': 482467658326650.7,
                   'total_cO3': 776049910440267.9,
                   'total_pypy3': 10284360372952.34,
                   'total_python3': 72112608034080.28,
                   'total_vs_python3_cO3': 2.0044295430692516e+16,
                   'total_vs_python3_pypy3': 102370206126819.2,
                   'vs_cO0_pypy3': 50.92,
                   'vs_cO3_cO0': 3.85,
                   'vs_cO3_pypy3': 195.8,
                   'vs_python3_cO3': 277.96,
                   'vs_python3_pypy3': 1.42},
           'v13': {'prev_cO0': 849.29,
                   'prev_cO3': 309.2,
                   'prev_pypy3': 4451.62,
                   'prev_python3': 3978.92,
                   'total_cO0': 4.097528898217055e+17,
                   'total_cO3': 2.399546323081308e+17,
                   'total_pypy3': 4.578203368235185e+16,
                   'total_python3': 2.869303771838021e+17,
                   'total_vs_python3_cO3': 6.197696147170126e+18,
                   'total_vs_python3_pypy3': 4.557129519978033e+17,
                   'vs_cO0_pypy3': 9.71,
                   'vs_cO3_cO0': 1.4,
                   'vs_cO3_pypy3': 13.6,
                   'vs_python3_cO3': 21.6,
                   'vs_python3_pypy3': 1.59},
           'v14': {'prev_cO0': 0.08,
                   'prev_cO3': 0.23,
                   'prev_pypy3': 1.39,
                   'prev_python3': 1.77,
                   'total_cO0': 3.186966920835487e+16,
                   'total_cO3': 5.453514370639338e+16,
                   'total_pypy3': 6.353425082448829e+16,
                   'total_python3': 5.080078809155841e+17,
                   'total_vs_python3_cO3': 1.4085673061750287e+18,
                   'total_vs_python3_pypy3': 6.324179742010333e+17,
                   'vs_cO0_pypy3': 0.54,
                   'vs_cO3_cO0': 4.09,
                   'vs_cO3_pypy3': 2.23,
                   'vs_python3_cO3': 2.77,
                   'vs_python3_pypy3': 1.24}}

# From time_parser but using more data points than above
ts_ratios = {
    'v00': {'cO0': {1: {128: 0.31, 256: 2.59, 512: 21.63, 1024: 179.48}},
            'cO3': {1: {256: 0.48, 512: 4.31, 1024: 38.54, 2048: 341.58}},
            'pypy3': {1: {128: 0.61, 256: 3.64, 512: 28.87, 1024: 241.47}},
            'python3': {1: {64: 0.59, 128: 4.52, 256: 35.87, 512: 299.12}}},
    'v01': {'cO0': {1: {128: 0.36, 256: 3.04, 512: 25.44, 1024: 211.12}},
            'cO3': {1: {256: 0.49, 512: 4.4, 1024: 39.04, 2048: 346.46}},
            'pypy3': {1: {128: 0.56, 256: 3.37, 512: 26.35, 1024: 218.26}},
            'python3': {1: {64: 0.44, 128: 3.31, 256: 25.83, 512: 213.48}}},
    'v02': {'cO0': {1: {256: 1.24, 512: 10.72, 1024: 92.54}},
            'cO3': {1: {256: 0.47, 512: 4.17, 1024: 36.72, 2048: 322.96}},
            'pypy3': {1: {128: 0.56, 256: 3.35, 512: 26.37, 1024: 218.67}},
            'python3': {1: {128: 1.56, 256: 12.3, 512: 100.11}}},
    'v03': {'cO0': {1: {512: 0.31, 1024: 2.47, 2048: 19.72, 4096: 157.2}},
            'cO3': {1: {1024: 0.42, 2048: 3.31, 4096: 26.32, 8192: 209.53}},
            'pypy3': {1: {512: 0.54, 1024: 3.08, 2048: 23.17, 4096: 183.28}},
            'python3': {1: {128: 0.48, 256: 3.6, 512: 29.2, 1024: 242.67}}},
    'v04': {'cO0': {1: {1024: 0.45, 2048: 3.6, 4096: 28.79, 8192: 230.35}},
            'cO3': {1: {2048: 1.43, 4096: 11.28, 8192: 89.75}},
            'pypy3': {1: {1024: 0.64, 2048: 3.94, 4096: 30.13, 8192: 238.74}},
            'python3': {1: {256: 1.13, 512: 9.23, 1024: 74.79}}},
    'v05': {'cO0': {1: {1024: 0.46, 2048: 3.75, 4096: 30.13, 8192: 241.81}},
            'cO3': {1: {2048: 1.43, 4096: 11.26, 8192: 89.71}},
            'pypy3': {1: {1024: 0.52, 2048: 3.02, 4096: 22.72, 8192: 179.73}},
            'python3': {1: {256: 0.7, 512: 6.06, 1024: 45.35, 2048: 386.37}}},
    'v06': {'cO0': {1: {1024: 0.47, 2048: 3.74, 4096: 29.42, 8192: 235.18}},
            'cO3': {1: {2048: 1.38, 4096: 10.92, 8192: 87.0}},
            'pypy3': {1: {2048: 2.5, 4096: 18.9, 8192: 149.33, 16384: 1192.5}},
            'python3': {1: {256: 0.37, 512: 3.05, 1024: 24.37, 2048: 194.38}}},
    'v07': {'cO0': {1: {2048: 0.92, 4096: 7.36, 8192: 58.93, 16384: 470.81}},
            'cO3': {1: {2048: 0.35, 4096: 2.75, 8192: 21.87, 16384: 174.33}},
            'pypy3': {1: {2048: 0.78, 4096: 4.95, 8192: 37.91, 16384: 299.91}},
            'python3': {1: {512: 0.8, 1024: 6.19, 2048: 48.98, 4096: 390.19}}},
    'v08': {'cO0': {1048576: {10: 0.3, 100: 3.17, 1000: 33.32, 10000: 335.54}},
            'cO3': {1048576: {100: 2.06, 1000: 21.52, 10000: 216.92}},
            'pypy3': {1048576: {10: 0.6, 100: 5.36, 1000: 54.7, 10000: 550.2}},
            'python3': {1: {262144: 0.3, 524288: 0.56, 1048576: 1.1},
                        1048576: {10: 4.23, 100: 51.48, 1000: 531.21}}},
    'v09': {'cO0': {1048576: {100: 0.95, 1000: 9.93, 10000: 100.21}},
            'cO3': {1048576: {100: 0.65,
                              1000: 6.82,
                              10000: 68.56,
                              100000: 689.35}},
            'pypy3': {1: {2: 0.44},
                      1048576: {100: 1.43,
                                1000: 13.41,
                                10000: 133.27,
                                100000: 1349.58}},
            'python3': {1048576: {10: 0.37,
                                  100: 4.19,
                                  1000: 43.84,
                                  10000: 441.42}}},
    'v10': {
        'cO0': {1048576: {100: 0.94, 1000: 9.87, 10000: 99.51}},
        'cO3': {1048576: {100: 0.64, 1000: 6.69, 10000: 67.1, 100000: 675.46}},
        'pypy3': {1: {2: 0.45},
                  1048576: {100: 1.43,
                            1000: 13.37,
                            10000: 133.27,
                            100000: 1342.05}},
        'python3': {1048576: {10: 0.31,
                              100: 3.26,
                              1000: 33.89,
                              10000: 343.85}}},
    'v11': {
        'cO0': {1048576: {100: 0.94, 1000: 9.89, 10000: 99.83}},
        'cO3': {1048576: {100: 0.64,
                          1000: 6.66,
                          10000: 67.19,
                          100000: 675.97}},
        'pypy3': {1: {131072: 0.31},
                  1048576: {100: 1.43,
                            1000: 13.34,
                            10000: 133.25,
                            100000: 1340.49}},
        'python3': {1048576: {10: 0.33,
                              100: 3.26,
                              1000: 33.8,
                              10000: 342.66}}},
    'v12': {
        'cO0': {1048576: {1000: 0.6, 10000: 5.93, 100000: 59.45}},
        'cO3': {1048576: {10000: 1.54, 100000: 15.46}},
        'pypy3': {1: {2: 0.45, 524288: 0.33, 1048576: 0.41},
                  1048576: {10: 0.67, 100: 3.84, 1000: 35.01, 10000: 327.67}},
        'python3': {1048576: {10: 0.5,
                              100: 4.35,
                              1000: 42.88,
                              10000: 431.46}}},
    'v13': {
        'cO0': {1048576: {100: 0.03, 1000: 0.03, 10000: 0.03, 100000: 0.07}},
        'cO3': {1048576: {100: 0.02, 1000: 0.02, 10000: 0.02, 100000: 0.05}},
        'pypy3': {1: {131072: 0.51, 262144: 0.51, 524288: 0.51, 1048576: 0.51},
                  1048576: {100: 0.51, 1000: 0.54, 10000: 0.56, 100000: 0.68}},
        'python3': {1: {131072: 0.87,
                        262144: 0.87,
                        524288: 0.87,
                        1048576: 0.87},
                    1048576: {100: 0.87,
                              1000: 0.87,
                              10000: 0.89,
                              100000: 1.08}}},
    'v14': {
        'cO0': {1048576: {100: 0.75, 1000: 0.75, 10000: 0.76, 100000: 0.9}},
        'cO3': {1048576: {100: 0.16, 1000: 0.16, 10000: 0.15, 100000: 0.22}},
        'pypy3': {1: {131072: 0.31, 262144: 0.31, 524288: 0.31, 1048576: 0.31},
                  1048576: {100: 0.31, 1000: 0.34, 10000: 0.37, 100000: 0.49}},
        'python3': {1: {131072: 0.41, 262144: 0.4, 524288: 0.41, 1048576: 0.4},
                    1048576: {100: 0.4,
                              1000: 0.41,
                              10000: 0.42,
                              100000: 0.61}}}}


def common_plot_cfg(p, legend=langs, legend_position="top_right", color=None):
    p.title.text_font_size = '24pt'
    p.y_range.start = 0
    # p.x_range.start = 0
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    p.toolbar.autohide = True
    p.xaxis.axis_label_text_font_size = '18pt'
    p.yaxis.axis_label_text_font_size = '18pt'
    p.yaxis.major_label_text_font_size = '15pt'
    p.plot_height = 600
    p.plot_width = 800

    if legend:
        data = dict(types=legend, values=range(len(legend)),
                    color=colors_by_lang[:len(legend)])
        if color:
            data["color"] = color
        p.vbar(x="types", top="values", width=0, alpha=0.8,
               color="color", legend="types",
               source=data)

        p.legend.location = legend_position
        p.legend.label_text_font_size = '21pt'
        p.legend.glyph_height = 45
        p.legend.glyph_width = 45


def ETA_plot(vmin=0, vmax=7, eta="eta_MAXN_y", title_sufix="N=2^20",
             unit="years"):
    output_file(f"plot_eta{vmax}.html")

    timing_subset = {k: v for k, v in timing.items()
                     if vmin <= int(k[1:]) <= vmax}
    timing_factors = []
    timing_ETA = []
    python3_line = []
    for version, language in timing_subset.items():
        for lang_name, times in language.items():
            timing_factors.append((version, lang_name))
            timing_ETA.append(times[eta])
            if lang_name == "python3":
                python3_line.append(times[eta])

    p = figure(
        title=f"Estimated time to compute {title_sufix}",
        x_range=FactorRange(*timing_factors))

    p.xaxis.axis_label = 'Code version'
    p.yaxis.axis_label = f'Elapsed time ({unit})'

    p.vbar(x=timing_factors, top=timing_ETA, width=1, alpha=0.8,
           color=colors_by_lang)

    p.line(x=[f for f in timing_factors if f[1] == "python3"],
           y=python3_line, color="red", line_width=6, line_dash='dashed')

    common_plot_cfg(p)

    show(p)


def speedup_prev_plot(vmin=1, vmax=7, init="v00"):
    output_file(f"plot_speedup{vmax}.html")

    speedup_subset = {k: v for k, v in speedup.items()
                      if vmin <= int(k[1:]) <= vmax}
    speedup_factors = [(init, l) for l in langs]
    speedup_relative_X = [1, 1, 1, 1]

    for version, info in speedup_subset.items():
        speedup_factors += [(version, l) for l in langs]
        speedup_relative_X += [info[f"prev_{l}"] for l in langs]

    p = figure(
        title="Incremental speedups (i.e. current vs previous)",
        x_range=FactorRange(*speedup_factors))

    p.xaxis.axis_label = 'Code version'
    p.yaxis.axis_label = 'X times faster'

    p.vbar(x=speedup_factors, top=speedup_relative_X, width=1, alpha=0.8,
           color=colors_by_lang)

    common_plot_cfg(p, legend_position="top_left")

    show(p)


def size_complexity_plot(vmin=1, vmax=7, ratio_base="8", index=1,
                         legend_loc="bottom_right"):

    output_file(f"plot_size_complexity{vmax}.html")

    ts_ratios_subset = {k: v for k, v in ts_ratios.items()
                        if vmin <= int(k[1:]) <= vmax}
    complexity_time = []
    complexity_size = []
    colors = []

    p = figure(
        title="Time vs size for Python3. Log scale",
        x_axis_type="log",
        y_axis_type="log")
    if ratio_base:
        p.match_aspect = True
        p.aspect_scale = 1 / float(ratio_base)
        p.title.text += f"; aspect ratio=1/{ratio_base}."

    p.xaxis.axis_label = 'Problem size (N))'
    p.yaxis.axis_label = 'Elapsed time (seconds)'

    for version, language in ts_ratios_subset.items():
        complexity_time = list(language["python3"][index].values())
        complexity_size = list(language["python3"][index].keys())
        colors = [color_mapper[int(version[1:]) - vmin]] * len(
            language["python3"][index])
        p.circle(complexity_size, complexity_time, fill_alpha=1, size=20,
                 color=colors, legend=version)

    p.legend.location = legend_loc
    p.legend.label_text_font_size = '18pt'
    p.legend.glyph_height = 45
    p.legend.glyph_width = 45

    common_plot_cfg(p, legend=None)
    p.xaxis.major_label_text_font_size = '15pt'

    show(p)


def speedup_vs_plot(vmin=0, vmax=14):
    output_file(f"plot_speedup_vs{vmax}.html")

    vs = ["vs_python3_pypy3", "vs_python3_cO3"]
    speedup_subset = {k: v for k, v in speedup.items()
                      if vmin <= int(k[1:]) <= vmax}
    speedup_factors = []
    speedup_relative_X = []

    for version, info in speedup_subset.items():
        speedup_factors += [(version, l.split("_")[-1]) for l in vs]
        speedup_relative_X += [info[l] for l in vs]

    p = figure(
        title="Relative speedups (i.e. Python3 vs (PyPy3/g++ -O3))",
        x_range=FactorRange(*speedup_factors))

    p.xaxis.axis_label = 'Code version'
    p.yaxis.axis_label = 'X times faster'

    p.vbar(x=speedup_factors, top=speedup_relative_X, width=1, alpha=0.8,
           color=["red", "blue"] * (vmax + 1))

    common_plot_cfg(p, legend=["PyPy3", "cO3"], color=["red", "blue"])

    show(p)


def outline():
    output_file(f"outline.html")

    x = {
        "Problem definition": 12,
        "Optimisations I": 27,
        "Compilers": 10,
        "Optimisations II": 13,
        "Profilers": 5,
        "Optimisations III": 11,
        "Conclusions": 21
    }

    data = pd.Series(x).reset_index(name='time').rename(
        columns={'index': 'section'})
    data['angle'] = data['time'] / data['time'].sum() * 2 * pi
    data['color'] = [color_mapper[i % 2 or i] for i in range(len(x))]
    p = figure(plot_width=800, title="Outline", toolbar_location=None,
               tools="hover", tooltips="@section: @time", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=0, radius=0.4, start_angle=cumsum(
        'angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='section', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    p.title.text_font_size = '24pt'
    p.legend.label_text_font_size = '21pt'
    p.legend.glyph_height = 45
    p.legend.glyph_width = 45

    show(p)


ETA_plot()
speedup_prev_plot()
size_complexity_plot()

ETA_plot(vmin=8, vmax=14, eta="eta_MAX_iter",
         title_sufix="100k N<=2^20", unit="seconds")
speedup_prev_plot(vmin=9, vmax=14, init="v08")
size_complexity_plot(vmin=8, vmax=14, ratio_base=None,
                     index=1048576, legend_loc="top_right")
speedup_vs_plot()

outline()
