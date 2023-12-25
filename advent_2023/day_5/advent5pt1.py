

def get_input(location):
    '''Takes in a file; outputs a 1D list'''

    array = []
    file = open(location, 'r')

    for line in file:
        array.append(line.strip())

    file.close()

    return array


def parse_input(file:list): # TODO: investigate why this is failing
    '''Takes in a 1D list; outputs a dictionary'''
    dictionary = {}
    key = ""

    # parse lines from file
    for line in file:
        # first line gets parsed different from the rest
        if line.find("seeds") > -1:
            key = line.split(": ")[0]
            value = line.split("")[1]
            dictionary[key] = value.split()
        # for 'map' lines, use line as new key
        elif line.find("map") > -1:
            key = line
            iteration = 0
            dictionary[key] = []
        # ignore empty lines
        elif line == "":
            continue
        # for numeric lines, add list of numbers to relevant map
        else:
            dictionary[key][iteration].append(line.split())
            iteration += 1

    return dictionary


def start(location):
    file = get_input(location)


#########
# start #
#########
if __name__ == "__main__":
    start("advent5input.txt")