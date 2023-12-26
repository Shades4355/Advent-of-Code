

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


def get_blank_map_list(seed_len:int):
    soil_list = []

    for i in range(0, seed_len):
        soil_list.append("")
    
    return soil_list


def start(location:str):
    answer = 0
    parsed_input = parse_input(get_input(location))
    last_seed = find_last_seed(parsed_input)
    seed_list = get_seed_list(last_seed)
    
    blank_soil_list = get_blank_map_list(len(seed_list))
    blank_fert_list = get_blank_map_list(len(seed_list))
    blank_water_list = get_blank_map_list(len(seed_list))
    blank_light_list = get_blank_map_list(len(seed_list))
    blank_temp_list = get_blank_map_list(len(seed_list))
    blank_humidity_list = get_blank_map_list(len(seed_list))
    blank_location_list = get_blank_map_list(len(seed_list))

    # propagate soil_list
    # propagate fert_list
    # propagate water_list
    # propagate light_list
    # propagate temp_list
    # propagate humidity_list
    # propagate location_list

    # find index for (seed list in parsed_input) in (seed_list) 
        # compare index in seed_list to same index in location_list
    # compare found location_list[index] values to find lowest
        # compare back to seed_list
        # return seed_list[index]

    return answer


#########
# start #
#########
if __name__ == "__main__":
    print(start("advent5input.txt"))