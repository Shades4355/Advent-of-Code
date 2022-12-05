from advent2pt1 import open_file


def parse_file(file: list) -> dict:
    '''Parses file into a dictionary'''

    dictionary = {"moves":[]}
    for line in file:
        if line.startswith("move"):
            ### Takes input starting with "move" and outputs a dictionary of {how many: [from here, to here]}
            words = line.split(" ")
            posisition = 0
            key = None
            start_pos = None
            end_pos = None

            for word in words:
                try:
                    int_word = int(word)
                    if posisition == 0:
                        key = int_word
                        posisition = 1
                    elif posisition == 1:
                        start_pos = int_word
                        posisition = 2
                    elif posisition == 2:
                        end_pos = int_word
                except:
                    continue
            pos = {key: [start_pos, end_pos]}
            dictionary["moves"].append(pos)
        elif line.startswith("["):
            ### take top input and outputs X arrays
            continue
    return dictionary


def start() -> None:
    file = open_file("advent5.txt")
    dictionary = parse_file(file)
    print(dictionary)


#########
# start #
#########
if __name__ == "__main__":
    start()