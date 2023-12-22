from advent4pt1 import get_input, parse_card

def total_scratchcards(scratchcard:dict):
    '''Takes in a scratchcard dictionary; 
    outputs the total number of cards'''
    stack_of_cards = []
    card_num = 1

    # read one card at a time
    for card_stack in scratchcard:
        for card in card_stack:
            for key in card:
                num_wins = read_scratchcard(scratchcard, key)
                if num_wins > 0:
                    card_num += 1
                    for i in range(num_wins):
                        new_card = card_num + i
                        if new_card <= len(scratchcard):
                            stack_of_cards.append(scratchcard[f"Card {new_card}"])    
                else:
                    card_key = f"Card {new_card}"
                    if scratchcard[card_key] == stack_of_cards[-1].keys():
                        break

    # returns the stack of cards + the original cards
    return len(stack_of_cards) + len(scratchcard)


def read_scratchcard(scratchcard:dict, key:str):
    '''Takes in a dictionary; 
    compares each num to the list of winning numbers; 
    increments points by 1 if num is in the list of winning numbers'''
    total = 0
    num_wins = 0

    for num in scratchcard[key][1]:
        if num in scratchcard[key][0]:
            num_wins += 1
    if num_wins > 0:
        total += num_wins
    
    return num_wins


def start(file:str):
    scratchcard = parse_card(get_input(file))
    
    return total_scratchcards(scratchcard)


#########
# start #
#########
if __name__ == "__main__":
    print(start("day4input.txt"))