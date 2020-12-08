

with open("2020/08_data.txt", 'r') as file:
    data = file.read()


# part 1 #


def loopHunter(file: str):
    commands = []

    parsed_data = file.split('\n')
    for command in parsed_data:
        parsed_command = command.split()
        executed = 0
        parsed_command.append(executed)
        commands.append(parsed_command)
        # print(commands)

    accumulator = bootup(commands, 0, 0)

    return accumulator


def bootup(command_list: list, n: int, acc: int):
    accumulator = acc
    command = command_list[n]
    if command[2] == 0:
        if command[0] == "nop":
            command[2] = 1
            return bootup(command_list, n + 1, accumulator)
        elif command[0] == "acc":
            accumulator += int(command[1])
            command[2] = 1
            return bootup(command_list, n + 1, accumulator)
        elif command[0] == "jmp":
            command[2] = 1
            return bootup(command_list, n + int(command[1]), accumulator)
    else:
        return accumulator


if __name__ == "__main__":
    print(loopHunter(data))
