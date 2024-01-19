

def advance_pos(out_direction:str, pos:list):
    i, j = pos

    if out_direction == "n":
        return [i - 1, j]
    elif out_direction == "s":
        return [i + 1, j]
    elif out_direction == "e":
        return [i, j + 1]
    elif out_direction == "w":
        return [i, j - 1]
    else:
        raise Exception("invalid direction:", out_direction)


def find_start(file:list):
    '''take in a 2D file; outputs the location of "S"'''
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j] == "S":
                return [i, j]

    raise Exception("No start point found")


def follow_pipes(file:list, start_point:list):
    '''takes in a list of pipes and a start position; return how many steps away the farthest point is'''
    i, j = start_point
    answer = 0
    direction = {}
    direction["pos1"] = []
    direction["in1"] = ""
    direction["out1"] = ""
    direction["pos2"] = []
    direction["in2"] = ""
    direction["out2"] = ""

    # find starting direction 1
    if i - 1 >= 0 and not file[i - 1][j] == ".":
            direction["pos1"] = [i - 1, j]
            direction["in1"] = "s"
    elif j + 1 < len(file[0]) and not file[i][j + 1] == ".":
            direction["pos1"] = [i, j + 1]
            direction["in1"] = "w"
    elif i + 1 < len(file) and not file[i + 1][j] == ".":
            direction["pos1"] = [i + 1, j]
            direction["in1"] = "n"
    elif j - 1 >= 0 and not file[i][j - 1] == ".":
            direction["pos1"] = [i, j - 1]
            direction["in1"] = "e"
    else:
        raise Exception("No pipes found")

    # find starting direction 2
    if j - 1 >= 0 and not file[i][j - 1] == ".":
            direction["pos2"] = [i, j - 1]
            direction["in2"] = "e"
    elif i + 1 < len(file) and not file[i + 1][j] == ".":
            direction["pos2"] = [i + 1, j]
            direction["in2"] = "n"
    elif j + 1 > len(file[0]) and not file[i][j + 1] == ".":
            direction["pos2"] = [i, j + 1]
            direction["in2"] = "w"
    elif i - 1 >= 0 and not file[i - 1][j] == ".":
            direction["pos2"] = [i - 1, j]
            direction["in2"] = "s"
    else:
        raise Exception("No pipes found")

    answer += 1

    while True:
        if direction["pos1"] == direction["pos2"]:
            return answer

        # if pos1 does not == pos2, have each take one step
        direction["out1"] = take_step(file, direction["in1"], direction["pos1"])
        direction["out2"] = take_step(file, direction["in2"], direction["pos2"])

        # advance pos1 and pos2
        direction["pos1"] = advance_pos(direction["out1"], direction["pos1"])
        direction["pos2"] = advance_pos(direction["out2"], direction["pos2"])

        # update "in" position
        direction["in1"] = update_direction(direction["out1"])
        direction["in2"] = update_direction(direction["out2"])

        # advance answer 1 step
        answer += 1


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


def take_step(file:list, in_direction:str, pos:list):
    i, j = pos
    position = file[i][j]

    if position == "|":
        if in_direction == "s":
            return "n"
        elif in_direction == "n":
            return "s"
    elif position == "-":
        if in_direction == "e":
            return "w"
        elif in_direction == "w":
            return "e"
    elif position == "L":
        if in_direction == "n":
            return "e"
        elif in_direction == "e":
            return "n"
    elif position == "J":
        if in_direction == "n":
            return "w"
        elif in_direction == "w":
            return "n"
    elif position == "7":
        if in_direction == "w":
            return "s"
        elif in_direction == "s":
            return "w"
    elif position == "F":
        if in_direction == "e":
            return "s"
        elif in_direction == "s":
            return "e"
 
    raise Exception("Loop broken! Position:", position, "| in direction:", in_direction)
    
    
def update_direction(out_direction:str):
    '''takes in an old "out direction"; returns a new "in direction"'''
    if out_direction == "n":
        return "s"
    elif out_direction == "s":
        return "n"
    elif out_direction == "e":
        return "w"
    elif out_direction == "w":
        return "e"
    else:
        raise Exception("Incorrect direction:", out_direction)

def start(location:str):
    answer = 0
    start_point = []
    file = get_input(location)

    start_point = find_start(file)
    answer += follow_pipes(file, start_point)

    return answer

#########
# Start #
#########
if __name__ == "__main__":
    print(start("day10input.txt"))
