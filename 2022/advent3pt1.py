from advent2pt1 import open_file


def organized_piles(backpacks: list) -> list:
    '''Converts list of backpacks into a list of compartments\n
    Returns a list of lists.
    \tEach super-list is a backpack
    \tEach sub-list is a compartment'''

    organized_piles = []
    for backpack in backpacks:
        organized_piles.append(compartments(backpack.strip()))
    return organized_piles


def compartments(backpack: str) -> list:
    '''Evenly splits items between compartment 1 and 2\n
    Compartment 1 holds the first half of the items
    Compartment 2 holds the second half of the items'''

    compartment_one = []
    compartment_two = []
    total_items = len(backpack)
    item_counter = 0
    for item in backpack:
        if item_counter < total_items / 2:
            compartment_one.append(item)
        else:
            compartment_two.append(item)
        item_counter += 1
    
    return [compartment_one, compartment_two]


def find_duplicates(compartment_one: list, compartment_two: list) -> str:
    '''Returns 1 item that is in both compartments'''

    for item in compartment_one:
        if item in compartment_two:
            return item


def priority(item: str) -> int:
    '''Returns an Integer value for the alphabetical character entered\n
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52'''

    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - 96
    elif ord("A") <= ord(item) <= ord("Z"):
        return ord(item)  - 38


def add_priorities(organized_bags: list) -> int:
    '''Takes in a list of organized bags\n
    Returns a total value of duplicate items'''

    total = 0
    for comp_one, comp_two in organized_bags:
        item = find_duplicates(comp_one, comp_two)
        total += priority(item)

    return total


def start():
    '''Program run command'''
    
    backpacks = open_file("advent3pt1.txt")
    pile_of_bags = organized_piles(backpacks)
    total = add_priorities(pile_of_bags)

    print("Total:", total)


#########
# start #
#########
if __name__ == "__main__":
    start()
