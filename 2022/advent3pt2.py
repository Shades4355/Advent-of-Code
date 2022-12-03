from advent2pt1 import open_file
from advent3pt1 import priority

# Every set of three lines in your list corresponds to a single group
def groups_of_three(elves: list) -> list:
    grouped_elves = []
    n = 0

    while n < len(elves) - 2:
        grouped_elves.append([elves[n], elves[n+1], elves[n+2]])
        n += 3
    return grouped_elves


def find_badge_items(group_of_elves: list) -> str:
    '''Finds the common item among 3 groups\n
    Returns item'''

    badge_list = []
    
    for three_group in group_of_elves:
        for item in three_group[0]:
            if item in three_group[1] and item in three_group[2]:
                badge_list.append(item)
                break

    return badge_list


# find priority of all items
def add_priorities(badge_list: list) -> int:
    total = 0
    for badge in badge_list:
        total += priority(badge)
    return total


def start() -> None:
    elves = open_file("advent3pt1.txt")
    group_of_elves = groups_of_three(elves)
    badge_list = find_badge_items(group_of_elves)
    total = add_priorities(badge_list)
    print(total)

#########
# start #
#########
if __name__ == "__main__":
    start()
