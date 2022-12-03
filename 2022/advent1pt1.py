def get_cal_list():
    '''Convert text file of raw data into a list'''
    file = open("2022/advent1pt1.txt", "r")
    calories = []

    for line in file:
        calories.append(line)
    file.close
    return calories


def get_elf(n: int):
    ''''Name an elf'''
    return f"elf {n}"

def get_calories(list: list):
    '''take in a list of numbers
    return a dictionary of "elf name": value'''

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
    '''Finds the largest value in given dictionary'''

    largest = 0
    for name, calories in dict.items():
        if calories > largest:
            largest = calories
    return largest


#########
# start #
#########
if __name__ == "__main__":
    calories = get_cal_list()
    elves = get_calories(calories)
    largest = find_largest_cal(elves)
    print(largest)

