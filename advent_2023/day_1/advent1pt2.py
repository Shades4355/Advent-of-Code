from advent1pt1 import get_cal_list, add_cal


def find_first_digit(calibration:list):
    '''Take in a line of alphanumerical digits
    return the first integer/number word'''
    cal_list = []
    current = 0

    for digit in calibration:
        cal_list.append(digit)

    while current < len(cal_list):
        num = None
        cur_cal = cal_list[current]
        num = get_num(cur_cal, cal_list, current)
        if num != None:
            return num
        current += 1


def find_last_digit(calibration: list):
    '''Take in a line of alphanumerical digits
    return the last integer/number word'''
    cal_list = []
    current = None

    for digit in calibration:
        cal_list.append(digit)
    
    current = len(cal_list) - 1

    while current >= 0:
        num = None
        cur_cal = cal_list[current]
        num = get_num(cur_cal, cal_list, current)
        if num != None:
            return num
        current -= 1


def check_word(current: int, cal_list:list, number:str):
    num_array = []
    location = 0

    for letter in number:
        num_array.append(letter)

    while location < len(num_array):
        if cal_list[current + location] != num_array[location]:
            return False
        location += 1
    return True

def get_num(cur_cal:str, cal_list:list, current:int):
    try:
        int_digit = int(cur_cal)
        return int_digit
    except:
        '''test for word'''
        if cur_cal.lower() == "o":
            # check for "one"
            if check_word(current, cal_list, "one"):
                return 1
        elif cur_cal.lower() == "t":
            # check for "two"
            if check_word(current, cal_list, "two"):
                return 2
            # check for "three"
            if check_word(current, cal_list, "three"):
                return 3
        elif cur_cal.lower() == "f":
            # check for "four"
            if check_word(current, cal_list, "four"):
                return 4
            # check for "five"
            if check_word(current, cal_list, "five"):
                return 5
        elif cur_cal.lower() == "s":
            # check for "six"
            if check_word(current, cal_list, "six"):
                return 6
            # check for "seven"
            if check_word(current, cal_list, "seven"):
                return 7
        elif cur_cal.lower() == "e":
            # check for "eight"
            if check_word(current, cal_list, "eight"):
                return 8
        elif cur_cal.lower() == "n":
            # check for "nine"
            if check_word(current, cal_list, "nine"):
                return 9
    return None


def start():
    cal_list = []
    first_digit = None
    last_digit = None

    cal = get_cal_list()

    for calibration in cal:
        first_digit = find_first_digit(calibration)
        last_digit = find_last_digit(calibration)
        int_cal = int(f"{first_digit}{last_digit}")
        cal_list.append(int_cal)
        first_digit = None
        last_digit = None

    print(add_cal(cal_list))


#########
# start #
#########
if __name__ == "__main__":
    start()
