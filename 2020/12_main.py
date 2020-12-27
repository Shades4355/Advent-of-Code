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

with open("2020/12_custom_test_data.txt", "r") as custom_test_file:
    custom_test_data = custom_test_file.read().split('\n')

custom_processed_test_data = list()
for i in custom_test_data:
    direction = i[0]
    distance = int(i[1:])
    custom_processed_test_data.append([direction, distance])

# Part 1 #


def manhattanDistance(directions: list):
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

# Part 2 #


def waypointShift(directions: list, s1: int, s2: int):
    heading = ["N", "E", "S", "W"]
    heading_variable = 1
    current_heading = heading[heading_variable]

    heading_1 = s1
    heading_2 = s2
    ship = [0, 0]
    waypoint = [[heading[heading_variable], heading_1],  # backwards?
                [heading[heading_variable - 1], heading_2]]

    for direction, distance in directions:
        if direction == "F":
            # move the ship forawrd distance times
            # moving (waypoint[0][1], waypoint[1][1]) units each time
            for _ in range(distance):
                if waypoint[0][0] == "N" or waypoint[0][0] == "S":
                    ship[0] += waypoint[0][1]
                elif waypoint[0][0] == "E" or waypoint[0][0] == "W":
                    ship[1] += waypoint[0][1]

                if waypoint[1][0] == "N" or waypoint[1][0] == "S":
                    ship[0] += waypoint[1][1]
                elif waypoint[1][0] == "E" or waypoint[1][0] == "W":
                    ship[1] += waypoint[1][1]

        elif direction == "R":
            # rotate waypoint clockwise around the ship (distance) degrees
            change_in_direction = distance // 90
            for _ in range(change_in_direction):
                heading_variable += 1

                # test for wrap around
                if heading_variable >= len(heading):
                    heading_variable -= len(heading)

                if waypoint[0][0] == "N" or waypoint[0][0] == "S":
                    waypoint[0] = [heading[heading_variable], waypoint[0][1]]

                elif waypoint[0][0] == "E" or waypoint[0][0] == "W":
                    waypoint[0] = [heading[heading_variable], -waypoint[0][1]]

                heading_variable_2 = heading_variable - 1
                # test for wrap around
                if heading_variable_2 < 0:
                    heading_variable_2 += len(heading)

                if waypoint[1][0] == "N" or waypoint[1][0] == "S":
                    waypoint[1] = [heading[heading_variable_2], waypoint[1][1]]
                elif waypoint[1][0] == "E" or waypoint[1][0] == "W":
                    waypoint[1] = [
                        heading[heading_variable_2], -waypoint[1][1]]

        elif direction == "L":
            # rotate waypoint counter-clockwise around the
            # ship (distance) degrees

            change_in_direction = distance // 90
            for _ in range(change_in_direction):
                heading_variable -= 1

                # check for wrap around
                if heading_variable < 0:
                    heading_variable += len(heading)

                if waypoint[0][0] == "E" or waypoint[0][0] == "W":
                    waypoint[0] = [heading[heading_variable], waypoint[0][1]]
                elif waypoint[0][0] == "N" or waypoint[0][0] == "S":
                    waypoint[0] = [heading[heading_variable], -waypoint[0][1]]

                heading_variable_2 = heading_variable - 1
                # test for wrap around
                if heading_variable_2 < 0:
                    heading_variable_2 += len(heading)

                if waypoint[1][0] == "N" or waypoint[1][0] == "S":
                    waypoint[1] = [
                        heading[heading_variable_2], -waypoint[1][1]]
                elif waypoint[1][0] == "E" or waypoint[1][0] == "W":
                    waypoint[1] = [
                        heading[heading_variable_2], waypoint[1][1]]

        if direction == "N":
            # move waypoint North
            if waypoint[0][0] == "N" or waypoint[0][0] == "S":
                waypoint[0][1] += distance
            elif waypoint[1][0] == "N" or waypoint[1][0] == "S":
                waypoint[1][1] += distance
        elif direction == "S":
            # move waypoint South
            if waypoint[0][0] == "N" or waypoint[0][0] == "S":
                waypoint[0][1] -= distance
            elif waypoint[1][0] == "N" or waypoint[1][0] == "S":
                waypoint[1][1] -= distance
        elif direction == "E":
            # move waypoint East
            if waypoint[0][0] == "E" or waypoint[0][0] == "W":
                waypoint[0][1] += distance
            elif waypoint[1][0] == "E" or waypoint[1][0] == "W":
                waypoint[1][1] += distance
        elif direction == "W":
            # move waypoint West
            if waypoint[0][0] == "E" or waypoint[0][0] == "W":
                waypoint[0][1] -= distance
            elif waypoint[1][0] == "E" or waypoint[1][0] == "W":
                waypoint[1][1] -= distance

    manhattan_distance = abs(ship[0]) + abs(ship[1])
    return manhattan_distance


if __name__ == "__main__":
    # print("Part 1, test:", manhattanDistance(processed_test_data)) # 25
    print("Part 1:", manhattanDistance(processed_data))
    # print("Part 2, test:", waypointShift(processed_test_data, 10, 1))  # 286
    # print("Part 2, test:", waypointShift(custom_processed_test_data, 10, 1))
    print("Part 2:", waypointShift(processed_data, 10, 1))
