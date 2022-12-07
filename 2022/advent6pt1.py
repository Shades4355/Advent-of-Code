from advent2pt1 import open_file


def split_data(raw_data: str) -> list:
    data_list = []
    
    for letter in raw_data:
        data_list.append(letter)
    return data_list


def read_data(data_list: list) -> str:
    '''Takes in a list of 'random' letters; outputs the first instance of 4 concurrent, unique letters'''

    for i in range(0, len(data_list), 1):
        data_chunk = [data_list[i], data_list[i + 1], data_list[i + 2], data_list[i + 3]]

        if len(data_chunk) == len(set(data_chunk)):
            return "".join(data_chunk)
    
    print("Error: no Marker found!")
    exit()


def find_index(data_stream: list, data_chunk: str) -> int:
    '''Finds the index of (the last character in a string) in a list\n
    Returns an Integer'''

    return "".join(data_stream).find(data_chunk) + len(data_chunk)


def start():
    raw_data_stream = open_file("advent6.txt")
    data_stream = split_data(raw_data_stream[0])
    data_chunk = read_data(data_stream)
    index = find_index(data_stream, data_chunk)

    print(index)

#########
# start #
#########

if __name__ == "__main__":
    start()
