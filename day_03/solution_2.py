from typing import List


def get_rows_from_file(filename: str) -> List[str]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(line.split("\n")[0])
    return rows


def find_trees(rows: List, nb_of_right_deplacement: int, nb_of_down_deplacement:int) -> int:
    position = 0
    trees = 0
    for index, row in enumerate(rows[::nb_of_down_deplacement]):
        if position >= len(row):
            position = position % len(row)

        if row[position] == '#':
            trees += 1

        position += nb_of_right_deplacement

    return trees


if __name__ == '__main__':
    rows = get_rows_from_file('input.txt')
    result = 1
    for deplacement_right, deplacement_down in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
        tmp_result = find_trees(rows, deplacement_right, deplacement_down)
        print(f'Right {deplacement_right}, down {deplacement_down} => {tmp_result}')
        result *= tmp_result
    print(f'result: {result}')
