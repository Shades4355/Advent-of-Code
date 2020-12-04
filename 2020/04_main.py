import re

file = open("2020/04_data.txt", "r").read()

# part 1 #


def scanner(batchData):
    validPassports = 0
    passportList = batchData.split('\n\n')

    for passport in passportList:
        if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport and "pid:" in passport:
            validPassports += 1

    return validPassports


print(scanner(file))


# part 2 #
def scannerRefined(batchData):
    passportList = batchData.split('\n\n')

    passport = []
    for entry in passportList:
        subsection = []
        section = re.split(' |\n', entry)
        for i in section:
            j = i.split(":")
            subsection.append(j)
        passport.append(subsection)

    v = 0
    for i in passport:
        for j in i:
            if j[0] == "byr":
                if len(j[1]) == 4 and 1920 <= int(j[1]) <= 2002:
                    v += 1
            elif j[0] == 'iyr':
                if len(j[1]) == 4 and 2010 <= int(j[1]) <= 2020:
                    v += 1
            elif j[0] == 'eyr':
                if len(j[1]) == 4 and 2020 <= int(j[1]) <= 2030:
                    v += 1
            elif j[0] == 'hgt':


scannerRefined(file)
