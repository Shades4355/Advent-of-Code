with open("2020/06_data.txt", "r") as fileInput:
    data = fileInput.read()


# part 1 #
def countYeses(data: str):
    passengersList = data.split('\n\n')
    total = 0

    for group in passengersList:
        groupAnswers = []
        people = group.split('\n')

        for person in people:
            answers = [char for char in person]

            # add all of a group's answers to one List
            for char in answers:
                groupAnswers.append(char)

        # then count the unique entries
        total += len(set(groupAnswers))
    return total


print("Part 1:", countYeses(data))  # 6351
