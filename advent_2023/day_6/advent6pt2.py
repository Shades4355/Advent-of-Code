from advent6pt1 import run_race

def get_input(location:str):
    file = open(location, "r")

    dictionary = {}
    for line in file:
        str_num = ""
        key, value = line.split(":")
        
        for num in value.split():
             str_num += num

        dictionary[key] = int(str_num)
    
    file.close()

    return dictionary


def start(location:str):
    parsed_info = get_input(location)

    return run_race(parsed_info["Time"], parsed_info["Distance"])



#########
# start #
#########
if __name__ == "__main__":
    print(start("day6input.txt"))