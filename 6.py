from read_input import read_day_06
from operator import mul, add
from functools import reduce

problems = read_day_06(example=False)
funcs = {
    "*": mul,
    "+": add
}

# part 1
total_sum = 0
for i in range(len(problems[0])):
    current_problem = [problems[row_index][i] for row_index in range(len(problems))]
    operator = current_problem.pop(-1)

    total_sum += reduce(funcs[operator], [int(digit) for digit in current_problem])
   
print(f"Answer part 1: {total_sum}")



# part 2
total_sum = 0
for i in range(len(problems[0])):
    current_problem = [problems[row_index][i] for row_index in range(len(problems))]
    operator = current_problem.pop(-1)

    total_sum += reduce(funcs[operator], [int(digit) for digit in current_problem])
   
print(f"Answer part 1: {total_sum}")

