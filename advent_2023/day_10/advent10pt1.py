

def find_start(file:list):
    '''take in a 2D file; outputs the location of "S"'''
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "S":
                return [i, j]

    raise Exception("No start point found")


def follow_pipes(file:list, start_point:list):
    '''takes in a list of pipes and a start position; return how many steps away the farthest point is'''

    # TODO: need to figure out how to trace pos1 and pos2 at the same time

    i, j = start_point
    answer = 0
    pos1 = [-1, 0]
    pos2 = [1, 0]

    while True:
        k, l = pos1
        position = file[i + k][j + l]
        if i + k < len(file):
            if position == "|" and k == 1:
                pos1 = [i + k - 1, j]
                answer += 1
            elif position == "|" and k == -1:
                pos1 = [i + k + 1, j]
                answer += 1
            elif position == "-" and l == 1:
                pos1 = [i, j + l + 1]
                answer += 1
            elif position == "-" and l == -1:
                pos1 = [i, j + l - 1]
                answer += 1
            # TODO: add the rest of the rules
            else: # if position == ".", then end of pipe has been reached
                break
        else:
            pos1 = [0, -1]

    return answer


def get_input(location:str):
    '''Takes in a txt file; outputs a 2D list'''
    array = []

    file = open(location, 'r')

    n = 0
    for line in file:
        array.append([])
        for cha in line.strip():
            array[n].append(cha)
        n += 1

    file.close()

    return array


def start(location:str):
    answer = 0
    start_point = []
    file = get_input(location)

    start_point = find_start(file)


    return answer

#########
# Start #
#########
if __name__ == "__main__":
    print(start("day10input.txt"))


'''
Rules:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''