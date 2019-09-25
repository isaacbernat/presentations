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
    parser.add_argument("-f", "--file", type=str, default="v05.py",
                        help="python file to run the program.")
    parser.add_argument("-c", "--c", type=int, default=0,
                        help="C implementation, instead of python.")
    parser.add_argument("-i", "--maxiters", type=int, default=1,
                        help="max iters for a chosen set of params")
    parser.add_argument("-s", "--seed", type=int, default=0x15AAC,
                        help="random seed to generate inputs.")

    # python3 tester_100k.py -f v13.py -i 5 -p pypy3
    # python3 tester_100k.py -f fvp_cpp17.cO3 -i 5 -c 1
    a = parser.parse_args()
    fname, f_sufix = a.file.split(".")
    runner = f_sufix if a.c else a.python
    today = time.strftime("%Y-%m-%d")

    random.seed(a.seed)
    total_seconds = 0
    total_iters = 0
    length = 100000
    MAX_N = 1048576

    while a.maxiters and total_iters < a.maxiters:
        values = [random.randint(1, MAX_N) for _ in range(length)]

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

        # print(command.stdout.decode().split("Total duration")[-1])
        verify(values, results)
        total_iters += 1
        total_seconds += elapsed
        print(f"{a.file} took {elapsed} for {length} elements, N <= {MAX_N}")


if __name__ == '__main__':
    main()
