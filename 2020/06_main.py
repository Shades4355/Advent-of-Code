import collections
with open("2020/06_data.txt", "r") as fileInput:
    data = fileInput.read()


# part 1 #
def countAnyYeses(data: str):
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


# Part 2 #

def countAllYeses(data):
    passengersList = data.split('\n\n')
    total = 0

    for i in range(len(passengersList)):
        group = passengersList[i].split('\n')
        groupAnswers = []

        for answers in group:
            answer = [char for char in answers]

            for char in answer:
                groupAnswers.append(char)

        countedAnswers = collections.Counter(groupAnswers)

        for key in countedAnswers:
            if countedAnswers[key] - len(group) >= 0:
                total += 1

    return total


print("Part 1:", countAnyYeses(data))  # 6351
print("Part 2:", countAllYeses(data))  # 3143
