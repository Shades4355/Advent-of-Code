from advent2pt1 import open_file


def elven_pairs(all_elves: list) -> list:
    '''Break elves into pairs\n
    Returns a list of paired elves'''

    paired_elves = []
    
    for line in all_elves:
        index = line.index(",")
        paired_elves.append([line[0:index], line[index + 1:len(line)].strip()])
    return paired_elves
                

def compare(elf_one: str, elf_two: str) -> bool:
    '''Compare two ranges\n
    Return True if either range is fully in the other'''

    index_one = elf_one.index("-")
    range_one = [elf_one[0:index_one], elf_one[index_one + 1:len(elf_one)]]
    index_two = elf_two.index("-")
    range_two = [elf_two[0:index_two], elf_two[index_two + 1:len(elf_two)]]
    
    if int(range_two[0]) <= int(range_one[0]) and int(range_one[1]) <= int(range_two[1]):
        return True
    elif int(range_one[0]) <= int(range_two[0]) and int(range_two[1]) <= int(range_one[1]):
        return True
    return False


def count(paired_elves: list) -> int:
    total = 0

    for elf_one, elf_two in paired_elves:
        if compare(elf_one, elf_two):
            total += 1
    return total

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
