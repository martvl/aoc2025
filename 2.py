from read_input import read_day_02

ranges = read_day_02(example=False)

def check_num_part_1(num):

    s_num = str(num)
    if len(s_num) % 2 != 0:
        return 0
    mod, rem = divmod(num, 10**(len(s_num) // 2))
    if mod == rem:
        return num
    else:
        return 0
    
# Part 1
invalid_nums = 0
for start, stop in ranges:
    for num in range(start, stop + 1):
        invalid_nums += check_num_part_1(num)

print(f"Answer part 1: {invalid_nums}")

def check_num_part_2(num):

    s_num = str(num)
    for len_to_check in range(len(s_num)//2):
        len_to_check = len_to_check + 1
        if len(s_num) % (len_to_check) == 0:
            split_s_num = [s_num[i:i+len_to_check] for i in range(0, len(s_num), len_to_check)]
            if len(set(split_s_num)) == 1:
                return int(s_num)
    return 0

        
invalid_nums = 0
for start, stop in ranges:
    for num in range(start, stop + 1):
        invalid_nums += check_num_part_2(num)

print(f"Answer part 2: {invalid_nums}")
