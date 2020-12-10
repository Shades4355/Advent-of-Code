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


if __name__ == "__main__":
    print("Part 1:", adaptors(data))
    # print("Part 2:", )
