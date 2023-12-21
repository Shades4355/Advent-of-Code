
def get_cal_list():
    '''Convert text file of raw data into a list'''
    file = open("advent1input.txt", "r")
    cal = []

    for line in file:
        cal.append(line)
    file.close
    return cal


def find_first_digit(calibration):
    '''Take in a line of alphanumerical digits
    return the first integer'''
    for digit in calibration:
        try:
            int_digit = int(digit)
            return int_digit
        except:
            continue


def find_last_digit(calibration):
    '''Take in a line of alphanumerical digits
    return the first integer'''
    cal_list = []

    for digit in calibration:
        cal_list.append(digit)
    
    cal_list.reverse()
    for digit in cal_list:
        try:
            int_digit = int(digit)
            return int_digit
        except:
            continue

    
def add_cal(cal_list):
    total = 0

    for number in cal_list:
        total += number

    return total

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
