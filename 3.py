from read_input import read_day_03

banks = read_day_03(example=False)

def detect_largest_num(seq: str, n: int = 2) -> int:
    """Detect the largest number of length n, scanning left to right        

    Args:
        seq (str): Sequence of numbers
        n (int, optional): Length of the largest number to detect. Defaults to 2.

    Returns:
        int: Largest number detected
    """
    
    largest_num_detected = [0 for _ in range(n)]
    index_detected = -1
    
    for i in range(n):
        for j in range(index_detected+1, len(seq)-n+i+1):
            num = int(seq[j])
            if int(num) > largest_num_detected[i]:
                largest_num_detected[i] = int(num)
                index_detected = j
    return int("".join(str(i) for i in largest_num_detected))

# Part 1

output = 0
for bank in banks:
    output += detect_largest_num(bank, n=2)

print(f"Answer part 1: {output}")



# Part 2

output = 0
for bank in banks:
    output += detect_largest_num(bank, n=12)

print(f"Answer part 2: {output}")