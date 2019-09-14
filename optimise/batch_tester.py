import glob
import subprocess

for py in sorted(glob.glob("v*.py")):
    # ignore variants and refactorings
    if len(py) != 6:
        continue

    params = f"python3 tester.py -f {py} -t 600 -o times.csv -i 5 -e 5".split()
    res = subprocess.run(params)
    res = subprocess.run(params + ["-p", "pypy3"])

c_implementations = [] # TODO
