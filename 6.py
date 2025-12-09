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
split_problems = [line.split() for line in problems]
for i in range(len(split_problems[0])):
    current_problem = [split_problems[row_index][i] for row_index in range(len(split_problems))]
    operator = current_problem.pop(-1)

    total_sum += reduce(funcs[operator], [int(digit) for digit in current_problem])
   
print(f"Answer part 1: {total_sum}")



# part 2
total_sum = 0
current_problem_result = 0
for i in range(len(problems[0])):
    if i < len(problems[-1]):
        operator_line_char = problems[-1][i]

    if operator_line_char == "*" or operator_line_char == "+":
        operator = operator_line_char
        total_sum += current_problem_result 
        current_problem_result = 0

    current_number = "".join([problems[row_index][i] for row_index in range(len(problems)-1)]).strip()
    if not current_number:
        continue
    current_int = int(current_number)
    if current_problem_result == 0:
        current_problem_result += current_int
    else:
        current_problem_result = funcs[operator](current_problem_result, current_int)

# add result of last loop
total_sum += current_problem_result

print(f"Answer part 2: {total_sum}")

