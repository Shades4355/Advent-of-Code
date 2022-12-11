
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

def is_visible(tree: list, forest: list) -> bool:
    tree_row, tree_col = tree
    tree = forest[tree_row, tree_col]
    
    # if not visible, return False

    # if visible from adjacentcy, contue checking
    # if visible from edge, return True
    return True


def find_tree(forest: list, current_tree: list=[0,0]):
    tree = [0, 0]

    if current_tree[0] <= 0:
        tree = [1, 1]
    elif current_tree[1] >= len(forest[current_tree[0]]) - 2:
        adv_row = current_tree[0] + 1
        col_start = 1
        tree[adv_row, col_start] # TODO: fix. Registering as a tuple
    else:
        tree = [
            current_tree[0], 
            current_tree[1] + 1
            ]

    return tree


def start():
    forest = open_file("advent8.txt")
    
    tree = find_tree(forest, [1, 98])
    print(tree)


    


#########
# start #
#########

if __name__ == "__main__":
    start()
