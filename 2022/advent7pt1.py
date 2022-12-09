from copy import deepcopy
from advent2pt1 import open_file


def read_line(line: str, tree: object, position: list) -> list:
    '''Read line'''

    new_tree = deepcopy(tree)
    current_position = position

    if line.startswith("$ cd"):
        current_position = cd_direction(line, current_position)
    # elif line.startswith("$ ls"):
        # return None
    
    new_tree = build_tree(new_tree, current_position)

    return [new_tree, current_position]


def build_tree(tree: object, position: list) -> object:
    new_tree = deepcopy(tree)

    # check position against tree
    # if position is not in tree, add it

    return new_tree


def cd_direction(line: str, position: list) -> list:
    current_position = position
    direction = line.split(" ")[2]

    if direction == "/":
        current_position = [direction]
    elif direction == "..":
        current_position = current_position[0:len(current_position)]
    else:
        current_position.append(direction)

    return current_position


def start():
    position = []
    tree = {}
    list_commands = open_file("advent7.txt")

    for line in list_commands:
        tree, position = read_line(line.strip(), tree, position)

    print("final Tree:", tree)

#########
# start #
#########

if __name__ == "__main__":
    start()

    
