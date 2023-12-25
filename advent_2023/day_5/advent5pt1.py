

def get_input(location:str):
    '''Takes in a file; outputs a 1D list'''

    array = []
    file = open(location, 'r')

    for line in file:
        array.append(line.strip())

    file.close()

    return array


def parse_input(file:list):
    '''Takes in a 1D list; outputs a dictionary'''
    dictionary = {}
    key = ""

    # parse lines from file
    for line in file:
        # first line gets parsed different from the rest
        if line.find("seeds") > -1:
            key = line.split(": ")[0]
            value = line.split(": ")[1]
            dictionary[key] = []
            for num in value.split():
                dictionary[key].append(int(num))
        # for 'map' lines, use line as new key
        elif line.find("map") > -1:
            key = line
            iteration = 0
            dictionary[key] = {}
        # ignore empty lines
        elif line == "":
            continue
        # for numeric lines, add list of numbers to relevant map
        else:
            dictionary[key][str(iteration)] = []
            for num in line.split():
                dictionary[key][str(iteration)].append(int(num))
            iteration += 1

    return dictionary


def get_seed_list(highest:int):
    all_seeds = []

    for i in range(0, highest + 1):
        all_seeds.append(i)

    return all_seeds


def find_last_seed(map:dict):
    last_seed = 0


    for key in map:
        if key == "seeds":
            for num in map[key]:
                if num > last_seed:
                    last_seed = num
        else:
            for map_list in map[key]:
                # [88, 18, 7]
                nums = map[key][map_list]
                if nums[0] + nums[2] > last_seed:
                    last_seed = nums[0] + nums[2]
                if nums[1] + nums[2] > last_seed:
                    last_seed = nums[1] + nums[2]
    
    return last_seed


def start(location:str):
    answer = 0
    parsed_input = parse_input(get_input(location))
    last_seed = find_last_seed(parsed_input)
    seed_list = get_seed_list(last_seed)


    return answer


#########
# start #
#########
if __name__ == "__main__":
    print(start("advent5input.txt"))