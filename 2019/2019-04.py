from utils import timed


@timed
def part_one():
    password_range = [int(i) for i in open('inputs/2019-04.txt').read().split('-')]

    possible_passwords = []
    for password in range(password_range[0], password_range[1] + 1):
        password = str(password)

        consecutive = False
        increasing = True
        for i, digit in enumerate(password):
            if i != len(password) - 1 and int(digit) > int(password[i + 1]):
                increasing = False
                break
            if i != 0 and digit == password[i - 1]:
                consecutive = True
        if increasing and consecutive:
            possible_passwords.append(password)

    print(len(possible_passwords))


@timed
def part_two():
    password_range = [int(i) for i in open('inputs/2019-04.txt').read().split('-')]

    possible_passwords = []
    for password in range(password_range[0], password_range[1] + 1):
        password = str(password)

        consecutive = False
        increasing = True

        for i, digit in enumerate(password):
            if i != len(password) - 1 and int(digit) > int(password[i + 1]):
                increasing = False
                break
        if not increasing:
            continue

        i = 0
        consecutive_digits = []
        current_counter = 1
        while i < len(password) - 1:
            if password[i] == password[i + 1]:
                current_counter += 1
            else:
                consecutive_digits.append(current_counter)
                current_counter = 1

            if i + 1 == len(password) - 1:
                consecutive_digits.append(current_counter)

            i += 1

        consecutive = any(c == 2 for c in consecutive_digits)

        if not consecutive:
            continue
        possible_passwords.append(password)

    print(len(possible_passwords))


part_one()
part_two()
