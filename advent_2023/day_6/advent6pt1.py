

def find_longest_press(time:int, distance:int):
        '''finds the longest valid time to hold the button'''
        for i in range(time, -1, -1):
            if (i * (time - i)) >= (distance):
                return i


def find_shortest_press(time:int, distance:int):
        '''finds the shortest valid time to hold the button'''
        for i in range(0, time):
            if (i * (time - i)) >= (distance):
                return i


def get_input(location:str):
    '''Takes in a txt file; outputs a dictionary'''
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


def run_race(time:int, distance:int):
    '''takes in a time and distance integer; outputs the number of possible answers'''

    shortest_press = find_shortest_press(time, distance)
    longest_press = find_longest_press(time, distance)
    
    return longest_press - shortest_press + 1


def start(file:str):
    parsed_info = get_input(file)

    answer = 1
    for i in range(0, len(parsed_info["Time"])):
         answer *= run_race(parsed_info["Time"][i], parsed_info["Distance"][i])

    return answer


#########
# start #
#########
if __name__ == "__main__":
    print(start("day6input.txt"))