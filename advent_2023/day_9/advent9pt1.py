
def find_next_line(old_line:list):
    '''Takes in a list; outputs a list of the difference between each item as well as whether or not the list was all 0s'''
    answer = []
    zeros = 0

    for i in range(0, len(old_line) - 1):
        if not old_line[i] == 0:
            new_num = old_line[i+1] - old_line[i]
            answer.append(new_num)
        elif old_line[i] == 0:
            new_num = old_line[i+1] - old_line[i]
            answer.append(new_num)
            zeros += 1

    if zeros == len(old_line) - 1:
        return [True, answer]

    return [False, answer]


def find_number(file:list):
    answer = 0
    temp_list = []

    for line in file:
        temp_list.append(line)

    for i in range(len(temp_list) - 1, 0, -1):
        new_num = temp_list[i][-1] + temp_list[i - 1][-1]
        temp_list[i - 1].append(new_num)

    answer = temp_list[0][-1]

    return answer


def get_input(location:str):
    '''parse txt file into a list'''
    output_file = []

    file = open(location, "r")

    for line in file:
        output_file.append(line.strip())

    file.close()

    return output_file


def parse_input(file:list):
    answer = []
    str_answer = []

    for i in range(0, len(file)):
        answer.append([])
        answer[i] = []
        str_answer.append([])
        str_answer[i] = file[i].split()
        for num in str_answer[i]:
            answer[i].append(int(num))

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

        # find last numbers, add them together
        answer += find_number(new_list)

    return answer


#########
# Start #
#########
if __name__ == "__main__":
    print(start("day9input.txt"))