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
                    if not occupiedSeat(floorplan, i, j - 1) and not occupiedSeat(floorplan, i, j + 1) and not occupiedSeat(floorplan, i - 1, j) and not occupiedSeat(floorplan, i + 1, j) and not occupiedSeat(floorplan, i - 1, j - 1) and not occupiedSeat(floorplan, i - 1, j + 1) and not occupiedSeat(floorplan, i + 1, j + 1) and not occupiedSeat(floorplan, i + 1, j - 1):
                        sitting.append((i, j))
                        change.append(True)

                # If a seat is occupied (#) and four or more seats
                # adjacent to it are also occupied, the seat becomes empty.
                # Otherwise, the seat's state does not change.
                elif floorplan[i][j] == "#":
                    occupied_seats = 0
                    if occupiedSeat(floorplan, i, j - 1):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i, j + 1):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i + 1, j - 1):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i + 1, j + 1):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i + 1, j):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i - 1, j):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i - 1, j - 1):
                        occupied_seats += 1
                    if occupiedSeat(floorplan, i - 1, j + 1):
                        occupied_seats += 1

                    if occupied_seats >= 4:
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


def occupiedSeat(list, i, j):
    if i == -1:
        return False
    if j == -1:
        return False
    try:
        if list[i][j] == "#":
            return True
        else:
            return False
    except:
        return False


if __name__ == "__main__":
    print("Part 1:", seatShuffle(floorplan))  # 37
