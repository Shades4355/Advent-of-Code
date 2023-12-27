

def create_blank_maps(parsed_input:list, length:int):
    '''creates blank maps, based on a given int. Ex: 100 would yield a list 100 characters long'''
    maps_dict = {}

    for key in parsed_input:
        if key == "seeds":
            continue
        elif key.find("-to-") > -1:
            source, dest = key.split("-to-")
            maps_dict[f"blank_{dest}_map"] = get_blank_map_list(length)
        else:
            raise Exception("\nUnexpected key in parsed_input:", key)
    
    return maps_dict


def fill_map(source:list, par_fill_map:list):
    '''Takes in a source list and a partially filled list; outputs a filled in list'''
    filled_map = par_fill_map

    for i in range(0, len(filled_map)):
            if filled_map[i] == "":
                filled_map[i] = source[i]

    return filled_map


def fill_in_maps(parsed_input:list, seed_list:list, blank_maps:list, order:list):
    '''Takes in the parsed input, a completed seed list, a dictionary of blank maps, and a list to control iteration order; outputs a dictionary of completed maps'''
    maps = {}
    par_filled_maps = {}
    
    for key in order:
        source, dest = key.split("-to-")
        if source == "seed":
            source_list = seed_list
        else:
            source_list = maps[source]
        dest_list = blank_maps[f"blank_{dest}_map"]

        rules = parsed_input[key]

        # TODO: delete
        print(f"\nsource map: {source}")
        print(f"blank_{dest}_map:")

        par_filled_maps[f"par_{dest}_map"] = par_fill_map(source_list, dest_list, rules)
        if source == "seed":
            source_list = seed_list
        else:
            source_list = maps[source]
        maps[dest] = fill_map(source_list, par_filled_maps[f"par_{dest}_map"])

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
                dest, source, length = map[key][map_list]
                if dest + length > last_seed:
                    last_seed = dest + length
                if source + length > last_seed:
                    last_seed = source + length
    
    return last_seed - 1


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

    for key in rules:
        index = -1
        additions = 0
        r_dest, r_source, r_len = rules[key]
        # index = source.index(r_source)

        # Test:
        indices = []
        for i in range(len(source)):
            if source[i] == r_source:
                indices.append(i)
        if not len(indices) == 1:
            raise Exception(f"Wrong number of indices found: {indices} | r_source: {r_source}")
        else:
            index = indices[0]

        if index > -1:
            for i in range(0, r_len):
                try:
                    par_filled_map[index + i] = r_dest + i
                except IndexError:
                    len_to_add = (index + i) - len(par_filled_map)
                    for j in range(0, len_to_add):
                        par_filled_map.append("")
                    len_to_add = (index + i) - len(par_filled_map)
                    additions += 1

                #TODO: delete
                print("r_source", r_source,
                    "| Index:", index,
                    "| r_len:", r_len,
                    "| Index + r_len - 1:", index + r_len - 1,
                    "| i:", i,
                    "| index + i:", index + i)
                print("par_map:\n", par_filled_map)
        else:
            raise Exception("No Index found")
        print("additions added to list:", additions) # TODO: delete

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
    
    order = [
        "seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location"]

    blank_maps = create_blank_maps(parsed_input, len(seed_list))

    filled_maps = fill_in_maps(parsed_input, seed_list, blank_maps, order)

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