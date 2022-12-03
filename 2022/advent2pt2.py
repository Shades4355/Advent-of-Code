from advent2pt1 import open_file, validate_answer


def compare(opponent_move: str, win_state: str, current_score: int) -> int:
    '''Compares Opponent's move vs win state, and determines a score\n
    Inputs:
    \tOpponent's move: A = Rock, B = Paper, C = Scissors\n
    \tWin state: X = Lose, Y = Draw, Z = Win'''

    total_score = current_score

    if win_state == "X":
        total_score += lose(opponent_move)
    elif win_state == "Y":
        total_score += draw(opponent_move)
    elif win_state == "Z":
        total_score += win(opponent_move)

    return total_score


def find_score(rounds: list, current_score: int = 0) -> list:
    '''Find a total score based on a starting score (default 0)\n
    Returns a list of "total score" and "number of rounds"'''
    total_score = current_score
    num_of_rounds = 0
    for opponent_move, win_state in rounds:
        total_score = compare(opponent_move, win_state, total_score)
        num_of_rounds += 1
    return [total_score, num_of_rounds]


def win(opponent_move: str) -> int:
    score = 6

    if opponent_move == "A":
        # you throw Paper
        score += 2
    elif opponent_move == "B":
        # you throw Scissors
        score += 3
    elif opponent_move == "C":
        # you throw Rock
        score += 1

    return score


def draw(opponent_move: str) -> int:
    score = 3

    if opponent_move == "A":
        # you throw Rock
        score += 1
    elif opponent_move == "B":
        # you throw Paper
        score += 2
    elif opponent_move == "C":
        # you throw Scissors
        score += 3

    return score


def lose(opponent_move: str) -> int:
    score = 0

    if opponent_move == "A":
        # you throw Scissors
        score += 3
    elif opponent_move == "B":
        # you throw Rock
        score += 1
    elif opponent_move == "C":
        # you throw Paper
        score += 2

    return score


#########
# start #
#########

if __name__ == "__main__":
    turns = open_file("advent2pt1.txt", 2)
    total_score, total_turns = find_score(turns)
    validate_answer(total_score, total_turns)
