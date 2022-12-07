from advent2pt1 import open_file
from advent5pt1 import parse_file, read_answer


def move_boxes(dictionary: dict) -> list:
    '''Move boxes from one stack to another'''

    inst_dict = dictionary["moves"]
    box_stack = dictionary["boxes"]

    for instructions in inst_dict:
        for how_many, pair in instructions.items():   
            # move boxes from one stack to another
            boxes = []
            start_pos, end_pos = pair

            for i in range(how_many):
                box = box_stack[str(start_pos)].pop()
                boxes.insert(0, box)
            
            for box in boxes:
                box_stack[str(end_pos)].append(box)

    return box_stack


def start() -> None:
    file = open_file("advent5.txt")
    dictionary = parse_file(file)
    moved_boxes = move_boxes(dictionary.copy())
    answer = read_answer(moved_boxes)

    print(answer)


#########
# start #
#########

if __name__ == "__main__":
    start()