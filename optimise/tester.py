import argparse
import random
import subprocess


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--range", type=int, default=100,
                        help="the maximum value of N. Defaults to 100")
    parser.add_argument("-e", "--entries", type=int, default=10,
                        help="the number of entries to test. Defaults to 10")
    parser.add_argument("-s", "--seed", type=int, default=0x15AAC,
                        help="random seed to generate inputs.")
    parser.add_argument("-f", "--file", type=str, default="v01.py",
                        help="python file to run the program.")

    a = parser.parse_args()
    random.seed(a.seed)
    values = [random.randint(1, a.range) for _ in range(a.entries)]

    command = subprocess.run(
        ["time", "python3", a.file],
        input="\n".join([str(v) for v in values] + [""]).encode(),
        capture_output=True)

    results = command.stdout.decode().split("\n")
    time = command.stderr.decode().strip().split(" ")[0]
    assert(len(values) + 1 == len(results))

    with open("output", 'r') as f:
        expected_output = f.read().split("\n")

    for v, r in zip(values, results):
        assert(expected_output[v - 1] == r)

    print(f"{a.file} took {time} for {a.entries} entries with N <= {a.range}"
        f" and seed {a.seed}.")


if __name__ == '__main__':
    main()
