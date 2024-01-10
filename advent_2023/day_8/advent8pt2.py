from advent8pt1 import get_input


def all_end_in_z(placements:list):
    for num in placements:
        if not num[-1] == "Z":
            return False
    return True


def follow_directions(file:dict):
    steps = 0
    placement = []

    for num in file["start"]:
        placement.append(num)

    looping = True
    while looping:
        for direction in file["directions"]:
            for i in range(0, len(placement)):
                if direction == "L":
                    placement[i] = file[placement[i]][0]
                elif direction == "R":
                    placement[i] == file[placement[i]][1]
                else:
                    raise Exception("Unexpected direction:", direction)
            steps += 1
                
            if all_end_in_z(placement):
                looping = False

    return steps


def parse_input(file:list):
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
    file = get_input(location)
    parsed_file = parse_input(file)

    return follow_directions(parsed_file)


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))