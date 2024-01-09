

def get_input(location):
    file_list = []

    file = open(location, "r")

    for line in file:
        file_list.append(line)

    file.close() 
    
    return file_list


def start(location:str):
    file = get_input(location)

    return "hi"


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day8input.txt"))