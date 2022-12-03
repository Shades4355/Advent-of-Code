

def open_file(file: str, x: int = 0) -> list:
    '''Open a file in the 2022 folder \n
    If X is greater than 0, returns a list of first and X+1 values\n
    Otherwise, returns a list containing one item per line of text'''
    file = open(f"2022/{file}", "r")
    lines = []
    n = 0

    for line in file:
        if x > 0:
            lines.append((line[0], line[x]))
        else:
            lines.append(line)
    file.close()

    return lines


def compare(opponent_move: str, own_move: str, current_score: int) -> int:
    '''Compare two throws in Rock-Paper-Scissors \n
    Returns the current score based on win-draw-lose and the shape thrown'''
    total_score = current_score
    if own_move == "X":
        total_score = rock_throw(opponent_move, current_score)
    elif own_move == "Y":
        total_score = paper_throw(opponent_move, current_score)
    elif own_move == "Z":
        total_score = scissor_throw(opponent_move, current_score)
    return total_score


def rock_throw(opponent_move: str, current_score: int) -> int:
    '''Throw for Rock \n
    Returns the current score based on win-draw-lose + 1'''
    score = current_score
    if opponent_move == "A":
        # Rock
        score += 1 + draw()
    elif opponent_move == "B":
        # Paper
        score += 1 + lose()
    elif opponent_move == "C":
        # Scissors
        score += 1 + win()
    return score


def paper_throw(opponent_move: str, current_score: int) -> int:
    '''Throw for Paper \n
    Returns the current score based on win-draw-lose + 2'''
    score = current_score
    if opponent_move == "A":
        # Rock
        score += 2 + win()
    elif opponent_move == "B":
        # Paper
        score += 2 + draw()
    elif opponent_move == "C":
        # Scissors
        score += 2 + lose()
    return score


def scissor_throw(opponent_move: str, current_score: int) -> int:
    '''Throw for Scissors \n
    Returns the current score based on win-draw-lose and + 3'''
    score = current_score
    if opponent_move == "A":
        # Rock
        score += 3 + lose()
    elif opponent_move == "B":
        # Paper
        score += 3 + win()
    elif opponent_move == "C":
        # Scissors
        score += 3 + draw()
    return score


def win() -> int:
    '''Points for winning'''
    return 6


def draw() -> int:
    '''Points for a Draw'''
    return 3


def lose() -> int:
    '''Points for Losing'''
    return 0


def find_score(rounds: list, current_score=0) -> list:
    '''Find a total score based on a starting score (default 0)\n
    Returns a list of "total score" and "number of rounds"'''
    total_score = current_score
    num_of_rounds = 0
    for opponent_move, own_move in rounds:
        total_score = compare(opponent_move, own_move, total_score)
        num_of_rounds += 1
    return [total_score, num_of_rounds]


def validate_answer(total_score: int, total_turns: int) -> None:
    '''Validates results from Rock-Paper-Scissors competition\n
    Returns "Answer too high!" if the input score is higher than that of a perfect game\n
    Returns "Answer too low!" if the input score is lower than a lose every round'''
    if total_score > total_turns * (6+3):
        print("Answer too high!")
        print(total_score)
        print("Matches Played:", total_turns)
    elif total_score < total_turns * 1:
        print("Answer too low!")
        print(total_score)
        print("Matches Played:", total_turns)
    else:
        print("score:", total_score)
        print("Matches Played:", total_turns)


#########
# start #
#########

if __name__ == "__main__":
    turns = open_file("advent2pt1.txt", 2)
    total_score, total_turns = find_score(turns)
    validate_answer(total_score, total_turns)
