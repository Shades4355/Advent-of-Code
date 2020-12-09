with open("2020/09_data.txt", 'r') as input_file:
    data = input_file.read()

with open("2020/09_test_data.txt", "r") as test_file:
    test_data = test_file.read()


# Part 1 #
def xmassHack(preamble: int, input_file: str):
    data = input_file.split('\n')
    num_data = [int(num) for num in data]
    n = preamble - 1

    for num in num_data[preamble:]:
        n += 1
        invalids = 0

        for j in num_data[n - preamble:n:1]:
            for k in num_data[n - preamble:n:1]:
                if j + k == num:
                    invalids = 0
                else:
                    invalids += 1
        if invalids == preamble**2:
            return num_data[n]

# Part 2 #


def hackXmass(preamble: int, input_file: str):
    data = input_file.split('\n')
    num_data = [int(i) for i in data]
    target = xmassHack(preamble, input_file)

    for i in num_data:
        n = num_data.index(i) + 1
        total = i
        tracker = [i, ]

        while n < len(num_data):
            total += num_data[n]
            tracker.append(num_data[n])
            if total == target:
                sorted_tracker = sorted(tracker)
                return sorted_tracker[0] + sorted_tracker[-1]
            n += 1


if __name__ == "__main__":
    # print("Part 1:", xmassHack(5, test_data))  # 127
    print("Part 1:", xmassHack(25, data))
    # print("Part 2:", hackXmass(5, test_data))  # 15 + 47 = 62
    print("Part 2:", hackXmass(25, data))
