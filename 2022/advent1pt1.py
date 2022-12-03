from pickle import APPEND
from sys import stdout


file = open("2022/advent1pt1.txt", "r")
calories = []

for line in file:
    calories.append(line)
file.close


def get_elf(n: int):
    return f"elf {n}"

def get_calories(list: list):
    n = 1
    elf_dict = {}

    elf_name = get_elf(n)
    elf_dict[elf_name] = 0

    for calories in list:
        if calories != "\n":
            elf_dict[elf_name] += int(calories)
        else:
            n += 1
            elf_name = get_elf(n)
            elf_dict[elf_name] = 0
    return elf_dict

def find_largest_cal(dict: dict):
    largest = 0
    for name, calories in dict.items():
        if calories > largest:
            largest = calories
    return largest


#########
# start #
#########

elves = get_calories(calories)
largest = find_largest_cal(elves)
print(largest)
