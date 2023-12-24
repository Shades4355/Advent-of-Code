from advent3pt1 import get_input, two_d_ify, test_num


def find_gear(two_d_list:list):
    '''Takes in a 2D list and outputs the total of the gear ratios'''
    max_rows = len(two_d_list)
    max_cols = len(two_d_list[0])
    gear_ratios = 0

    # check each cha to see if it's an '*'
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
    max_row = len(two_d_list)
    max_col = len(two_d_list[0])
    r = -1

    while r < 2:
        c = -1

        while c < 2:
            if 0 <= row + r < max_row and 0 <= col + c < max_col and test_num(two_d_list[row + r][col + c]):
                # If the above is a number, iterate through it to find where it starts and how long it is
                start_offset, num_length = find_num(two_d_list, row + r, col + c)

                str_num = ""
                for i in range(0, num_length):
                    # create a str of the number
                    str_num += str(two_d_list[row + r][col + c + start_offset + i])

                if test_num(str_num): # test that the str was created correctly
                    total *= int(str_num) # multiply both gear ratios for this one gear together
                else:
                    raise Exception("test_num failed unexpectedly\nERROR:", str_num)

                # set 'c' to the cha after the number, so we don't accidentally read the same number multiple times
                c += start_offset + num_length
            else:
                c += 1
        r += 1

    # return total gear ratio for this one gear
    return total


def find_num(two_d_list:list, row:int, col:int):
    '''Takes in a 2D list and a position ([row][col]) of a number;
    outputs the offset of the beginning of the number, and the number's length'''
    left_looping = True
    begin_offset = -1
    max_col = len(two_d_list[0])

    # look for the beginning of the number
    while left_looping:
        if (col + begin_offset) >= 0 and test_num(two_d_list[row][col + begin_offset]):
            begin_offset -= 1
        else:
            left_looping = False
            begin_offset += 1

    # Look for the end of the number
    end_offset = 1
    right_looping = True
    while right_looping:
        if (col + end_offset) < max_col and test_num(two_d_list[row][col + end_offset]):
            end_offset += 1
        else:
            right_looping = False

    num_length = end_offset - begin_offset

    # return the position of the beginning of the number and the number's length
    return [begin_offset, num_length]


def test_gear(two_d_list:list, row:int, col:int):
    '''Takes in a 2D list and the position of a gear;
    returns True if exactly 2 numbers are found adjacent/diagonal
    to it, otherwise returns False'''
    max_col = len(two_d_list[0])
    check = 0
    r = -1

    while r < 2:
        c = -1
        while c < 2:
            if 0 <= row + r < len(two_d_list) and 0 <= col + c < max_col and test_num(two_d_list[row + r][col + c]):
                start_offset, num_length = find_num(two_d_list, row + r, col + c)
                check += 1
                if start_offset + num_length <= 0:
                    c += 1
                else:
                    c += start_offset + num_length
            else:
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

