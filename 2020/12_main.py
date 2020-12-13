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
    heading_variable = 0
    current_heading = heading[heading_variable]

    heading_1 = s1
    heading_2 = s2
    ship = [0, 0]
    waypoint = [[heading[heading_variable], heading_1],
                [heading[heading_variable + 1], heading_2]]
    waypoint1 = waypoint[0]
    waypoint2 = waypoint[1]

    manhattan_distance = 0

    for direction, distance in directions:
        if direction == "F":
            # move towards waypoint (distance) times
            pass
        elif direction == "R":
            # rotate waypoint clockwise around the ship (distance) degrees
            change_in_direction = distance // 90

            for _ in range(change_in_direction):

                heading_variable += 1

                if heading_variable >= len(heading):
                    heading_variable -= len(heading)
                if waypoint1[0] == "N" or waypoint1[0] == "S":
                    waypoint1 = [heading[heading_variable], waypoint1[1]]
                elif waypoint1[0] == "E" or waypoint1[0] == "W":
                    waypoint1 = [heading[heading_variable], -waypoint1[1]]

                if heading_variable + 1 >= len(heading):
                    heading_variable -= len(heading) - 1
                if waypoint2[0] == "N" or waypoint2[0] == "S":
                    waypoint2 = [heading[heading_variable + 1], waypoint2[1]]
                elif waypoint2[0] == "E" or waypoint2[0] == "W":
                    waypoint2 = [heading[heading_variable + 1], -waypoint2[1]]

        elif direction == "L":
            # rotate waypoint counter-clockwise around the
            # ship (distance) degrees
            change_in_direction = distance // 90

            for _ in range(change_in_direction):

                heading_variable -= 1

                if heading_variable < 0:
                    heading_variable += len(heading)
                if waypoint1[0] == "E" or waypoint1[0] == "W":
                    waypoint1 = [heading[heading_variable], waypoint1[1]]
                elif waypoint1[0] == "N" or waypoint1[0] == "S":
                    waypoint1 = [heading[heading_variable], -waypoint1[1]]

                if heading_variable + 1 >= len(heading):
                    heading_variable -= len(heading) - 1
                if waypoint2[0] == "E" or waypoint2[0] == "W":
                    waypoint2 = [heading[heading_variable + 1], waypoint2[1]]
                elif waypoint2[0] == "N" or waypoint2[0] == "S":
                    waypoint2 = [heading[heading_variable + 1], -waypoint2[1]]

        if direction == "N":
            # move waypoint North
            if waypoint1[0] == "N" or waypoint1[0] == "S":
                waypoint1[1] += distance
            elif waypoint2[0] == "N" or waypoint2[0] == "S":
                waypoint2[1] += distance
        elif direction == "S":
            # move waypoint South
            if waypoint1[0] == "N" or waypoint1[0] == "S":
                waypoint1[1] -= distance
            elif waypoint2[0] == "N" or waypoint2[0] == "S":
                waypoint2[1] -= distance
        elif direction == "E":
            # move waypoint East
            if waypoint1[0] == "E" or waypoint1[0] == "W":
                waypoint1[1] += distance
            elif waypoint2[0] == "E" or waypoint2[0] == "W":
                waypoint2[1] += distance
        elif direction == "W":
            # move waypoint West
            if waypoint1[0] == "E" or waypoint1[0] == "W":
                waypoint1[1] -= distance
            elif waypoint2[0] == "E" or waypoint2[0] == "W":
                waypoint2[1] -= distance

        elif direction == "F":
            # move the ship forawrd distance times
            # moving waypoint1[1], waypoint2[1] units each time
            for _ in range(distance):
                if waypoint1[0] == "N" or waypoint1[0] == "S":
                    ship[0] += waypoint1[1]
                elif waypoint1[0] == "E" or waypoint1[0] == "W":
                    ship[1] += waypoint1[1]

                if waypoint2[0] == "N" or waypoint2[0] == "S":
                    ship[0] += waypoint2[1]
                elif waypoint2[0] == "E" or waypoint2[0] == "W":
                    ship[1] += waypoint2[1]
            pass

    waypoint_off_ships_bow = abs(waypoint1[1]) + abs(waypoint2[1])
    manhattan_distance = abs(ship[0]) + abs(ship[1])
    starting_location = abs(s1) + abs(s2)

    return manhattan_distance + starting_location


if __name__ == "__main__":
    # print("Part 1, test:", manhattanDistance(processed_test_data)) # 25
    # print("Part 1:", manhattanDistance(processed_data))
    # print("Part 2, test:", waypointShift(processed_test_data, 1, 10))
    print("Part 2:", waypointShift(processed_data, 1, 10))
    pass


# too high: 71168, 71146
