def read_day_01(example = False):

    file = f"input/input_01{'_example' if example else ''}.txt"

    directions, nums = [], []

    with open(file) as infile:
        for line in infile.readlines():
            directions.append(line[0])
            nums.append(int(line[1:]))
    return directions, nums