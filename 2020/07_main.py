import re

with open("2020/07_data.txt") as file:
    data = file.read().strip()


def bagPuzzle1(file: str):
    total = 0
    bag_object = {}

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
        bag_object[bag] = stripped_bag_list

    # for key in bag_object:
    #     for i in bag_object[key]:
    #         if i == "shiny gold bag":
    #             total += 1

    for i in bag_object:
        total += getBagContents(i, bag_object)

    return total


def getBagContents(bag: str, all_bags: object):
    for i in all_bags[bag]:
        if i == "shiny gold bag":
            return 1
        elif i == "no other bag":
            return 0
        else:
            return getBagContents(i, all_bags)


if __name__ == "__main__":
    print(bagPuzzle1(data))
