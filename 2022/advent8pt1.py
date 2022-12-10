
def open_file(file: str) -> list:
    '''Open a file in the 2022 folder \n
    If X is greater than 0, returns a list of first and X+1 values\n
    Otherwise, returns a list containing one item per line of text'''
    file = open(f"2022/{file}", "r")
    lines = []

    for line in file:
        lines.append(line.strip())
    file.close()

    return lines


### A tree is visible if all of the other trees between it and an edge of the grid are shorter than it
### cardinal directions only


### how many trees are *visible* from outside the grid?

def is_visible(tree: int, forest: list) -> bool:
    # if not visible, return False
    # if visible from adjacentcy, contue checking
    # if visible from edge, return True
    return True


def start():
    forest = open_file("advent8.txt")
    
    print(forest)

#########
# start #
#########

if __name__ == "__main__":
    start()
