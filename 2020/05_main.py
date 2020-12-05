
file = "2020/05_data.txt"


# part 1 #
def seatSearch(file: str):
    "A Binary Search function"

    highestSeatID = 0
    with open(file) as inputFile:
        data = inputFile.read().split('\n')

    for seat in data:
        n = 0
        l_row = 0
        h_row = 127

        l_column = 0
        h_column = 7

        # for each F/B in seat[0] through seat[-3] (exclusive)
        # narrow down the possible seat rows
        for n in range(len(seat)-3):
            h_row, l_row = binarySearchROW(
                seat[n], h_row, l_row)
            seatSearchR = h_row

        # for each L/R in seat[-3] through seat[-1] (inclusive)
        # narrow down the possible seats
        for n in range(-3, 0, 1):
            h_column, l_column = binarySearchColumn(
                seat[n], h_column, l_column)
            seatSearchC = h_column

        # seat ID = row * 8 + column
        seatID = seatSearchR * 8 + seatSearchC

        # find highest seat ID
        if seatID > highestSeatID:
            highestSeatID = seatID

    return highestSeatID


def binarySearchROW(frontBack: str, high: int, low: int):
    if high != low:
        if frontBack == "F":
            high = (high + low) // 2
        elif frontBack == "B":
            low = (high + low) // 2
        else:
            print("Row Error")
            return None, None
    return high, low


def binarySearchColumn(rightLeft: str, high: int, low: int):
    if high != low:
        if rightLeft == "L":
            high = (high + low) // 2
        elif rightLeft == "R":
            low = (high + low) // 2
        else:
            print("Column Error")
            return None, None
    return high, low

# part 2 #


def findSeat(file: str):
    map = [['.'] * 8 for i in range(128)]

    with open(file) as inputFile:
        data = inputFile.read().split('\n')

    z = 0

    for seat in data:
        z += 1

        # binary search
        seatSearchR, seatSearchC = siftThroughSeats(seat)

        if map[seatSearchR][seatSearchC] == '.':
            map[seatSearchR][seatSearchC] = 'X'
        else:
            return "Error, map[seatSearchR][seatSearchC] = {} at seat #{}".format(map[seatSearchR][seatSearchC], z)
    row, column = locateSeat(map)

    return row * 8 + column


def siftThroughSeats(string: str):
    l_row = 0
    h_row = 127

    l_column = 0
    h_column = 7
    # for each F/B in seat[0] through seat[-3] (exclusive)
    # narrow down the possible seat rows
    for n in range(len(string)-3):
        h_row, l_row = binarySearchROW(
            string[n], h_row, l_row)
        seatSearchR = h_row

    # for each L/R in seat[-3] through seat[-1] (inclusive)
    # narrow down the possible seats
    for n in range(-3, 0, 1):
        h_column, l_column = binarySearchColumn(
            string[n], h_column, l_column)
        seatSearchC = h_column

    return seatSearchR, seatSearchC


def locateSeat(list: list):
    previous = None
    current = None
    x = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            previous = current
            current = list[i][j]
            if previous == "X" and current == ".":
                x += 1
            elif previous == "." and current == "X":
                x += 1
            else:
                x = 0
            if x == 2:
                return i, j - 1
    return None, None


if __name__ == '__main__':
    print("Part 1:", seatSearch(file))
    print("Part 2", findSeat(file))
