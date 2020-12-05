
file = "2020/05_data.txt"


def seatSearch(file: str):
    "A Binary Search function"

    highestSeatID = 0
    with open(file) as inputFile:
        data = ['BFFFBBFRRR']

    for seat in data:
        n = 0
        l_row = 0
        h_row = 127

        l_column = 0
        h_column = 8

        # for each F/B in seat[0] through seat[-3] (exclusive)
        # narrow down the possible seat rows
        for n in range(len(seat)-3):
            seatSearchR, h_row, l_row = binarySearchROW(
                seat[n], h_row, l_row)
            print("seat search r:", seatSearchR)

        # for each L/R in seat[-3] through seat[-1] (inclusive)
        # narrow down the possible seats
        for n in range(-3, 0, 1):
            seatSearchC, h_column, l_column = binarySearchColumn(
                seat[n], h_column, l_column)
            print("seat search C:", seatSearchC)

        # seat ID = row * 8 + column
        seatID = seatSearchR * 8 + seatSearchC
        print('~' * 40)
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


print(seatSearch(file))


# wrong answers: 893, 990

# manual check:
# highest possible row = 127
# highest possible column = 7
# highest possible seatID = 1023
