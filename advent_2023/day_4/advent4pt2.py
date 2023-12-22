from advent4pt1 import get_input, parse_card

def read_scratchcard_updated(scratchcard:dict):
    '''Takes in a scratchcard dictionary; 
    outputs the total number of cards'''
    total = 0

    # read one card
    # count the number of cards won

    return total


def start(file:str):
    scratchcard = parse_card(get_input(file))
    
    return read_scratchcard_updated(scratchcard)


#########
# start #
#########
if __name__ == "__main__":
    print(start("day4input.txt"))