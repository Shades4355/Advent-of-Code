
def getInput(location):
    file = open(location, "r")

    dictionary = {}
    value_array = []
    for line in file:
        key, value = file.split(":").strip()
        value_array = value.split()
        dictionary[key] = value_array
    
    return dictionary


