import argparse
import random
import subprocess
import time


with open("output", 'r') as f:
    expected_output = f.read().split("\n")


def verify(values, results):
    assert(len(values) + 1 == len(results))

    for v, r in zip(values, results):
        if r > "1000000":
            continue
        try:
            assert(expected_output[v - 1] == r)
        except Exception:
            print(f"Values don't match!! v={v}, r={r}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--python", type=str, default="python3",
                        help="python intepreter. Defaults to python3.")
    parser.add_argument("-e", "--entries", type=int, default=1,
                        help="10^e entries to test. Defaults to 1")
    parser.add_argument("-r", "--range", type=int, default=1048576,
                        help="the maximum value of N. Defaults to 1048576")
    parser.add_argument("-f", "--file", type=str, default="v05.py",
                        help="python file to run the program.")
    parser.add_argument("-o", "--csv", type=str, default="",
                        help="output filename using csv format")
    parser.add_argument("-c", "--c", type=int, default=0,
                        help="C implementation, instead of python.")
    parser.add_argument("-i", "--maxiters", type=int, default=0,
                        help="max iters for a chosen set of params")
    parser.add_argument("-s", "--seed", type=int, default=0x15AAC,
                        help="random seed to generate inputs.")
    parser.add_argument("-t", "--timeout", type=int, default=0,
                        help="re-run each iteration if < elapsed seconds")

    # e.g. python3 tester.py -f v05.py -t 5 -o times.csv -i 5
    # e.g. python3 tester.py -f v08.py -t 5 -o times.csv -i 5 -e 3
    # e.g. python3 tester.py -f v05.py -r 1024
    # e.g. python3 tester.py -f v08.py -e 5 -p pypy3
    # g++ v01.c -o v01.cO0 -std=c++17
    # g++ v01.c -O3 -o v01.cO3 -std=c++17
    # e.g. python3 tester.py -f v01.cO0 -c 1 -r 2048

    a = parser.parse_args()
    fname, f_sufix = a.file.split(".")
    runner = f_sufix if a.c else a.python
    today = time.strftime("%Y-%m-%d")

    v = 1
    total_seconds = 0
    total_iters = 0
    while v < a.range:
        v *= 2
        if a.c:
            command = subprocess.run(
                ["time", f"./{a.file}"],
                input=f"{v}\n0".encode(),
                capture_output=True)
        else:
            command = subprocess.run(
                ["time", a.python, a.file],
                input=f"{v}\n".encode(),
                capture_output=True)

        results = command.stdout.decode().split("\n")
        elapsed = float(command.stderr.decode().strip().split(" ")[0])
        verify([v], results)

        if a.csv:
            # "file_name,runtime,maxN,entries,runner,date,machine"
            line = f"{fname},{elapsed},{v},1,{runner},{today},mbp2012\n"
            with open(a.csv, "a") as f:
                f.write(line)

        print(f"{a.file} took {elapsed} for N = {v}.")

        total_iters += 1
        if a.maxiters and total_iters >= a.maxiters:
            total_iters = 0
            total_seconds = 0
            continue

        total_seconds += elapsed
        if a.timeout:
            if total_seconds <= a.timeout:
                # repeat the same test again, cancel the *= 2 of each iteration
                v = int(v / 2)
            elif total_seconds > a.timeout or total_iters < a.maxiters:
                # this is getting too long... let's already finish
                return
            else:
                total_iters = 0
                total_seconds = 0

    if a.entries == 1:
        return

    random.seed(a.seed)
    total_seconds = 0
    total_iters = 0
    length = 1
    while length < 10 ** a.entries:
        length *= 10
        values = [random.randint(1, a.range) for _ in range(length)]

        if a.c:
            command = subprocess.run(
                ["time", f"./{a.file}"],
                input="\n".join([str(v) for v in values] + ["0"]).encode(),
                capture_output=True)
        else:
            command = subprocess.run(
                ["time", a.python, a.file],
                input="\n".join([str(v) for v in values]).encode(),
                capture_output=True)

        results = command.stdout.decode().split("\n")
        elapsed = float(command.stderr.decode().strip().split(" ")[0])
        verify(values, results)

        if a.csv:
            # "file_name,runtime,maxN,entries,runner,date,machine"
            line = f"{fname},{elapsed},{v},{length},{runner},{today},mbp2012\n"
            with open(a.csv, "a") as f:
                f.write(line)

        print(f"{a.file} took {elapsed} for {length} elements, N <= {a.range}")

        total_iters += 1
        if a.maxiters and total_iters >= a.maxiters:
            total_iters = 0
            total_seconds = 0
            continue

        total_seconds += elapsed
        if a.timeout:
            if total_seconds <= a.timeout:
                # repeat the same test again, cancel the *= 2 of each iteration
                length = int(length / 10)
            elif total_seconds > a.timeout or total_iters < a.maxiters:
                # this is getting too long... let's already finish
                return
            else:
                total_iters = 0
                total_seconds = 0


if __name__ == '__main__':
    main()
