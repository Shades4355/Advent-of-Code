from advent2pt1 import get_input


def two_d_ify(engine_list:list):
    max_col = len(engine_list[0])
    max_row = len(engine_list)
    
    engine_array = [[0]*max_col]*max_row

    row = 0
    for line in engine_list:
        col = 0
        for cha in line:
            print("cha:", cha) # TODO: delete
            print("row:", row, "col:", col) # TODO: delete
            engine_array[row][col] = cha
            col += 1
        row += 1

    return engine_array

def start():
    engine_2d_list = []

    engine_list = get_input()
    engine_2d_list = two_d_ify(engine_list)

    print(engine_2d_list)
    
    

#########
# start #
#########
if __name__ == "__main__":
    start()