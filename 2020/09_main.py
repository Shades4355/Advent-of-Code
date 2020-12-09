# with open("2020/09_data.txt", 'r') as file:
#     data = file.read()

with open("2020/09_test_data.txt", "r") as test_file:  #
    test_data = test_file.read()                            #


def xmassHack(preamble: int, file: str):
    data = file.split('\n')

    # is data[i] the sum of 2 values in range(i - preamble, i)?
    # if no
    return data[i]


if __name__ == "__main__":
    print("part 1:", xmassHack(5, test_data))
