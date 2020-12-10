from typing import List, Tuple


def load_and_process_input_file(filename: str) -> list[int]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(int(line.replace('\n', '')))
    return sorted(rows)


def find_jolt_differences(rows: List[int]) -> int:
    counter1 = 0
    counter3 = 0
    for index in range(1, len(rows)):
        if rows[index] - rows[index - 1] == 1:
            counter1 += 1
        elif rows[index] - rows[index - 1] == 3:
            counter3 += 1

    counter1 += 1  # first one
    counter3 += 1  # last one
    return counter1 * counter3


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = find_jolt_differences(rows)
    print(f'result: {result}')
