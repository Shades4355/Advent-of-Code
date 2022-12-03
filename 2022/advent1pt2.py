from advent1pt1 import get_cal_list, get_calories

def top_3(dict: dict):
    '''Find the 3 largest values in a dictionary'''
    first = 0
    second = 0
    third = 0
    
    for key, value in dict.items():
        if value > first:
            third = second
            second = first
            first = value
        elif value > second:
            third = second
            second = value
        elif value > third:
            third = value
    return [first, second, third]

def add_x(list: list, x: int):
    '''add X number of integers from a list together
    returns the total value as an Int'''
    n = 0
    total = 0
    while n < x:
        total += list[n]
        n += 1
    return total


#########
# start #
#########
calories = get_cal_list()
elves = get_calories(calories)
top_three = top_3(elves)

print (add_x(top_three, 3))
