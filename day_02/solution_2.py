from typing import List, Dict, Optional


def get_each_password(filename: str) -> List[Dict]:
    passwords = []
    with open(filename) as f:
        for line in f.readlines():
            row = {}
            splited_line = line.split()
            position1, position2 = splited_line[0].split('-')
            char = splited_line[1].split(':')[0]
            passord = splited_line[2]
            row['position1'] = int(position1)
            row['position2'] = int(position2)
            row['char'] = char
            row['password'] = passord
            passwords.append(row)

    return passwords


def find(password: str, char: str) -> Optional[List[int]]:
    indexes = [index + 1 for index, letter in enumerate(password) if letter == char]
    if len(indexes) == 0:
        return None
    else:
        return indexes


def verify_password_policy(passwords: List[Dict]) -> int:
    nb_valid_password = 0
    for password_infos in passwords:
        positions = find(password_infos['password'], password_infos['char'])
        if positions:
            if (password_infos["position1"] in positions) ^ (password_infos["position2"] in positions):
                nb_valid_password += 1
    return nb_valid_password


if __name__ == '__main__':
    passwords = get_each_password('input.txt')
    nb_valid_password = verify_password_policy(passwords)
    print(f'nb of valid password: {nb_valid_password}')
