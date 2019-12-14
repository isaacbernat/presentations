import glob
import subprocess
import os

for py in sorted(glob.glob("code/v*.py")):
    # ignore variants and refactorings
    if len(py) != 5 + 6:
        continue

    params = f"python3 tester.py -f {py} -t 600 -o times.csv -i 5 -e 5".split()
    subprocess.run(params)
    subprocess.run(params + ["-p", "pypy3"])

for file in sorted(glob.glob("code/v*.cpp")):
    # ignore variants and 1337.cpp which should run under tester_100k.py
    if len(file) != 5 + 7:
        continue

    exe = [f"{file}O0", f"{file}O3"]
    subprocess.run(["g++", file, "-o", exe[0], "-std=c++17"])
    subprocess.run(["g++", file, "-o", exe[1], "-std=c++17", "-O3"])

    for e in exe:
        subprocess.run("python3 tester.py"
                       f" -f {e} -t 600 -o times.csv -i 5 -e 5 -c 1".split())
        os.remove(e)
