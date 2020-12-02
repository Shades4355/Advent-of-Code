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
# print(oldCorpPasswords(file))
