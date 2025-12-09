from read_input import read_day_07
from collections import defaultdict

diagram = read_day_07(example=False)

# Part 1
total_splits = 0

beam_positions = [diagram[0].find("S")]
for row in diagram[1:]:
    split_positions = [i for i in range(len(row)) if row[i] == "^" and i in beam_positions]
    if not split_positions:
        continue
    total_splits += len(split_positions)
    new_beam_positions = set()
    for pos in beam_positions:
        if pos in split_positions:
            new_beam_positions.update([pos+d for d in (-1, 1)])
        else:
            new_beam_positions.add(pos)
    beam_positions = new_beam_positions

print(f"Answer part 1: {total_splits}")


# Part 2

beam_positions = defaultdict(int)
beam_positions[diagram[0].find("S")] = 1
for row_num, row in enumerate(diagram[1:]):
    split_positions = [i for i in range(len(row)) if row[i] == "^" and i in beam_positions]
    if not split_positions:
        continue
    current_beam_positions = [k for k, v in beam_positions.items() if v > 0]
    for pos in current_beam_positions:
        if pos in split_positions:
            beam_positions[pos-1] += beam_positions[pos]
            beam_positions[pos+1] += beam_positions[pos]
            beam_positions[pos] = 0

print(f"Answer part 2: {sum(beam_positions.values())}")