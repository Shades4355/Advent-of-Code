from advent2pt1 import open_file


def parse_file(file: list) -> dict:
    '''Parses file into a dictionary'''

    dictionary = {
        "moves": [],
        "boxes": []
        }
    for line in file:
        if line.startswith("move"):
            # Takes input starting with "move" and outputs a
            # dictionary of {how many: [from here, to here]}
            words = line.split(" ")
            position = 0
            key = None
            start_pos = None
            end_pos = None

            for word in words:
                try:
                    int_word = int(word)
                    if position == 0:
                        key = int_word
                        position = 1
                    elif position == 1:
                        start_pos = int_word
                        position = 2
                    elif position == 2:
                        end_pos = int_word
                except:
                    continue
            pos = {key: [start_pos, end_pos]}
            dictionary["moves"].append(pos)
        elif line.startswith("["):
            ### take top input and outputs 9 arrays
            words = line.split(" ")
            row_num = 0
            array_of_boxes = [[], [], [], [], [], [], [], [], []]
            for word in words:
                try:
                    end_num_index = word.index("]")
                    letter = word[1:end_num_index].strip()
                    array_of_boxes[row_num].append(letter) # TODO: fix this to end up with [letter][row_number]
                    row_num += 1
                except:
                    row_num += 1
                    continue
            print(array_of_boxes)
            dictionary["boxes"].append(array_of_boxes)

    return dictionary


def move_boxes(dictionary: dict) -> list:
    inst_dict = dictionary["moves"]
    box_stack = dictionary["boxes"]
    # for box_pile in box_stack:
    #     print(box_pile)
    for instructions in inst_dict:
        for key, pair in instructions.items():
            # move boxes from one stack to another
            boxes = []
            start_pos, end_pos = pair
            for i in range(key):
                n = i
                loop = True
                box = ""
                while loop:
                    try:
                        box = box_stack[start_pos][n].pop(0) # TODO: fix
                        print("Box:", box) # TODO: delete
                    except IndexError:
                        loop = False
                    except:
                        n += 1
                    else:
                        loop = False
                if box != "":
                    boxes.append(box)
                print("Boxes:", boxes) # TODO: delete
                
    
    return box_stack


def start() -> None:
    file = open_file("advent5.txt")
    dictionary = parse_file(file)
    moved_boxes = move_boxes(dictionary)


#########
# start #
#########
if __name__ == "__main__":
    start()
