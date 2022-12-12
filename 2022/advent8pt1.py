

def open_file(file: str) -> list:
    '''Open a file in the 2022 folder \n
    Strips each line, then returns a list containing one item per line of text'''

    file = open(f"2022/{file}", "r")
    lines = []

    for line in file:
        lines.append(line.strip())
    file.close()

    return lines


def is_visible(tree: list, forest: list) -> bool:
    '''tests if a tree is visible\n
    Returns a boolean value: False if not visible, True otherwise'''
    
    tree_row, tree_col = tree
    tree = forest[tree_row][tree_col]
    tree_bool = [True, True, True, True]
    
    # check left
    for i in range(0, len(forest[tree_row][0:tree_col])):
        if tree <= forest[tree_row][i]:
            tree_bool[0] = False

    # check right    
    for i in range(len(forest[tree_row][0:tree_col]) + 1, len(forest[tree_row])):
        if tree <= forest[tree_row][i]:
            tree_bool[1] = False

    # check up
    for i in range(0, len(forest[0:tree_row])):
        if tree <= forest[i][tree_col]:
            tree_bool[2] = False

    #check down
    for i in range(len(forest[0:len(forest[tree_row:])]) + 1, len(forest[tree_row])):
        if tree <= forest[i][tree_col]:
            tree_bool[3] = False

    # if visible from edge, return True
    return any(tree_bool)


def count_visible_trees(forest: list):
    '''Count the number of visible trees\n
    Returns an Integer'''

    total = 0
    total += len(forest) * 2 # add trees along the top and bottom
    total += len(forest[0]) * 2 # add trees along the right and left
    total -= 4 # account for corners being counted twice

    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[i]) - 1):
            tree = [i, j]
            if is_visible(tree, forest):
                total += 1

    return total


def start():
    forest = open_file("advent8.txt")
    tree_count = count_visible_trees(forest)

    print(tree_count)


#########
# start #
#########

if __name__ == "__main__":
    start()

    # 593 = Too Low
    # 809 = Wrong
    # 896 = Wrong