from advent3pt1 import get_input, two_d_ify, find_max_column, test_num


def find_gear(two_d_list:list):
    max_rows = len(two_d_list)
    row = 0
    max_cols = find_max_column(two_d_list)
    gear_ratios = 0

    while row < max_rows:
        col = 0
        while col < max_cols:
            if two_d_list[row][col] == "*":
                if test_gear(two_d_list, row, col):
                    gear_ratios += find_gear_ratio(two_d_list, row, col)
            col += 1
        row += 1

    return gear_ratios


def find_num(two_d_list:list, row:int, col:int):
    left_looping = True
    begin = -1
    end = 1
    max_col = find_max_column(two_d_list)

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

    return [col + begin, num_length]


def test_gear(two_d_list:list, row:int, col:int):
    check = 0
    r = -1

    while r < 2:
        c = -1
        while c < 2:
            try:
                if test_num(two_d_list[row+r][col+c]):
                    num_start, num_length = find_num(two_d_list, row+r, col+c)
                    check += 1
                    c = num_start + num_length
            except:
                continue
            c += 1
        r += 1

    if check == 2:
        print("True") # TODO: delete
        return True
    return False


def find_gear_ratio(two_d_list:list, row:int, col:int):
    total = 1    
    r = -1
    str_num = ""

    while r < 2:
        c = -1
        while c < 2:
            try:
                if test_num(two_d_list[row+r][col+c]):
                    num_start, num_length = find_num(two_d_list, row+r, col+c)
                    c = num_start + num_length
                    for i in range(0, num_length):
                        str_num += f"{two_d_list[row+r][num_start + i]}"
                    print("number:", str_num) # TODO: delete
                    if test_num(str_num):
                        total *= int(str_num)
                    str_num = ""
            except:
                continue
            c += 1
        r += 1

    return total


def start():
    engine_2d_list = []

    engine_2d_list = two_d_ify(get_input("advent3input.txt"))
    

    print(find_gear(engine_2d_list))


#########
# start #
#########
if __name__ == "__main__":
    start()

# 65320597 = too low