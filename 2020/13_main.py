with open("2020/13_custom_test_data.txt") as input_test_file:
    test_data = input_test_file.read().split('\n')
test_leave_time = int(test_data[0])
test_busses = test_data[1]
processed_test_busses = test_busses.split(',')


with open("2020/13_data.txt") as input_file:
    data = input_file.read().split('\n')
leave_time = int(data[0])
busses = data[1]
processed_busses = busses.split(',')


# Part 1 #
def bussFinder(departure_time: int, all_busses: list):
    bus_id = 0  # ID of the bus
    bus_arrivals = list()
    active_busses = list()

    for bus in all_busses:
        if not bus == "x":
            active_busses.append(int(bus))
    for bus in active_busses:
        bus_time = 0  # time the bus actually arrives
        bus_id = bus
        while bus_time < departure_time:
            bus_time += bus_id
        bus_arrivals.append((bus_id, bus_time))

    shortest_time = departure_time
    shortest_bus = 0
    for bus, time in bus_arrivals:
        # find bus with smallest difference from departure_time
        time_difference = time - departure_time
        if time_difference <= shortest_time:
            shortest_time = time_difference
            shortest_bus = bus

    return shortest_time * shortest_bus

# Part 2 #


class Bus(object):
    def __init__(self, name, id, minutes_offset):
        self.name = name
        self.id = int(id)
        self.minutes_offset = int(minutes_offset)


def timestampHunter(busses: list):
    bus_list = list()
    earliest_time = 0

    for num, bus in enumerate(busses):
        if not bus == "x":
            bus_list.append(Bus(name="Bus {}".format(bus),
                                id=bus, minutes_offset=num))

    earliest_time = findTime(bus_list, bus_list[0].id, 0, 0)

    return earliest_time


def findTime(busses: list, step: int, n: int, start: int):
    # ax + bxy + cxyz + [...]
    bus_1 = busses[n]
    bus_2 = busses[n + 1]

    answer = 0
    m = 0
    while True:
        m += 1
        time = start + (step * m)
        print("m, n:", m, n)
        print("step:", step)
        print("time:", time)
        print("~" * 20)
        if (time + bus_2.minutes_offset) % bus_2.id == 0:
            if n + 2 < len(busses):  # there are busses left
                # recursive call
                new_step = time
                answer += findTime(busses, new_step, n + 1, time)
                return answer
            else:  # no busses left
                return time


if __name__ == "__main__":
    # print("Part 1, test:", bussFinder(test_leave_time, processed_test_busses))  # 295
    # print("Part 1:", bussFinder(leave_time, processed_busses))
    print("Part 2:", timestampHunter(processed_test_busses))  # 1068781
    pass
