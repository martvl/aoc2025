from read_input import read_day_05

ranges, ingredients = read_day_05(example = False)

def ingredient_in_range(ingredient, min, max):

    return min <= ingredient <= max

def find_fresh_ingredients(ranges, ingredients):
    n_fresh_ingredients = 0

    for i in ingredients:
        for min, max in ranges:
            if ingredient_in_range(i, min, max):
                n_fresh_ingredients += 1
                break

    return n_fresh_ingredients

n_fresh_ingredients = find_fresh_ingredients(ranges, ingredients)
print(f"Answer part 1: {n_fresh_ingredients}")




def ranges_overlap(range_1, range_2):
    min_1, max_1 = range_1
    min_2, max_2 = range_2

    if min_2 >= max_2:
        pass
    

def find_all_fresh_ingredients(ranges):
    final_ranges = []
    ranges.sort(key=lambda x: x[0])
    
    for check_min, check_max in ranges:
        for i, (f_min, f_max) in enumerate(final_ranges):
            if check_min <= f_max + 1:
                if check_max > f_max:
                    final_ranges[i] = (final_ranges[i][0], check_max)
                    break
                elif check_max <= f_max:
                    break
        else:      
            final_ranges.append((check_min, check_max))
    return sum([max-min+1 for min, max in final_ranges])
                
            




n_fresh_ingredients = find_all_fresh_ingredients(ranges)
print(f"Answer part 2: {n_fresh_ingredients}")