from typing import List


def get_rows_from_file(filename: str) -> List[str]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(line.split("\n")[0])
    return rows


def find_trees(rows: List[str]) -> int:
    position = 0
    trees = 0
    for index, row in enumerate(rows):
        if position >= len(row):
            position = position % len(row)

        if row[position] == '#':
            trees += 1

        position += 3

    return trees



if __name__ == '__main__':
    rows = get_rows_from_file('input.txt')
    nb_trees = find_trees(rows)
    print(f'nb trees: {nb_trees}')
