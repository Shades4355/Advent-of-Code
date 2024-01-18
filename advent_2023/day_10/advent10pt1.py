
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
    file = get_input(location)

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