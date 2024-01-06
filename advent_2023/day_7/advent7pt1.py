import numpy as np

def get_input(location:str):
    dic = {}
    hand_num = 1

    file = open(location, 'r')

    for line in file:
        hand, wager =  line.split()
        dic[f"hand {hand_num}"] = {}
        dic[f"hand {hand_num}"]["hand"] = hand
        dic[f"hand {hand_num}"]["wager"] = int(wager)
        dic[f"hand {hand_num}"]["hand type"] = ""
        dic[f"hand {hand_num}"]["ranking"] = 0

        hand_num += 1

    file.close()

    return dic


def find_hand_type(hand_dic:dict):
    '''Takes in a hand dictionary (ex: "hand 1"); outputs the type of hand it is (ex: "Full House) as a string'''
    def x_of_a_kind(hand:list, num:int):
        '''determines if there is x of a kind, where x is an integer (ex: 4 of a kind); outputs True or False'''
        for cha in np.unique(hand):
            if hand.count(cha) == num:
                return True
        return False    
    
    def find_two_pair(hand:list):
        '''Determines if there are exactly 2 sets of paired cards (plus a 5th unpaired card)'''
        count = 0

        if not len(np.unique(hand)) == 3:
            return False
        
        for cha in np.unique(hand):
            if hand.count(cha) == 2:
                count += 1
        if not count == 2:
            return False
    
        return True

    hand = []

    for cha in hand_dic["hand"]:
        hand.append(cha)

    if len(np.unique(hand)) == 1:
        return "Five of a Kind"
    elif x_of_a_kind(hand, 4):
            return "Four of a Kind"
    elif x_of_a_kind(hand, 3) and len(np.unique(hand)) == 2:
        return "Full House"
    elif x_of_a_kind(hand, 3):
        return "Three of a Kind"
    elif find_two_pair(hand):
        return "Two Pair"
    elif x_of_a_kind(hand, 2):
        return "One Pair"
    else:
        return "High Card"


def order_hands(hands_dic:dict):
    ordered_dic = {}
    card_dic = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    for key in hands_dic:
        ordered_dic[key] = hands_dic[key]
    


    return ordered_dic

def start(location:str):
    parsed_file = get_input(location)
    
    for hand_key in parsed_file:
        parsed_file[hand_key]["hand type"] = find_hand_type(parsed_file[hand_key])

    return "Hi"

#########
# start #
#########
if __name__ == "__main__":
    print(start("day7input.txt"))



# Notes:
# Every hand is exactly one type. From strongest to weakest, they are:
    # * Five of a kind, where all five cards have the same label: AAAAA
    # * Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # * Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # * Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # * Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # * One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # * High card, where all cards' labels are distinct: 23456

# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

