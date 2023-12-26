

def create_blank_maps(parsed_input:list, length:int):
    maps_dict = {}

    for key in parsed_input:
        if key == "seeds":
            continue
        elif key.find("-to-") > -1:
            source, dest = key.split("-to-")
            maps_dict[f"blank_{dest}_list"] = get_blank_map_list(length)
        else:
            raise Exception("\nUnexpected key in parsed_input:", key)
    
    return maps_dict


def fill_map(source:list, par_fill_map:list):
    '''Takes in a source list and a partially filled list; outputs a filled in list'''
    filled_map = par_fill_map
    loop = True

    while loop:
        for i in range(0, len(filled_map)):
            try:
                index = filled_map[i].index("")
                filled_map[i][index] = source[index]
            except ValueError:
                loop = False

    return filled_map


def fill_in_maps(parsed_input:list, seed_list:list, blank_maps:list):
    maps = {}
    par_filled_maps = []
    
    for key in parsed_input:
        if key == "seeds":
            continue
        else:
            source, dest = key.split("-to-")
            if source == "seed":
                source_list = seed_list
            else:
                source_name = f"par_{source}_map"
                source_list = par_filled_maps[source_name]
            dest_name = f"blank_{dest}_map"
            dest_list = blank_maps[dest_name]

            rules = parsed_input[key]
            par_filled_maps.append(par_fill_map(source_list, dest_list, rules))

            if source == "seed":
                source_list = seed_list
            else:
                source_name = f"par_{source}_map"
                source_list = par_filled_maps[source_name]
            maps[dest] = fill_map(source_list, par_filled_maps)

    return maps


def find_last_seed(map:dict):
    last_seed = 0


    for key in map:
        if key == "seeds":
            for num in map[key]:
                if num > last_seed:
                    last_seed = num
        else:
            for map_list in map[key]:
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


def get_input(location:str):
    '''Takes in a file; outputs a 1D list'''

    array = []
    file = open(location, 'r')

    for line in file:
        array.append(line.strip())

    file.close()

    return array


def get_seed_list(highest:int):
    all_seeds = []

    for i in range(0, highest + 1):
        all_seeds.append(i)

    return all_seeds


def par_fill_map(source:list, destination:list, rules:list):
    '''takes in a filled source list and a blank destination list; outputs a partially filled list'''
    par_filled_map = destination

    for i in range(0, len(rules)):
        r_dest, r_source, r_len = rules[str(i)]
        index = source.index(r_source)
        for i in range(0, r_len):
            par_filled_map[index + i] = r_dest + i

    return par_filled_map


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
            key = line.strip(" map:")
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


def start(location:str):
    answer = 0
    parsed_input = parse_input(get_input(location))
    last_seed = find_last_seed(parsed_input)
    seed_list = get_seed_list(last_seed)
    
    blank_maps = create_blank_maps(parsed_input, len(seed_list))
    
    filled_maps = fill_in_maps(parsed_input, seed_list, blank_maps)

    lowest = None
    for seed in parsed_input["seeds"]:
        index = seed_list.index(seed)
        if lowest < filled_maps[-1][index]:
            lowest = filled_maps[-1][index]
            answer = seed_list[index]
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