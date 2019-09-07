import glob
import subprocess

for py in sorted(glob.glob("v*.py")):
    params = f"python3 tester.py -f {py} -t 300 -o times.csv -i 5 -e 5".split()
    res = subprocess.run(params)
    res = subprocess.run(params + ["-p", "pypy3"])

c_implementations = [] # TODO
