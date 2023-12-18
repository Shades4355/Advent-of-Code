from advent2pt1 import get_input, get_dic


def find_min(game_dic:dict):
    '''Find the minimum value for a particular color'''
    # {round_num: {color: number}}
    min_value = {"red": 0, "green": 0, "blue": 0}
    
    for round in game_dic:
        for color in game_dic[str(round)]:
            if min_value[color] < int(game_dic[round][color]):
                min_value[color] = int(game_dic[round][color])
    
    return min_value


def multiply(num_list:dict):
    '''take in a dictionary of colors and numbers;
    returns an int of the numbers multiplied together'''
    total = 1
    for color in num_list:
        total *= num_list[color]
    
    return total


def add_powers(powers:dict):
    '''Adds the values of a dictionary together'''
    total = 0

    for game in powers:
        total += powers[game]
    
    return total


def start():
    '''Start program'''
    min_values = {}
    game_total = {}
    total = 0

    game_dic = get_dic(get_input())
    for game in game_dic:
        min_values = find_min(game_dic[game])
        game_total[str(game)] = multiply(min_values)

    print(add_powers(game_total))


#########
# start #
#########
if __name__ == "__main__":
    start()
