from advent3pt1 import get_input, two_d_ify, find_max_column, test_num


def find_gear(two_d_list:list):
    '''Takes in a 2D list and outputs the total of the gear ratios'''
    max_rows = len(two_d_list)
    max_cols = find_max_column(two_d_list)
    gear_ratios = 0

    # check each cha to see if it's an *
    for row in range(0, max_rows):
        for col in range(0, max_cols):
            if two_d_list[row][col] == "*":
                # if an * is found, test how many numbers are around it
                if test_gear(two_d_list, row, col):
                    # if exactly 2 numbers are found, add gear ratio to running gear_ratios
                    gear_ratios += find_gear_ratio(two_d_list, row, col)

    return gear_ratios



def find_gear_ratio(two_d_list:list, row:int, col:int):
    '''Takes in a 2D list with the row and column of a gear and outputs that gear's gear ratio'''
    total = 1    
    max_col = find_max_column(two_d_list)
    max_row = len(two_d_list)
    r = -1
    str_num = ""

    while r < 2: # Unit Test fails when these While loops is replaced with a For loops
        c = -1
        while c < 2:
            if 0 <= row + r < max_row and 0 <= col + c < max_col:
                # Test if two_d_list[row + r][col + c] is a number; returns True or False
                if test_num(two_d_list[row + r][col + c]):
                    # If the above is a number, iterate through it to find where it starts and how long it is
                    num_start, num_length = find_num(two_d_list, row + r, col + c)
                    # set 'c' to the cha after the number, so we don't accidentally read the same number multiple times
                    c = num_start + num_length
                    for i in range(0, num_length):
                        # create a str of the number
                        str_num += f"{two_d_list[row + r][num_start + i]}"
                    if test_num(str_num): # test that the str was created correctly
                        total *= int(str_num) # multiply all gear ratios for this one gear together
                    else:
                        raise Exception("test_num failed unexpectedly")
                    str_num = ""
            c += 1
        r += 1

    # return total gear ratio for this one gear
    return total


def find_num(two_d_list:list, row:int, col:int):
    '''Takes in a 2D list and a position ([row][col]) of a number;
    outputs the position of the beginning of the number, and the number's length'''
    left_looping = True
    begin = -1
    end = 1
    max_col = find_max_column(two_d_list)

    # look for the beginning of the number
    while left_looping:
        if (col + begin) >= 0:
            if test_num(two_d_list[row][col + begin]):
                begin -= 1
            else:
                left_looping = False
                begin += 1
        else:
            left_looping = False
            begin += 1

    # Look for the end of the number
    right_looping = True
    while right_looping:
        if (col + end) < max_col:
            if test_num(two_d_list[row][col + end]):
                end += 1
            else:
                right_looping = False
                end -= 1
        else:
            right_looping = False
            end -= 1

    num_length = end - begin + 1

    # return the position of the beginning of the number and the number's length
    return [col + begin, num_length]


def test_gear(two_d_list:list, row:int, col:int):
    '''Takes in a 2D list and the position of a gear; 
    returns True if exactly 2 numbers are found adjacent/diagonal to it, otherwise returns False'''
    max_col = find_max_column(two_d_list)
    check = 0
    r = -1

    while r < 2:
        c = -1
        while c < 2:
            if 0 <= row + r < len(two_d_list) and 0 <= col + c < max_col:
                if test_num(two_d_list[row + r][col + c]):
                    num_start, num_length = find_num(two_d_list, row + r, col + c)
                    check += 1
                    c = num_start + num_length
            c += 1
        r += 1

    if check == 2:
        return True
    return False


def start(file:str):
    '''Starts the program; returns the final gear ratio total'''
    engine_2d_list = []
    engine_2d_list = two_d_ify(get_input(file)) # generates the 2D list
    
    # uses return instead of print so as to be testable
    return find_gear(engine_2d_list)


#########
# start #
#########
if __name__ == "__main__":
    print(start("advent3input.txt"))

