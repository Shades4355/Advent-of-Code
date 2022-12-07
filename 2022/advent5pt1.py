from advent2pt1 import open_file


def parse_file(file: list) -> dict:
    '''Parses file into a dictionary'''

    dictionary = {
        "moves": [],
        "boxes": {}
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
            ### take top input and adds them to the dictionary
            words = []
            for i in range(1, 35, 4):
                letter = line[i]
                words.append(letter)
            
            row_num = 0
            for word in words:
                row_num += 1

                if word == "" or word == " ":
                    continue
                else:
                    letter = word
                    try:
                        dictionary["boxes"][str(row_num)].insert(0, letter)
                    except:
                        dictionary["boxes"][str(row_num)] = []
                        dictionary["boxes"][str(row_num)].insert(0, letter)

                if row_num > 9:
                    print('Error: "row_num" out of range!')
                    exit()
    
    if not validate_num(sorted(dictionary["boxes"]), 9):
        print("Error: Too Many Stacks Of Boxes!")
        exit()
    
    return dictionary


def move_boxes(dictionary: dict) -> list:
    inst_dict = dictionary["moves"]
    box_stack = dictionary["boxes"]

    for instructions in inst_dict:
        for key, pair in instructions.items():
            # move boxes from one stack to another
            boxes = []
            start_pos, end_pos = pair

            for i in range(key):
                try:
                    box = box_stack[str(start_pos)].pop(-1)
                except:
                    continue

                if box != "":
                    boxes.append(box)

            rev_boxes = reversed(boxes)
            for box in rev_boxes:
                box_stack[str(end_pos)].append(box)
            
    return box_stack


def read_answer(box_piles: object):
    answer = []

    for row, stack in box_piles.items():
        box = box_piles[row][-1]
        answer.append(box)
    return "".join(answer)

def validate_num(to_be_checked: list, max: int) -> bool:
    if len(to_be_checked) > max:
        return False
    return True

def start() -> None:
    file = open_file("advent5.txt")
    dictionary = parse_file(file)
    moved_boxes = move_boxes(dictionary)
    answer = read_answer(moved_boxes)

    print(answer)


#########
# start #
#########
if __name__ == "__main__":
    start()

    # not right: PWHWFGPZS