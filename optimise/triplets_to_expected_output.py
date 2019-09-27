# 2M triplets from https://www.mathblog.dk/tools/pythagorean-triplets-generator

with open("triplets.txt", 'r') as triplets:
    with open("output.txt", "w") as output:
        result = 0
        current = 1
        target_index = 0
        targets = [int(line.split(",")[-1]) for line in triplets]
        while target_index < len(targets):
            target = targets[target_index]
            for i in range(current, target):
                output.write(f"{result}\n")
            current = target
            try:
                while target == targets[target_index]:
                    target_index += 1
                    result += 1
            except IndexError:
                break
