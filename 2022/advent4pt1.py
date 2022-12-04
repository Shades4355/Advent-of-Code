from advent2pt1 import open_file


def elven_pairs(all_elves: list) -> list:
    '''Break elves into pairs\n
    Returns a list of paired elves'''

    paired_elves = []
    
    for line in all_elves:
        index = line.index(",")
        paired_elves.append([line[0:index], line[index + 1:len(line)].strip()])
    return paired_elves
                

# compare cleaning spaces
def compare(elf_one: list, elf_two: list) -> bool:
    '''Compare to ranges\n
    Return True if either range is fully in the other'''
    index_one = elf_one.index("-")
    range_one = [elf_one[0:index_one], elf_one[index_one + 1:len(elf_one)]]
    index_two = elf_two.index("-")
    range_two = [elf_two[0:index_two], elf_two[index_two + 1:len(elf_one)]]
    
    if range_two[0] <= range_one[0] and range_one[1] <= range_two[1]:
        return True
    elif range_one[0] <= range_two[0] and range_two[1] <= range_one[1]:
        return True
    return False



# In how many assignment pairs does one range fully contain the other?

def start():
    all_elves = open_file("advent4pt1.txt")
    paired_elves = elven_pairs(all_elves)
    total = 0 

    for elf_one, elf_two in paired_elves:
        if compare(elf_one, elf_two):
            total += 1

    print("Total:", total)


#########
# start #
#########

if __name__ == "__main__":
    start()

    # 529 = Too high
