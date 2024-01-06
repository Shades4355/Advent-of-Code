
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
    def x_of_a_kind(hand:list, num:int):
        for cha in hand:
            if hand.count(cha) == num:
                return True
        return False    
    
    hand = []

    for cha in hand_dic["hand"]:
        hand.append(cha)

    if len(hand.unique()) == 1:
        return "Five of a Kind"
    
    if x_of_a_kind(hand, 4):
            return "Four of a kind"
    elif x_of_a_kind(hand, 3) and hand.unique() == 2:
        return "Full House"
    elif x_of_a_kind(hand, 3):
        return "Three of a kind"
    # elif ?????:
        # return "Two Pair"
    elif x_of_a_kind(hand, 1):
        return "One Pair"
    else:
        return "High Card"


def start(location:str):
    parsed_file = get_input(location)

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

