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

        bag = i.split(' contain ')[0]
        in_bags = i.split(' contain ')[1].split(', ')

        for i in in_bags:
            stripped_bags = re.sub('[0-9] ', '', i).strip('.')
            stripped_bag_list.append(stripped_bags)

        bag_object[bag] = stripped_bag_list

    print(bag_object)

    return total


def getBagContents(bags):
    contents = []
    # return list of bags

    return contents


if __name__ == "__main__":
    print(bagPuzzle1(data))
