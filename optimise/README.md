# From > 1 Billion years to < 1 second

Presentation on the topic of code optimisation given at PyCon Sweden. Learn 10+ techniques applicable in a wide variety of situations and see how Python performance compares to C++.
[![YouTube link to the talk](https://raw.githubusercontent.com/isaacbernat/presentations/master/optimise/images/video_preview_with_play_button.png "YouTube link to the talk")](https://youtu.be/asZ0SDTKqvM)

Additional content, references and notes supporting the slides are found in `final.md`. More info in the section *How to run the presentation* below.

## Content
### Abstract (50-word version)
Adding resources to speed up processes isn't always feasible. This talk presents a simple problem and how to achieve >10^18x speedups on a regular laptop. Be warned, as overall time is reduced, minuscule overheads become gigantic. Nevertheless, most techniques can still be effective in more general contexts.

### Abstract (150-word version)
The goal of this talk is to empower people with over a dozen optimisation techniques which may be effectively used in a wide variety of situations, even beyond Python.

I will present best practices, typical pitfalls and common tools, but the main focus will be on a practical approach. I will showcase a small problem and a naive solution, just a few lines of Python, so that it's easily understood. Iteratively I will apply each optimisation, explain the reasoning behind it and note how execution time is reduced. By the end of the talk, one will see how the code evolved from something that would take > 1 billion years to compute to < 1 second on a regular laptop.

I will also compare running times between Python, PyPy and C++ implementations (one being just a few milliseconds), and show how the same techniques may achieve vastly different speedups from the Python versions.

### File structure
#### code
Contains all the Python code and C++ ports used for the presentation.
- **v05_bytecode:** contains dissassembled CPython bytecode for v05 and v06 used in slide 19.
- **pprofile_output:** contains the full profiler output of some Python versions used in slides 32-33.

### plots
Contains the interactive plots used for the presentation and a Python file to generate them using bokeh.

#### batch_tester.py
Just a few lines of code, but here goes a description: Runs all Python files in batches of increasing input sizes using CPython and using PyPy. For each combination of version + interpreter + input size it will try to run it 5 times (but will stop and increase size if that already took more than 600 seconds). The same happens for C++, it is compiled with and without -O3 optimisation flag and run.
It exhaustively verifies that the output of each run is correct and records runtimes on `times.csv`.

#### tester.py
A simple CLI to test individual versions for speed and correctness. Used by `batch_tester.py` but may be called individually (e.g. `python3 tester.py -f code/v08.py -t 5 -o times.csv -i 5 -e 3 -p pypy3`, type `python3 tester.py --help` for argument explanation).

#### tester_100k.py
A less versatile version of `tester.py` adapted to run `v1337.cpp` which is more optimised and less generic/robust than other versions (e.g. `g++ code/v1337.cpp -O3 -o code/v1337.cO3 -std=c++17` and `python3 tester_100k.py -f code/v1337.cO3 -i 5 -c 1`). It runs other versions too (e.g. `python3 tester_100k.py -f code/v13.py -i 5 -p pypy3`).

#### time_parser.py
It reads `times.csv` and generates a summary of results, using the best of each run type (interpreter + input size + version of code). Used as raw data generate presentation plots. For more info about plots look into that directory.

#### times.csv
Where runtime information from `batch_tester.py` is stored.

#### timings.md
Summary of `times.csv` as generated by `time_parser.py`.

#### triplets.txt
All possible combinations that fullfill the problem description up to N=2 000 000. Used for result verification.

## How to run the presentation
### If you don't care too much about the format
[Click here](https://github.com/isaacbernat/presentations/blob/master/optimise/final_github_viewer.md) (the charts are not interactive).

### If you want it to look "good"
- Clone or download this repository.
- In a terminal with the same path as this directory run `python3 -m http.server`.
- Open in a browser `http://localhost:8000`.
- Press shift+F for full screen, shift+P for presentation mode (with notes). Up and Down arrows to go through slides.
- For more info https://github.com/gnab/remark
