from advent9pt1 import get_input, parse_input, find_next_line


def find_prev_number(file:list):
    answer = 0
    temp_list = []

    for line in file:
        temp_list.append(line)

    for i in range(len(temp_list) - 1, 0, -1):
        new_num = temp_list[i - 1][0] - temp_list[i][0]
        temp_list[i - 1].insert(0, new_num)

    answer = temp_list[0][0]

    return answer


def start(location:str):
    answer = 0
    file = parse_input(get_input(location))

    for line in file:
        all_zeros = False
        new_list = []
        new_line = line

        # find all new lines
        while not all_zeros:
            new_list.append(new_line)
            all_zeros, new_line = find_next_line(new_line)

        # find first numbers, add them together
        answer += find_prev_number(file)

    return answer


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day9input.txt"))