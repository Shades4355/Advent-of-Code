def get_input(location:str):
    array = []
    file = open(location, "r")

    for line in file:
        array.append(line.strip())
    
    return array


def find_max_column(list:list):
    max_col = 0

    for i in range(0, len(list)):
        if max_col < len(list[i]):
            max_col = len(list[i])
    
    return max_col


def two_d_ify(engine_list:list):
    max_row = len(engine_list)
    max_col = find_max_column(engine_list)

    engine_array = [['.'] * max_col for i in range(max_row)]

    row = 0
    while row < max_row:
        col = 0
        while col < max_col:
            engine_array[row][col] = engine_list[row][col]
            col += 1
        row += 1

    return engine_array


def test_num(digit:str):
    '''Test if a digit is an Integer'''
    try:
        int(digit)
        return True
    except:
        return False
    

def test_adjacency(two_d_list:list, col_start: int, col_end: int, row:int):
    '''Test if a non-period symbol is next to, or diagonal to, a number'''
    
    for r in range(-1, 2):
        for c in range(-1, col_end-col_start+1):
            try:
                if not test_num(two_d_list[row+r][col_start+c]):
                    if not str(two_d_list[row+r][col_start+c]) == ".":
                        return True
            except:
                continue

    return False


def find_number(two_d_list:list):
    '''test if a number is valid; if so, add it to a running total; returns the total'''
    total = 0
    max_rows = len(two_d_list)
    rows = 0
    max_cols = find_max_column(two_d_list)

    while rows < max_rows:
        cols = 0
        while cols < max_cols:
            str_num = ""
            if test_num(two_d_list[rows][cols]):
                loop = True
                i = 1
                while loop:
                    try:
                        if test_num(two_d_list[rows][cols+i]):
                            i += 1
                        else:
                            loop = False
                    except:
                        loop = False
                for j in range(0, i):
                    str_num += f"{two_d_list[rows][cols+j]}"

                if test_adjacency(two_d_list, cols, cols+i, rows):
                    if test_num(str_num):
                        total += int(str_num)
                    else:
                        raise Exception("str_num invalid")
                cols += i
            cols += 1
        rows += 1

    return total


def start():
    total = 0
    engine_2d_list = []

    engine_2d_list = two_d_ify(get_input("advent3input.txt"))
    total = find_number(engine_2d_list)

    print(total)


#########
# start #
#########
if __name__ == "__main__":
    start()


# 3594 is too low
