import re
# I hate regex

from utils import timed

with open('inputs/2020-04.txt') as f:
    input_lines = f.readlines()

def get_passport_indexes(input_lines):
    passport_indexes = []
    for i, line in enumerate(input_lines):
        if i == 0 or input_lines[i - 1] == '\n':  # beginning of a passport
            passport_indexes.append([i, None])
        if i == len(input_lines) - 1 or input_lines[i + 1] == '\n':  # end of a passport
            passport_indexes[-1][1] = i

    return passport_indexes


@timed
def part_one(input_lines):
    passport_indexes = get_passport_indexes(input_lines)

    num_valid_passports = 0
    for passport_index in passport_indexes:
        passport_info = ' '.join(input_lines[passport_index[0]:passport_index[1] + 1]).split(' ')  # split by field
        fields = dict([field.split(':') for field in passport_info])

        if len(passport_info) < 7:
            continue
        if len(passport_info) == 7 and 'cid' in fields.keys():  # cid is not the missing field: invalid
            continue

        num_valid_passports += 1

    return num_valid_passports

@timed
def part_two(input_lines):
    passport_indexes = get_passport_indexes(input_lines)

    num_valid_passports = 0
    for passport_index in passport_indexes:
        passport_info = ' '.join(input_lines[passport_index[0]:passport_index[1] + 1]).split(' ')  # split by field
        fields = dict([field.split(':') for field in passport_info])

        if len(passport_info) < 7:
            continue
        if len(passport_info) == 7 and 'cid' in fields.keys():  # cid is not the missing field: invalid
            continue


        invalid = False
        for field_name, field_data in fields.items():
            field_data = field_data.strip('\n')

            if field_name == 'byr' and not 1920 <= int(field_data) <= 2002:
                invalid = True
            elif field_name == 'iyr' and not 2010 <= int(field_data) <= 2020:
                invalid = True
            elif field_name == 'eyr' and not 2020 <= int(field_data) <= 2030:
                invalid = True
            elif field_name == 'hgt':
                height_regex = (
                    r'^(1([5-8]\d|9[0-3])cm|'  # 150-193cm
                    r'(59|6\d|7[0-6])in)$'  # 59-76in
                )
                if not re.match(height_regex, field_data):
                    invalid = True
            elif field_name == 'hcl' and not re.match(r'^#[0-9a-f]{6}$', field_data):
                invalid = True
            elif field_name == 'ecl' and field_data not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                invalid = True
            elif field_name == 'pid' and not re.match(r'^\d{9}$', field_data):
                # tfw u spend 1 hour trying to figure out why \d{9} matches strings with 10 digits
                invalid = True

            if invalid is True:
                break

        if not invalid:
            num_valid_passports += 1

    return num_valid_passports


print(part_one(input_lines))
print(part_two(input_lines))
