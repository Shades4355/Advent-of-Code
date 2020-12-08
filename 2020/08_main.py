

# with open("2020/08_data.txt", 'r') as file:
#     data = file.read()

with open("2020/08_test_data.txt", "r") as test_file:  # 5, False
    data = test_file.read()                            # 8, True

# part 1 #


def bootup(file: str):
    commands = []

    parsed_data = file.split('\n')
    for command in parsed_data:
        parsed_command = command.split()
        commands.append(parsed_command)

    accumulator, boolean = loopHunter(commands)

    if boolean == True:
        return accumulator, boolean
    else:
        return accumulator, boolean


def loopHunter(command_list: list):
    n = 0
    accumulator = 0
    visited = []

    while n < len(command_list):
        ins, val = command_list[n]

        if n in visited:
            return accumulator, False

        visited.append(n)
        if ins == "nop":
            n += 1
        elif ins == "acc":
            accumulator += int(val)
            n += 1
        elif ins == "jmp":
            n += int(val)
    else:
        return accumulator, True
    n = 0
    accumulator = 0

    while n <= len(command_list) - 1:
        command = command_list[n]

        if command[2] == 1:
            return accumulator, False

        if command[0] == "nop":
            n += 1
        elif command[0] == "acc":
            accumulator += int(command[1])
            n += 1
        elif command[0] == "jmp":
            n += int(command[1])
        command[2] = 1
    else:
        return accumulator, True

# part 2 # (WIP)


if __name__ == "__main__":
    print("Part 1", bootup(data))
    # print("Part 2", bootup2(data))
