# From > 1 Billion years to < 1 second

Presentation on the topic of code optimisation given at PyCon Sweden. Learn 10+ techniques applicable in a wide variety of situations and see how Python performance compares to C++.
[![YouTube link to the talk](https://github.com/isaacbernat/presentations/blob/master/optimise/video_preview.png)](https://youtu.be/asZ0SDTKqvM)

Additional content, references and notes supporting the slides are found in `final.md`. More info in the section *How to run the presentation* below.

## Content
### Abstract (50-word version)
Adding resources to speed up processes isn't always feasible. This talk presents a simple problem and how to achieve >10^18x speedups on a regular laptop. Be warned, as overall time is reduced, minuscule overheads become gigantic. Nevertheless, most techniques can still be effective in more general contexts.

### Abstract (150-word version)
The goal of this talk is to empower people with over a dozen optimisation techniques which may be effectively used in a wide variety of situations, even beyond Python.

I will present best practices, typical pitfalls and common tools, but the main focus will be on a practical approach. I will showcase a small problem and a naive solution, just a few lines of Python, so that it's easily understood. Iteratively I will apply each optimisation, explain the reasoning behind it and note how execution time is reduced. By the end of the talk, one will see how the code evolved from something that would take > 1 billion years to compute to < 1 second on a regular laptop.

I will also compare running times between Python, PyPy and C++ implementations (one being just a few milliseconds), and show how the same techniques may achieve vastly different speedups from the Python versions.

## How to run the presentation
### If you don't care too much about the format
[Click here](https://github.com/isaacbernat/presentations/blob/master/optimise/final_github_viewer.md) (the charts are not interactive).

### If you want it to look "good"
- Clone or download this repository.
- In a terminal with the same path as this directory run `python3 -m http.server`.
- Open in a browser `http://localhost:8000`.
- Press shift+F for full screen, shift+P for presentation mode (with notes). Up and Down arrows to go through slides.
- For more info https://github.com/gnab/remark
