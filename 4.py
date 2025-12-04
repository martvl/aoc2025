from read_input import read_day_04

rows = read_day_04(example=False)

def find_accessible_rolls(rows, indices_to_check):
    
    n_accessible_rolls = 0
    indices_accessible_rolls = []
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] == ".":
                continue
            occupied_positions = 0
            for dx, dy in indices_to_check:
                check_y, check_x = (y+dy, x+dx)
                if check_y < 0 or check_x < 0:
                    continue
                if check_y >= len(rows) or check_x >= len(rows[y]):
                    continue
                item = rows[check_y][check_x]
                if item == "@":
                    occupied_positions += 1
            if occupied_positions < 4:
                indices_accessible_rolls.append((y,x))
                n_accessible_rolls += 1
    
    return n_accessible_rolls, indices_accessible_rolls

# Part 1

indices_to_check = [
    (-1,-1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1,-1),
    (0,-1)
]

n_rolls, _ = find_accessible_rolls(rows, indices_to_check)
print(f"Answer part 1: {n_rolls}")

# Part 2
def remove_accessible_rolls(rows, indices_to_remove):
    for y, x in indices_to_remove:
        rows[y] = f"{rows[y][:x]}{'.'}{rows[y][x+1:]}"
    return rows

total_removed_rolls = 0
updated_rows = rows
while True:
    n_rolls_to_remove, indices_accessible_rolls = find_accessible_rolls(updated_rows, indices_to_check)
    if n_rolls_to_remove == 0:
        break
    updated_rows = remove_accessible_rolls(updated_rows, indices_accessible_rolls)
    total_removed_rolls += n_rolls_to_remove
    
print(f"Answer part 2: {total_removed_rolls}")
