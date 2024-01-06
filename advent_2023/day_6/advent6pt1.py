
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
    # Rules:
        # starting speed = 0 mm/s
        # for each whole ms held, speed increases by 1 mm/s
        # while held, make no forward movement
    answer = 0

    for i in range(1, time):
        if (i * (time - i)) >= (distance):
            answer += 1
        
    return answer

def start(file:str):
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