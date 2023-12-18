def get_input():
    '''Convert text file of raw data into a list'''
    file = open("advent2input.txt", "r")

    games = []

    for game in file:
        games.append(game)
    file.close()

    return games


def get_dic(games:list):
    '''Converts a list into a dictionary'''
    dic = {}
    round_played = []

    for game in games:
        temp1 = game.split(": ") # ["Game" game_id, games_played]
        game_id = str(temp1[0].split()[1])
        games_played_list = temp1[1].split("; ") # [game_played, game_played, ... ]
        dic[game_id] = {}
        round = 1
        for game in games_played_list:
            rounds_played = game.split(", ") # ["1 red", "1 blue", ... ]
            dic[game_id][str(round)] = {}
            for rounds in rounds_played:
                color = rounds.split()[1]
                num = rounds.split()[0]
                dic[game_id][str(round)][color] = num
            round += 1
    
    # data structure
    # {game_id:
    #   {round_num:
    #       {color: number}
    #   }
    # }
    return dic


def test_game(game_dic:dict):
    '''Tests if a game is valid'''
    # {round_num: {color: number}}
    for round in game_dic:
        for color in game_dic[round]:
            num = int(game_dic[round][color])
            if color == "red" and num > 12:
                return False
            elif color == "green" and num > 13:
                return False
            elif color == "blue" and num > 14:
                return False

    return True


def add_ids(game_id_list:list):
    total = 0

    for id in game_id_list:
        total += int(id)

    return total


def start():
    game_dic = get_dic(get_input())
    # {game_id: {round_num: {color: number}}}
    valid_games = []
    for game_id in game_dic:
        if test_game(game_dic[game_id]):
            valid_games.append(game_id)

    print(add_ids(valid_games))
    

#########
# start #
#########
if __name__ == "__main__":
    start()
