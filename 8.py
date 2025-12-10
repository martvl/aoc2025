from read_input import read_day_08
from math import sqrt
from itertools import combinations
from operator import mul
from functools import reduce

vectors = read_day_08(example=False)

def distance_between(a, b):
    return sqrt(sum([abs(x-y)**2 for x,y in zip(a,b)]))

all_pairs = [(v0, v1) for v0, v1 in combinations(vectors, r=2)]
all_pairs = [pair for pair in sorted(all_pairs, key=lambda x: distance_between(x[0], x[1]))]

# Part 1
circuits = []
for i in range(10):
    conn = all_pairs[i]
    box_present_in_circuit = [index for index, c in enumerate(circuits) if conn[0] in c or conn[1] in c]
    if len(box_present_in_circuit) == 2:
        circuits[box_present_in_circuit[0]].update(circuits[box_present_in_circuit[1]])
        circuits.pop(box_present_in_circuit[1])
    elif len(box_present_in_circuit) == 1:
        circuits[box_present_in_circuit[0]].update(conn)
    else:
        circuits.append(set(conn))
    
answer = reduce(mul, sorted([len(c) for c in circuits], reverse=True)[:3])
print(f"Answer part 1: {answer}")

# Part 2
circuits = []
for i in range(len(all_pairs)):
    conn = all_pairs[i]
    box_present_in_circuit = [index for index, c in enumerate(circuits) if conn[0] in c or conn[1] in c]
    if len(box_present_in_circuit) == 2:
        circuits[box_present_in_circuit[0]].update(circuits[box_present_in_circuit[1]])
        circuits.pop(box_present_in_circuit[1])
    elif len(box_present_in_circuit) == 1:
        circuits[box_present_in_circuit[0]].update(conn)
    else:
        circuits.append(set(conn))
    
    if len(circuits) == 1 and len(circuits[0]) == len(vectors):
        break

answer = conn[0][0] * conn[1][0]
print(f"Answer part 2: {answer}")
