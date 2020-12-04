file = open("2020/04_data.txt", "r").read()


def scanner(batchData):
    validPassports = 0
    passportList = batchData.split('\n\n')

    for passport in passportList:
        if "byr:" in passport and "iyr:" in passport and "eyr:" in passport and "hgt:" in passport and "hcl:" in passport and "ecl:" in passport and "pid:" in passport:
            validPassports += 1

    return validPassports


# part 1 #
print(scanner(file))
