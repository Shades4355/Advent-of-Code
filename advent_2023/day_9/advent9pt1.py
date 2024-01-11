
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