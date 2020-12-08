import re

with open("2020/07_data.txt") as file:
    data = file.read().strip()

# part 1 #


def bagPuzzle1(file: str):
    total = 0
    bag_dict = {}

    # need to recognize bag colors
    bags_in_bags = file.split('.\n')

    for i in bags_in_bags:
        stripped_bag_list = []

        # define 'bag' and remove trainiling 's'
        bag = i.split(' contain ')[0]
        if bag.endswith('s'):
            bag = bag[:len(bag)-1]

        # define stripped_bag_list and remove trailing 's'
        in_bags = i.split(' contain ')[1].split(', ')
        for i in in_bags:
            stripped_bags = re.sub('[0-9] ', '', i).strip('.')
            if stripped_bags.endswith('s'):
                stripped_bags = stripped_bags[:len(stripped_bags)-1]
            stripped_bag_list.append(stripped_bags)

        # make an object with key 'bag' and value 'stripped_bag_list'
        bag_dict[bag] = stripped_bag_list

    # Determine if there is at least 1 gold bag in the current key
    for key in bag_dict:
        if getBagContents(key, bag_dict) > 0:
            total += 1

    return total


def getBagContents(bag: str, all_bags: dict):
    """recursively check bags for 'shiny gold bag' or the end of the chain ('no other bag')"""
    total = 0
    for i in all_bags[bag]:
        if i == "shiny gold bag":
            total += 1
        elif i == "no other bag":
            total += 0
        else:
            total += getBagContents(i, all_bags)

    return total


# part 2 #
def bagPuzzle2(file: str):
    bag_dict = {}
    # need to recognize bag colors
    bags_in_bags = file.split('.\n')

    for i in bags_in_bags:
        stripped_bag_list = []

        # define 'bag' and remove trainiling 's'
        bag = i.split(' contain ')[0]
        if bag.endswith('s'):
            bag = bag[:len(bag)-1]

        # define stripped_bag_list and remove trailing 's'
        in_bags = i.split(' contain ')[1].split(', ')
        for i in in_bags:
            stripped_bags = i.strip('.')
            if stripped_bags.endswith('s'):
                stripped_bags = stripped_bags[:len(stripped_bags) - 1]
            number_of_bags = stripped_bags.split()[0]
            bag_color = " ".join(stripped_bags.split()[1:])
            stripped_bag_list.append([number_of_bags, bag_color])

        # make an Dictionary with key 'bag' and value 'stripped_bag_list'
        bag_dict[bag] = stripped_bag_list

    total = bagCalculater("shiny gold bag", bag_dict)

    return total


def bagCalculater(bag: str, all_bags: dict):
    total = 0

    for key in all_bags[bag]:
        if key[1] != "other bag":
            total += int(key[0])
            for i in range(int(key[0])):
                total += bagCalculater(key[1], all_bags)
        else:
            total += 0

    return total


if __name__ == "__main__":
    print("Part 1", bagPuzzle1(data))  # 222
    print("Part 2", bagPuzzle2(data))  # 13264
