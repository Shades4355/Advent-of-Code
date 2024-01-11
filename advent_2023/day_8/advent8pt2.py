import time
from advent8pt1 import get_input


def all_end_in_z(placements:list):
    '''Checks if a list of values all end in "Z"'''
    for num in placements:
        if not num[-1] == "Z":
            return False

    return True


def follow_directions(file:dict):
    '''Takes in a dictionary containing starting values and L/R directions; outputs the number of steps needed to reach a situation where all current values end in "Z"'''
    steps = 0
    placement = []
    new_placement = []

    log_file = f"logs/day8log_{time.time()}.txt" # TODO: delete

    for num in file["start"]:
        placement.append(num)
        new_placement.append(num)

    while True:
        for direction in file["directions"]:
            
            # TODO: delete log creation
            log = open(log_file, "a")
            
            for i in range(0, len(placement)):
                if direction == "L":
                    new_placement[i] = file[placement[i]][0]
                    placement[i] = new_placement[i]
                elif direction == "R":
                    new_placement[i] = file[placement[i]][1]
                    placement[i] = new_placement[i]
                else:
                    raise Exception("Unexpected direction:", direction)

            steps += 1

            # TODO: delete log printout
            log.write("steps: ")
            log.write(str(steps))
            log.write("\nplacement: ")
            log.write(str(placement))
            log.write("\n\n")
            log.close()
            if steps >= 500000:
                raise Exception("Too Many Steps! Aborting program...")

            # tests to see if done
            if all_end_in_z(placement):
                return steps

            # tests for infinite loops; ex "BBB" = ("BBB", "BBB")
            for i in range(0, len(placement)):
                if placement[i] == file[placement[i]][0] and placement[i] == file[placement[i]][1] and not placement[i][-1] == "Z":
                    # If infinite loop found at "TSZ" = ("TSZ", "TSZ"), that's fine. Only infinite loops not ending in "Z" are a problem
                    raise Exception("Infinite Loop found at:", placement[i], placement)


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