from typing import List, Dict


def get_each_password(filename: str) -> List[Dict]:
    passwords = []
    with open(filename) as f:
        for line in f.readlines():
            row = {}
            splited_line = line.split()
            minimum, maximum = splited_line[0].split('-')
            char = splited_line[1].split(':')[0]
            passord = splited_line[2]
            row['min'] = int(minimum)
            row['max'] = int(maximum)
            row['char'] = char
            row['password'] = passord
            passwords.append(row)

    return passwords


def verify_password_policy(passwords: List[Dict]) -> int:
    nb_valid_password = 0

    for password_infos in passwords:
        nb_of_char = password_infos['password'].count(password_infos['char'])
        if password_infos['min'] <= nb_of_char <= password_infos['max']:
            nb_valid_password += 1

    return nb_valid_password


if __name__ == '__main__':
    passwords = get_each_password('input.txt')
    nb_valid_password = verify_password_policy(passwords)
    print(f'nb of valid password: {nb_valid_password}')
