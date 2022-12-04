from advent2pt1 import open_file
from advent4pt1 import elven_pairs

def count(paired_elves: list) -> int:
    '''Count the number of times compare() returns True'''

    total = 0

    for elf_one, elf_two in paired_elves:
        total += compare(elf_one, elf_two)
    return total

def compare(elf_one: list, elf_two: list) -> bool:
    '''Compare two ranges\n
    Return True if either range is partially in the other'''

    # break lists of strings into lists of integer
    index_one = elf_one.index("-")
    range_one = [int(elf_one[0:index_one]), int(elf_one[index_one + 1:len(elf_one)])]
    index_two = elf_two.index("-")
    range_two = [int(elf_two[0:index_two]), int(elf_two[index_two + 1:len(elf_two)])]

    # compare range one and range two, looking for overlaps
    if range_two[0] <= range_one[0] <= range_two[1]:
        return True
    elif range_two[0] <= range_one[1] <= range_two[1]:
        return True
    elif range_one[0] <= range_two[0] <= range_one[1]:
        return True
    elif range_one[0] <= range_two[1] <= range_one[1]:
        return True

    return False

def start():
    all_elves = open_file("advent4pt1.txt")
    paired_elves = elven_pairs(all_elves)
    total = count(paired_elves)
    
    print("Total:", total)


#########
# start #
#########

if __name__ == "__main__":
    start()
