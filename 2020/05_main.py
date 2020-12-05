
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
            seatSearchR, h_row, l_row = binarySearchROW(
                seat[n], h_row, l_row)

        # for each L/R in seat[-3] through seat[-1] (inclusive)
        # narrow down the possible seats
        for n in range(-3, 0, 1):
            seatSearchC, h_column, l_column = binarySearchColumn(
                seat[n], h_column, l_column)

        # seat ID = row * 8 + column
        seatID = seatSearchR * 8 + seatSearchC

        # find highest seat ID
        if seatID > highestSeatID:
            highestSeatID = seatID

    return highestSeatID


def binarySearchROW(highLow: str, high: int, low: int):
    if high != low:
        guess = low + (high - low) // 2

        if highLow == "F":
            high = guess - 1
        elif highLow == "B":
            low = guess + 1
        else:
            print("Row Error")
            return None, None, None
    else:
        guess = high
        return guess, high, low
    return guess, high, low


def binarySearchColumn(highLow: str, high: int, low: int):
    if high != low:
        guess = low + (high - low) // 2

        if highLow == "L":
            high = guess - 1
        elif highLow == "R":
            low = guess + 1
        else:
            print("Column Error")
            return None, None, None
    else:
        guess = high
        return guess, high, low
    return guess, high, low


# part 2 #
def findSeat(file: str):
    map = [['.'] * 128] * 8

    with open(file) as inputFile:
        data = inputFile.read().split('\n')

    z = 0

    for seat in data:
        z += 1
        n = 0
        l_row = 0
        h_row = 127

        l_column = 0
        h_column = 7

        # for each F/B in seat[0] through seat[-3] (exclusive)
        # narrow down the possible seat rows
        for n in range(len(seat)-3):
            seatSearchR, h_row, l_row = binarySearchROW(
                seat[n], h_row, l_row)

        # for each L/R in seat[-3] through seat[-1] (inclusive)
        # narrow down the possible seats
        for n in range(-3, 0, 1):
            seatSearchC, h_column, l_column = binarySearchColumn(
                seat[n], h_column, l_column)

        map[seatSearchC][seatSearchR] = 'X'


if __name__ == '__main__':
    print("Part 1:", seatSearch(file))
    print("Part 2", findSeat(file))
