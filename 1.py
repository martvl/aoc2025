from read_input import read_day_01

from operator import sub, add

directions, nums = read_day_01(example = False)

# Part 1
operators = {
        "R": add,
        "L": sub
    }
pos = 50
password = 0

for d, n in zip(directions, nums):
    pos = operators[d](pos, n)
    if pos % 100 == 0:
        password += 1

print(f"Part 1 Password: {password}")


pos = 50
password = 0 
for d, n in zip(directions, nums):
    new_pos = operators[d](pos, n)
    
    mod, rem = divmod(new_pos, 100)
    password += abs(mod)

    if d == "L" and rem == 0:
        password += 1   
    elif d == "L" and pos == 0:
        password -= 1
    pos = rem
    

print(f"Part 2 Password: {password}")