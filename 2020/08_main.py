

# with open("2020/08_data.txt", 'r') as file:
#     data = file.read()

with open("2020/08_test_data.txt", "r") as test_file:  # 8
    data = test_file.read()

# part 1 #


def bootup(file: str):
    commands = []

    parsed_data = file.split('\n')
    for command in parsed_data:
        parsed_command = command.split()
        executed = 0
        parsed_command.append(executed)
        commands.append(parsed_command)

    accumulator, boolean = loopHunter(commands)

    return accumulator, boolean


def loopHunter(command_list: list):
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

# part 2 #


def bootup2(file: str):
    commands = []

    parsed_data = file.split('\n')
    for command in parsed_data:
        parsed_command = command.split()
        executed = 0
        parsed_command.append(executed)
        commands.append(parsed_command)

    accumulator = bootFix(commands, 0, 0)

    return accumulator


def bootFix(command_list, n, acc, nj=[]):
    accumulator = acc
    command = command_list[n]
    nop_jmp = nj

    if command[2] == 0:
        if command[0] == "nop":
            command[2] = 1
            if int(command[1]) > 0:
                nop_jmp.append(["nop", n])
            return bootFix(command_list, n + 1, accumulator, nop_jmp)
        elif command[0] == "acc":
            accumulator += int(command[1])
            command[2] = 1
            return bootFix(command_list, n + 1, accumulator, nj)
        elif command[0] == "jmp":
            command[2] = 1
            if int(command[1]) <= 0:
                nop_jmp.append(["jmp", n])
            return bootFix(command_list, n + int(command[1]), accumulator, nop_jmp)
    else:
        print("nj:", nj)
        for pair in nj:
            borked_command = pair[0]
            position = pair[1]
            if borked_command == "jmp":
                command_list[position][0] = "nop"
                command_list[position][2] = 0
                # nj.remove(pair)
                print("popped nj:", nj)
                return bootFix(command_list, position, accumulator, nj)
            elif borked_command[0] == "nop":
                command_list[position][0] = "jmp"
                command_list[position][2] = 0
                # nj.remove(pair)
                print("popped nj:", nj)
                return bootFix(command_list, position, accumulator, nj)
            else:
                print("Error!")


if __name__ == "__main__":
    print("Part 1", bootup(data))
    # print("Part 2", bootup2(data))
