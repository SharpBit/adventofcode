import re

from utils import timed

passwords = open('inputs/2020-02.txt').readlines()

@timed
def part_one():
    valid_passwords = 0
    for pw in passwords:
        regex_match = r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
        min_req, max_req, letter, password = re.findall(regex_match, pw)[0]
        letter_count = sum(1 for char in password if char == letter)
        if int(min_req) <= letter_count <= int(max_req):
            valid_passwords += 1
    return valid_passwords

@timed
def part_two():
    valid_passwords = 0
    for pw in passwords:
        regex_match = r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
        pos1, pos2, letter, password = re.findall(regex_match, pw)[0]
        if (password[int(pos1) - 1] == letter) ^ (password[int(pos2) - 1] == letter):
            valid_passwords += 1
    return valid_passwords


print(part_one())
print(part_two())
