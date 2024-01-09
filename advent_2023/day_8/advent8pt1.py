

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

    for i in range(2, len(file)):
        key, value = file[i].split(" = ")
        lv, rv = value.strip().strip("(").strip(")").split(", ")
        
        dictionary[key] = [lv, rv]

    return dictionary


def start(location:str):
    file = get_input(location)
    parsed_file = parse_input(file)
    
    
    return "hi"


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))