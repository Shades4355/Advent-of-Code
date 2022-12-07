from advent2pt1 import open_file
from advent6pt1 import *


def read_data(data_list: list, length: int) -> str:
    '''Takes in a list of 'random' letters; outputs the first instance of 4 concurrent, unique letters'''

    for i in range(0, len(data_list), 1):
        data_chunk = []
        for j in range(length):
            datum = data_list[i + j]
            data_chunk.append(datum)

        if len(data_chunk) == len(set(data_chunk)):
            return "".join(data_chunk)
    
    print("Error: no Marker found!")
    exit()


def start():
    raw_data_stream = open_file("advent6.txt")
    data_stream = split_data(raw_data_stream[0])
    data_chunk = read_data(data_stream, 14)
    index = find_index(data_stream, data_chunk)

    print(index)

#########
# start #
#########

if __name__ == "__main__":
    start()
