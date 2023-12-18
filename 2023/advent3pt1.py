def get_input(location:str):
    array = []
    file = open(location, "r")

    for line in file:
        array.append(line.strip())
    
    return array


def two_d_ify(engine_list:list):
    max_row = len(engine_list)
    max_col = 0
    column = 0

    for i in range(0, len(engine_list)):
        if max_col < len(engine_list[column]):
            max_col = len(engine_list[column])
        column += 1

    engine_array = [["."]*max_col]*max_row

    row = 0
    while row < max_row:
        col = 0
        while col < max_col:
            print("cha:", engine_list[row][col])  # TODO: delete
            print("row:", row, "col:", col) # TODO: delete
            engine_array[row][col] = engine_list[row][col]
            col += 1
        row += 1

    return engine_array


def start():
    engine_2d_list = []

    engine_list = get_input("advent3input.txt")
    engine_2d_list = two_d_ify(engine_list)

    print(engine_2d_list)
    
    

#########
# start #
#########
if __name__ == "__main__":
    start()
