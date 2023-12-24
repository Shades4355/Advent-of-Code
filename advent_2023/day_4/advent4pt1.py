
def get_input(location:str):
    '''parses a txt file into a 1D list'''
    array = []
    file = open(location, "r")

    for line in file:
        array.append(line.strip())
    
    file.close()
  
    return array


def parse_card(one_d_list:list):
    '''Takes in a 1D list; outputs a dictionary'''
    scratchcard = {}

    for row in one_d_list:
        key, temp_numbers = row.split(": ")
        winning_nums, numbers = temp_numbers.split(" | ")
        
        winning_numbers = []
        winning_numbers = winning_nums.split()

        all_nums = []
        all_nums = numbers.split()
        
        scratchcard[" ".join(key.split())] = [winning_numbers, all_nums]

    return scratchcard


def read_scratchcard(scratchcard:dict):
    '''Takes in a dictionary; 
    compares each num to the list of winning numbers; 
    increments points by 1 if num is in the list of winning numbers'''
    point_total = 0

    for card in scratchcard:
        points = 0
        for num in scratchcard[card][1]:
            if num in scratchcard[card][0]:
                points += 1
        if points > 0:
            point_total += 2 ** (points - 1)
    
    return point_total


def start(file:str):
    '''Starts the program; returns the final total'''
    scratchcard = parse_card(get_input(file))
        
    # uses return instead of print so as to be testable
    return read_scratchcard(scratchcard)


#########
# start #
#########
if __name__ == "__main__":
    print(start("day4input.txt"))