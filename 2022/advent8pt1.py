
def open_file(file: str) -> list:
    '''Open a file in the 2022 folder \n
    Returns a list containing one item per line of text'''

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
    '''tests if a tree is visible\n
    Returns a boolean value: True if visible, False otherwise'''

    tree_row, tree_col = tree
    tree = forest[tree_row][tree_col]
    
    # if not visible, return False
    # if visible from adjacentcy, contue checking

    # check left
    for i in range(0, len(forest[tree_row][0:tree_col])):
        if tree < forest[tree_row][i]:
            return False

    # check right    
    for i in range(len(forest[tree_row][0:tree_col]) + 1, len(forest[tree_row])):
        if tree < forest[tree_row][i]:
            return False
    
    # check up
    for i in range(0, len(forest[0:tree_row])):
        if tree < forest[i][tree_col]:
            return False

    #check down
    for i in range(len(forest[0:len(forest[tree_row + 1:])]), len(forest[tree_row])):
        if tree < forest[i][tree_col]:
            return False

    # if visible from edge, return True
    return True


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
    # 896 = Wrong