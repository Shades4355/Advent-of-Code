with open("2020/12_data.txt", "r") as input_file:
    data = input_file.read().split('\n')

processed_data = list()
for i in data:
    direction = i[0]
    distance = int(i[1:])
    processed_data.append([direction, distance])


with open("2020/12_test_data.txt", "r") as test_file:
    test_data = test_file.read().split('\n')

processed_test_data = list()
for i in test_data:
    direction = i[0]
    distance = int(i[1:])
    processed_test_data.append([direction, distance])


# Part 1 #
def manhattanDistance(directions):
    heading = ["N", "E", "S", "W"]
    y = 1
    current_heading = heading[y]
    north_south = 0
    east_west = 0

    for direction, distance in directions:

        if direction == "F":
            direction = current_heading

        if direction == "N":
            north_south += distance
        elif direction == "S":
            north_south -= distance
        elif direction == "E":
            east_west += distance
        elif direction == "W":
            east_west -= distance

        elif direction == "R":
            x = distance // 90
            y += x
            if y >= len(heading):
                y -= len(heading)
            current_heading = heading[y]
        elif direction == "L":
            x = distance // 90
            y -= x
            if y < 0:
                y += len(heading)
            current_heading = heading[y]

    return abs(north_south) + abs(east_west)


if __name__ == "__main__":
    # print("Part 1, test:", manhattanDistance(processed_test_data)) # 25
    print("Part 1:", manhattanDistance(processed_data))
    pass
