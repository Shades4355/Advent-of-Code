from advent4pt1 import get_input, parse_card


def total_scratchcards(scratchcard_stack:dict):
    '''Takes in a scratchcard dictionary; 
    outputs the total number of cards'''
    # stack_of_cards | key = Card #
    # value = the number of that card in the stack
    stack_of_cards = {} 
    card_num = 1

    # prime the stack with first card:
    stack_of_cards['Card 1'] = 1

    # add cards to stack of cards (dict = str: int)
    for card_num in range(1, len(scratchcard_stack) + 1):
        current_card = f"Card {card_num}"
        num_wins = read_scratchcard(scratchcard_stack[current_card])
        if num_wins > 0:
            for i in range(1, num_wins + 1):
                new_card_id = card_num + i
                new_card = f"Card {new_card_id}"
                if new_card_id <= len(scratchcard_stack):
                    add_cards = stack_of_cards[current_card]
                    if new_card in stack_of_cards:
                        stack_of_cards[new_card] += add_cards
                    else:
                        stack_of_cards[new_card] = 1 + add_cards
        else:
            # If num of wins is 0, 
            new_card_id = card_num + 1
            # ...and new card is within the range of the data set,
            if new_card_id <= len(scratchcard_stack):
                # ...add original to stack; then continue
                if new_card in stack_of_cards:
                    stack_of_cards[new_card] += 1
                else:
                    stack_of_cards[new_card] = 1
            # ...if new card is outside data set; terminate loop
            else:
                break

    # finds the num of cards in the stack of cards
    num_cards = 0
    for i in stack_of_cards:
        # num_cards = only the copies in the stack_of_cards
        num_cards += stack_of_cards[i]
    
    # returns copies + originals
    return num_cards


def read_scratchcard(card:list):
    '''Takes in a list of two lists; 
    compares each number to the list of winning numbers; 
    increments points by 1 if num is in the list of winning numbers'''
    total = 0
    num_wins = 0
    numbers = card[1]
    winning_num = card[0]

    # compare num in numbers section to list of 'Winning Numbers'
    # If num is in 'winning numbers', increment 'total' by 1
    for num in numbers:
        if num in winning_num:
            num_wins += 1
    if num_wins > 0:
        total += num_wins
    
    return num_wins


def start(file:str):
    scratchcard_stack = parse_card(get_input(file))
    
    return total_scratchcards(scratchcard_stack)


#########
# start #
#########
if __name__ == "__main__":
    print(start("day4input.txt"))