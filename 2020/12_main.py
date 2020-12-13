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
    heading_variable = 1
    current_heading = heading[heading_variable]
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
            change_in_direction = distance // 90
            heading_variable += change_in_direction
            if heading_variable >= len(heading):
                heading_variable -= len(heading)
            current_heading = heading[heading_variable]
        elif direction == "L":
            change_in_direction = distance // 90
            heading_variable -= change_in_direction
            if heading_variable < 0:
                heading_variable += len(heading)
            current_heading = heading[heading_variable]

    return abs(north_south) + abs(east_west)


if __name__ == "__main__":
    # print("Part 1, test:", manhattanDistance(processed_test_data)) # 25
    print("Part 1:", manhattanDistance(processed_data))
    pass
