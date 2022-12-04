from advent2pt1 import open_file


def elven_pairs(all_elves: list) -> list:
    '''Break elves into pairs\n
    Returns a list of paired elves'''

    paired_elves = []
    
    for line in all_elves:
        index = line.index(",")
        paired_elves.append([line[0:index], line[index+1:len(line)].strip()])
    return paired_elves
                

# compare cleaning spaces
def 

# In how many assignment pairs does one range fully contain the other?

def start():
    all_elves = open_file("advent4pt1.txt")
    paired_elves = elven_pairs(all_elves)

    for elf_one, elf_two in paired_elves:


#########
# start #
#########

if __name__ == "__main__":
    start()
