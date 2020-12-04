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
    total = 0
    for line in passportList:
        if checkPassport(line):
            total += 1
    return total

def checkPassport( passport):
    if not re.search('byr:(19[2-9][0-9]|200[0-2])( |\n|$)', passport):
        return False
    if not re.search('iyr:(201[0-9]|2020)( |\n|$)', passport):
        return False
    if not re.search('eyr:(202[0-9]|2030)( |\n|$)', passport):
        return False
    if not re.search('hgt:(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))( |\n|$)', passport):
        return False
    if not re.search('hcl:#[0-9a-f]{6}( |\n|$)', passport):
        return False
    if not re.search('ecl:(amb|blu|brn|gry|grn|hzl|oth)( |\n|$)', passport):
        return False
    if not re.search('pid:[0-9]{9}( |\n|$)', passport):
        return False
    return True


print("Part 2:", scannerRefined(file))
