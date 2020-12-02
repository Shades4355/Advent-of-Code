file = open("2020/02_data.txt", "r")

def oldCorpPasswords(file):
    validPasswords = 0
    for line in file:
        # test if password is valid
        parsedLine = line.split()

        min_max = parsedLine[0].split('-')
        string = parsedLine[2]
        letter = parsedLine[1].strip(':')

        if int(min_max[0]) <= string.count(letter) <= int(min_max[1]):
            validPasswords += 1

    return("validPasswords: " + str(validPasswords))

####################

def newCoprPasswords(file):
    validPasswords = 0
    for line in file:
        parsedLine = line.split()
        yesAndNo = parsedLine[0].split('-')
        yes = int(yesAndNo[0]) - 1
        no = int(yesAndNo[1]) - 1
        string = parsedLine[2]
        letter = parsedLine[1].strip(':')

        if string[yes] == letter and string[no] != letter:
            validPasswords += 1
        elif string[no] == letter and string[yes] != letter:
            validPasswords += 1

    return("validPasswords: " + str(validPasswords))



# print(oldCorpPasswords(file))
print(newCoprPasswords(file))
