file = open("2020/01_expense.txt", "r")

expenses = []
for line in file:
    expenses.append(int(line))

def find2020(list:list):
    for i in range(len(list) - 1):
        for entry in list:
            if list[i] + entry == 2020:
                return list[i] * entry

def find2020again(list:list):
    for i in list:
        for j in list:
            for k in list:
                if i + j + k == 2020:
                    return i * j * k

#########
# start #
#########
print("Part 1: " + str(find2020(expenses)))
print("Part 2: " + str(find2020again(expenses)))
