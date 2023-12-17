def get_input():
    '''Convert text file of raw data into a list'''
    file = open("advent2input.txt", "r")

    games = []

    for game in file:
        games.append(game)
    file.close()

    return games


def get_dic(games:list):
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


def start():
    game_dic = get_dic(get_input())
    

#########
# start #
#########
if __name__ == "__main__":
    start()
