def read_day_01(example = False):

    file = f"input/input_01{'_example' if example else ''}.txt"

    directions, nums = [], []

    with open(file) as infile:
        for line in infile.readlines():
            directions.append(line[0])
            nums.append(int(line[1:]))
    return directions, nums

def read_day_02(example = False):
    file = f"input/input_02{'_example' if example else ''}.txt"

    ranges = []
    with open(file) as infile:
        for line in infile.readlines():
            for range in line.split(","):
                ranges.append(tuple(int(i) for i in range.split("-")))

    return ranges

def read_day_03(example = False):
    file = f"input/input_03{'_example' if example else ''}.txt"

    with open(file) as infile:
        banks = [line.strip() for line in infile.readlines()]

    return banks


def read_day_04(example = False):
    file = f"input/input_04{'_example' if example else ''}.txt"

    with open(file) as infile:
        rows = [line.strip() for line in infile.readlines()]

    return rows