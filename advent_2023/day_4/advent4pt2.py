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
    for key in scratchcard_stack:
        num_wins = read_scratchcard(scratchcard_stack[key])
        if num_wins > 0:
            if card_num > len(scratchcard_stack):
                raise Exception(f"Card_num too high: {card_num}")
            for i in range(1, num_wins + 1):
                new_card = card_num + i
                if new_card <= len(scratchcard_stack):
                    add_cards = stack_of_cards[f"Card {card_num}"]
                    if f"Card {new_card}" in stack_of_cards:
                        stack_of_cards[f"Card {new_card}"] += add_cards
                    else:
                        stack_of_cards[f"Card {new_card}"] = 1 + add_cards
        else:
            # If num of wins is 0, add original to stack; then continue
            new_card = card_num + 1
            if not new_card > len(scratchcard_stack):
                stack_of_cards[f"Card {new_card}"] = 1
        card_num += 1

    # finds the num of cards in the stack of cards
    num_cards = 0
    for i in stack_of_cards:
        # num_cards = only the copies in the stack_of_cards
        num_cards += stack_of_cards[i] - 1
    
    # returns copies + originals
    return num_cards + len(scratchcard_stack)


def read_scratchcard(card:list):
    '''Takes in a list of two lists; 
    compares each number to the list of winning numbers; 
    increments points by 1 if num is in the list of winning numbers'''
    total = 0
    num_wins = 0

    # compare num in numbers section to list of 'Winning Numbers'
    # If num is in 'winning numbers', increment total by 1
    for num in card[1]:
        if num in card[0]:
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