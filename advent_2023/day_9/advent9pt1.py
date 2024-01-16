
def find_next_line(old_line:list):
    '''Takes in a list; outputs a list of the difference between each item as well as whether or not the list was all 0s'''
    answer = []
    zeros = 0

    for i in range(0, len(old_line)):
        if not old_line[i] == 0 and not i == len(old_line) - 1:
            new_num = old_line[i+1] - old_line[i]
            answer.append(new_num)
        elif old_line[i] == 0 and not i == len(old_line) - 1:
            new_num = old_line[i+1] - old_line[i]
            answer.append(new_num)
            zeros += 1

    if zeros == len(old_line) - 1:
        return [True, answer]

    return [False, answer]


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

    return answer


#########
# Start #
#########
print(start("day9input.txt"))