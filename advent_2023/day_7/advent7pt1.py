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


def get_wagers(hand_dic:dict):
    answer = 0

    for key in hand_dic:
        answer += hand_dic[key]["wager"] * hand_dic[key]["ranking"]

    return answer


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
    hand_ranking = 1
    hc_list = {}
    one_pair_list = {}
    two_pair_list = {}
    three_kind_list = {}
    fh_list = {}
    four_kind_list = {}
    five_kind_list = {}

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

    for key in ordered_dic:
        if ordered_dic[key]["hand type"] == "High Card":
            hc_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "One Pair":
            one_pair_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "Two Pair":
            two_pair_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "Three of a Kind":
            three_kind_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "Full House":
            fh_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "Four of a Kind":
            four_kind_list[key] = ordered_dic[key]
        elif ordered_dic[key]["hand type"] == "Five of a Kind":
            five_kind_list[key] = ordered_dic[key]
        else:
            raise Exception("Unexpected hand type:", key, ordered_dic[key]["hand type"])

    # for 1+ 'high card' hands...
    if len(hc_list) > 0:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in hc_list:
            presorted_list[key] = []
            for cha in hc_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))
        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1
    
    # for 1+ 'One Pair' hands...
    if len(one_pair_list) > 0:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in one_pair_list:
            presorted_list[key] = []
            for cha in one_pair_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1

    # for 1+ 'Two Pair' hands...
    if len(two_pair_list) > 1:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in two_pair_list:
            presorted_list[key] = []
            for cha in two_pair_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1
    
    # for 1+ 'Three of a Kind' hand...
    if len(three_kind_list) > 0:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in three_kind_list:
            presorted_list[key] = []
            for cha in three_kind_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1

    # for 1+ 'Full House' hands...
    if len(fh_list) > 1:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in fh_list:
            presorted_list[key] = []
            for cha in fh_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1

    # for 1+ 'Four of a Kind' hand...
    if len(four_kind_list) > 1:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in four_kind_list:
            presorted_list[key] = []
            for cha in four_kind_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1

    # for 1+ 'Five of a Kind' hands...
    if len(five_kind_list) > 1:
        # sort list based on card_dic; lowest to highest
        presorted_list = {}
        for key in five_kind_list:
            presorted_list[key] = []
            for cha in five_kind_list[key]["hand"]:
                presorted_list[key].append(card_dic[cha])

        sorted_list = dict(sorted(presorted_list.items(), key=lambda item: item[1]))

        for hand in sorted_list:
            ordered_dic[hand]["ranking"] = hand_ranking
            hand_ranking += 1

    return ordered_dic


def start(location:str):
    parsed_file = get_input(location)
    
    for hand_key in parsed_file:
        parsed_file[hand_key]["hand type"] = find_hand_type(parsed_file[hand_key])

    ordered_dic = order_hands(parsed_file)

    return get_wagers(ordered_dic)


#########
# start #
#########
if __name__ == "__main__":
    print(start("day7input.txt"))
