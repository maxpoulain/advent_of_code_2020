from typing import List, Tuple


def load_and_process_input_file(filename: str) -> list[int]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(int(line.replace('\n', '')))
    return rows


def compute_possibilities(list_of_possible: list[int]) -> list[int]:
    return [x + y for x in list_of_possible for y in list_of_possible]


def find_problem_in_list(rows: list[int]) -> int:
    for index in range(25, len(rows)):
        if rows[index] not in compute_possibilities(rows[index - 25:index]):
            return rows[index]


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = find_problem_in_list(rows)
    print(f'result: {result}')
