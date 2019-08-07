import argparse
import random
import subprocess


with open("output", 'r') as f:
    expected_output = f.read().split("\n")


def verify(values, results):
    assert(len(values) + 1 == len(results))

    for v, r in zip(values, results):
        if r > "1000000":
            continue
        assert(expected_output[v - 1] == r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", type=int, default=1048576,
                        help="the maximum value of N. Defaults to 1048576")
    parser.add_argument("-e", "--entries", type=int, default=1,
                        help="the number of entries to test. Defaults to 1")
    parser.add_argument("-s", "--seed", type=int, default=0x15AAC,
                        help="random seed to generate inputs.")
    parser.add_argument("-f", "--file", type=str, default="v05.py",
                        help="python file to run the program.")
    parser.add_argument("-p", "--python", type=str, default="python3",
                        help="python intepreter. Defaults to python3.")

    a = parser.parse_args()
    # e.g. python3 tester.py -f v05.py -r 1024
    # e.g. python3 tester.py -f v06.py -e 2

    v = 1 if a.entries == 1 else 524288
    while v < a.range:
        v *= 2
        command = subprocess.run(
            ["time", a.python, a.file],
            input="\n".join([str(v), ""]).encode(),
            capture_output=True)

        results = command.stdout.decode().split("\n")
        time = command.stderr.decode().strip().split(" ")[0]
        verify([v], results)

        print(f"{a.file} took {time} for N = {v}.")
    if a.entries == 1:
        return

    random.seed(a.seed)
    length = 1
    for _ in range(a.entries - 1):
        length *= 10
        values = [random.randint(1, a.range) for _ in range(length)]

        command = subprocess.run(
            ["time", a.python, a.file],
            input="\n".join([str(v) for v in values]).encode(),
            capture_output=True)

        results = command.stdout.decode().split("\n")
        time = command.stderr.decode().strip().split(" ")[0]
        verify(values, results)

        print(f"{a.file} took {time} for {length} elements, N <= {a.range}")


if __name__ == '__main__':
    main()
