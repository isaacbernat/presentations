# From > 1 Billion years to < 1 second

## Content
### Intro
Adding resources to speed up processes isn't always feasible. This talk presents a simple problem and how to achieve >10^15x speedups on a regular laptop. Be warned, as overall time is reduced, minuscule overheads become gigantic. Nevertheless, most techniques can still be effective in more general contexts.

### Abstract
The goal of this talk is to empower people with over a dozen optimisation techniques which may be effectively used in a wide variety of situations, even beyond Python.

I will present best practices, typical pitfalls and common tools, but the main focus will be on a practical approach. I will showcase a small problem and a naive solution, just a few lines of Python, so that it's easily understood. Iteratively I will apply each optimisation, explain the reasoning behind it and note how execution time is reduced. By the end of the talk, one will see how the code evolved from something that would take > 1 billion years to compute to < 1 second on a regular laptop.

I will also compare running times between Python, PyPy and C++ implementations (one being just a few milliseconds), and show how the same techniques may achieve vastly different speedups from the python versions.

### Time estimates
Attendants are encouraged to participate [in a survey and for each presented optimisation fill their estimated speedup](https://tinyurl.com/pycon2019). That's a good exercise to evaluate how good one is at estimating code performance (compared to reality and also to other fellows, so please don't cheat!).

## How to run the presentation
### If you don't care too much about the format
[Click here](https://github.com/isaacbernat/presentations/blob/master/optimise/final.md) (just open the markdown file)

### If you want it to look "good"
- In a terminal with the same path as this directory type `python3 -m http.server`.
- Then open in a browser `http://localhost:8000`.
- Use shift+F for full screen, shift+P for presentation mode. Up and Down to go through slides.
- For more info https://github.com/gnab/remark
