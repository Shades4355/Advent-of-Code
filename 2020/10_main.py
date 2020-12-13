with open("2020/10_data.txt", 'r') as input_file:
    data = input_file.read()

processed_data = [int(i) for i in data.split('\n')]
processed_data.append(0)
processed_data.sort()


with open("2020/10_test_data.txt", "r") as test_file:
    test_data = test_file.read()

processed_test_data = [int(i) for i in test_data.split('\n')]
processed_test_data.append(0)
processed_test_data.sort()


# Part 1 #


def adaptors(file: str):
    parsed_data = file.split("\n")
    num_data = [int(num) for num in parsed_data]
    num_data.append(0)
    num_data.sort()
    n = 0
    ones = 0
    threes = 1

    while n < len(num_data)-1:
        if num_data[n+1] - num_data[n] == 1:
            ones += 1
        elif num_data[n+1] - num_data[n] == 3:
            threes += 1
        n += 1

    return ones * threes

# part 2 #  # Not my work #

# Given a sorted sequence of adapter voltages, return the number of ways to
# connect them.


def num_connections(sequence):
    # Here is a list as long as the input. Each position contains the number of
    # ways to reach the end of the sequence from that position, if we know it.
    # In other cases, we'd likely use a dictionary, but for this particular problem,
    # I know something about the shape, so I can be efficient.
    # At first, we know nothing.
    connections_from_position = [None] * len(sequence)
    # Actually, we know one thing - there is exactly one way to connect when you're on
    # the last adapter. You've found the completed chain. This is our recursive base case,
    # or, put differently, the first subproblem we know the answer to.
    connections_from_position[-1] = 1

    def subprocess(position):
        # Don't redo work. If we've previously computed how many paths from this position
        # to the end, just give that back.
        cached = connections_from_position[position]
        if cached is not None:
            return cached
        # ... and if we haven't previously computed it, we'd better start.
        count = 0
        # Try to jump down the chain ...
        for i, v in enumerate(sequence[position+1:], start=1):
            # ... until the diff is too large.
            if v - sequence[position] > 3:
                break
            # OK, there is a valid jump i steps ahead of our current position. How many ways can
            # we get to the end from there? I dunno, recurse.
            count += subprocess(position + i)
        # The subproblem starting from this position is officially solved.
        # Write that down in your copybook now.
        connections_from_position[position] = count
        return count
    # And now, solving the actual problem.
    return subprocess(0)


if __name__ == "__main__":
    # print("Part 1:", adaptors(data))
    # print("Part 2:", num_connections(processed_test_data))  # 19208
    print("Part 2:", num_connections(processed_data))
