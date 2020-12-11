with open("2020/10_data.txt", 'r') as input_file:
    data = input_file.read()

with open("2020/10_test_data.txt", "r") as test_file:
    test_data = test_file.read()


# Part 1 #
def adaptors(file: str):
    parsed_data = file.split("\n")
    num_data = [int(num) for num in parsed_data]
    num_data.append(0)
    num_data.sort()
    n = 0
    ones = 0
    threes = 1

    while n < len(num_data)-1:
        if num_data[n+1] - num_data[n] == 1:
            ones += 1
        elif num_data[n+1] - num_data[n] == 3:
            threes += 1
        n += 1

    return ones * threes

# part 2 #


def adaptorCombos(file: str):
    parsed_data = file.split("\n")
    num_data = [int(num) for num in parsed_data]
    num_data.append(0)
    num_data.sort()

    phone = num_data[-1] + 3
    combos = 0
    n = 1
    list_of_combo_lists = []
    position = 1

    while n < len(num_data):
        # clear list
        combo_list = list()

        # has to start at num_data[0]
        combo_list.append(num_data[0])

        # has to jump by 3 or less
        if num_data[n] - combo_list[-1] <= 3:
            combo_list.append(num_data[n])
        else:
            return combos

        # incrementally adds numbers to combo_list,
        # starting at num_data[n + 1]
        num = n + 1
        while num < len(num_data) - 1:
            print("num:", num)
            # has to jump by 3 or less
            if num_data[num] - combo_list[-1] <= 3:
                x = num_data[num]
                combo_list.append(x)
                print(combo_list)
            else:  # invalid list; restart
                break

            num += 1

        # has to end at phone
        if num_data[num] - phone <= 3:
            combos += 1
            combo_list = list()
        else:  # invalid list
            combo_list = list()

        n += 1

    return combos


if __name__ == "__main__":
    # print("Part 1:", adaptors(data))
    print("Part 2:", adaptorCombos(test_data))  # 19208
