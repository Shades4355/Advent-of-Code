import time, numpy as np
from advent8pt1 import get_input


def all_end_in_z(placements:list):
    '''Checks if a list of values all end in "Z"'''
    for num in placements:
        if not num[-1] == "Z":
            return False

    return True


def follow_directions(file:dict):
    '''Takes in a dictionary containing starting values and L/R directions; outputs the number of steps needed to reach a situation where all current values end in "Z"'''
    placement = []
    new_placement = []

    for num in file["start"]:
        placement.append(num)
        new_placement.append(num)

    # find the length of each cycle
    answers = []
    for i in range(0, len(placement)):
        looping = True
        steps = 0
        while looping:
            for direction in file["directions"]:
                if direction == "L":
                    new_placement[i] = file[placement[i]][0]
                    placement[i] = new_placement[i]
                elif direction == "R":
                    new_placement[i] = file[placement[i]][1]
                    placement[i] = new_placement[i]
                else:
                    raise Exception("Unexpected direction:", direction)

                steps += 1

                if placement[i][-1] == "Z":
                    answers.append(steps)
                    looping = False
    
    # find the lowest common multiple of the cycles
    return np.lcm.reduce(answers)


def parse_input(file:list):
    '''Takes in a list; outputs a dictionary with a "directions" key, a "start" key, and a key for each value'''
    dictionary = {}
    directions = []
    
    for cha in file[0].strip():
        directions.append(cha)

    dictionary["directions"] = directions
    dictionary["start"] = []

    for i in range(2, len(file)):
        key, value = file[i].split(" = ")
        dictionary[key] = value.strip().strip("(").strip(")").split(", ")
        if key[2] == "A":
            dictionary["start"].append(key)

    return dictionary


def start(location:str):
    '''Starts the program. Takes in the location of a file; outputs the prompt answer'''
    file = get_input(location)
    parsed_file = parse_input(file)

    return follow_directions(parsed_file)


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))