
def get_input(location):
    file = open(location, "r")

    dictionary = {}
    for line in file:
        value_array = []
        key, value = line.split(":")
        
        for num in value.split():
            value_array.append(int(num))

        dictionary[key] = value_array
    
    file.close()

    return dictionary


def start(file):
    parsed_info = get_input(file)

    # determine number of ways to win
    # record number of ways to win each race
    # multiply number of ways together
    # Return solution

    return "hi"


#########
# start #
#########
if __name__ == "__main__":
    print(start("day6input.txt"))