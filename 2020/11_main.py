with open("2020/11_data.txt", "r") as file:
    data = file.read().split('\n')

floorplan = list()
for string in data:
    sublist = list()
    for char in string:
        sublist.append(char)
    floorplan.append(sublist)


with open("2020/11_test_data.txt", "r") as file:
    test_data = file.read().split('\n')

test_floorplan = list()
for string in test_data:
    sublist = list()
    for char in string:
        sublist.append(char)
    test_floorplan.append(sublist)


# part 1 #


def seatShuffle(floorplan: list):
    seats = 0

    while True:
        change = list()
        sitting = list()
        vacating = list()

        for i in range(len(floorplan)):
            for j in range(len(floorplan[i])):
                # If a seat is empty (L) and there are no occupied seats
                # adjacent to it, the seat becomes occupied.
                if floorplan[i][j] == "L":
                    if seatCheck(floorplan, i, j) == 0:
                        sitting.append((i, j))
                        change.append(True)

                # If a seat is occupied (#) and four or more seats
                # adjacent to it are also occupied, the seat becomes empty.
                # Otherwise, the seat's state does not change.
                elif floorplan[i][j] == "#":
                    if seatCheck(floorplan, i, j) >= 4:
                        vacating.append((i, j))
                        change.append(True)

                # Floor (.) never changes; seats don't move, and nobody sits on the floor.

        for i, j in sitting:
            floorplan[i][j] = "#"

        for i, j in vacating:
            floorplan[i][j] = "L"

        if not True in change:
            break

    for k in floorplan:
        seats += k.count("#")

    return seats


def occupiedSeat(seatList: list, i: int, j: int):
    if 0 <= i < len(seatList) and 0 <= j < len(seatList[i]):
        return seatList[i][j] == "#"
    return False


def seatCheck(seatList: list, i: int, j: int):
    occupied_seats = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if not k == i or not l == j:
                if occupiedSeat(seatList, k, l):
                    occupied_seats += 1
    return occupied_seats

# Part 2 #


def seatSeeing(floorplan: list):
    pass


if __name__ == "__main__":
    print("Part 1, test:", seatShuffle(test_floorplan))  # 37
    print("Part 1:", seatShuffle(floorplan))
    print("Part 2, test:")
