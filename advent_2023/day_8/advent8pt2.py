from advent8pt1 import get_input

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

    return "Hi"


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))