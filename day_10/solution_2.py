from typing import List


def load_and_process_input_file(filename: str) -> list[int]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(int(line.replace('\n', '')))
    return sorted(rows)


def find_jolt_differences(rows: List[int]) -> int:
    possibilities = {0: 1}
    for row in rows:
        possibilities[row] = 0
        if row - 1 in possibilities:
            possibilities[row] += possibilities[row - 1]

        if row - 2 in possibilities:
            possibilities[row] += possibilities[row - 2]

        if row - 3 in possibilities:
            possibilities[row] += possibilities[row - 3]
    return possibilities[max(rows)]


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = find_jolt_differences(rows)
    print(f'result: {result}')
