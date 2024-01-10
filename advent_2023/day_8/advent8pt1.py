

def get_input(location):
    file_list = []

    file = open(location, "r")

    for line in file:
        file_list.append(line)

    file.close() 

    return file_list


def parse_input(file:list):
    dictionary = {}
    directions = []
    
    for cha in file[0].strip():
        directions.append(cha)

    dictionary["directions"] = directions
    dictionary["start"] = file[2].split(" = ")[0]

    for i in range(2, len(file)):
        key, value = file[i].split(" = ")
        dictionary[key] = value.strip().strip("(").strip(")").split(", ")

    return dictionary


def follow_directions(dictionary:dict):
    steps = 0
    placement = ""

    placement = dictionary["start"]

    while not placement == "ZZZ":
        for direction in dictionary["directions"]:
            if direction == "L":
                placement = dictionary[placement][0]
            elif direction == "R":
                placement = dictionary[placement][1]
            else:
                raise Exception("Unexpected direction:", direction)

            steps += 1

            if placement == "ZZZ":
                break
            elif placement == dictionary[placement][0] and placement == dictionary[placement][1]:
                raise Exception("Infinite Loop found at:", placement)
    
    return steps



def start(location:str):
    file = get_input(location)
    parsed_file = parse_input(file)

    return follow_directions(parsed_file)


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))