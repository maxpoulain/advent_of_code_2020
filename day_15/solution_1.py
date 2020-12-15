from typing import List


def load_and_process_input_file(filename: str) -> List[int]:
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data = [int(i) for i in line.replace("\n", "").split(',')]
    return data


def find_2020th_number(data: List[int]) -> int:
    numbers = {}

    for index, nb in enumerate(data):
        numbers[nb] = [index + 1]

    turn = len(data) + 1
    prev_nb = data[-1]
    while turn < 2021:
        if prev_nb in numbers and len(numbers[prev_nb]) < 2:
            prev_nb = 0
        else:
            prev_nb = numbers[prev_nb][-1] - numbers[prev_nb][-2]

        if prev_nb not in numbers:
            new_list = []
        else:
            new_list = numbers[prev_nb]
        new_list.append(turn)
        numbers[prev_nb] = new_list

        turn += 1

    return prev_nb


if __name__ == '__main__':
    data = load_and_process_input_file('input.txt')
    print(data)
    result = find_2020th_number(data)
    print(f'result: {result}')
