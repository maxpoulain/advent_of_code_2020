from typing import List


class MyNewInt(int):
    def __add__(self, number2):
        return MyNewInt(int(self) + number2)

    def __sub__(self, number2):
        return MyNewInt(int(self) * number2)


def load_and_process_input_file(filename: str) -> List[str]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            cleaned_line = line.replace('\n', '')
            rows.append(cleaned_line)

    return rows


def transform_rows(rows: List[str]) -> List[str]:
    new_rows = []
    for row in rows:
        row = row.replace('*', '-')
        new_row = []
        for element in row:
            if element == '(' or element == ')' or element == '+' or element == '-' or element == ' ':
                new_row.append(element)
            else:
                new_row.append(f'Operations({element})')
        new_rows.append(''.join(new_row))

    return new_rows


def evaluate_rows(new_rows: List[str]) -> List[int]:
    results = []
    for row in new_rows:
        results.append(eval(row, {'Operations': MyNewInt}))

    return results


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    new_rows = transform_rows(rows)
    results = evaluate_rows(new_rows)
    print(f'results: {sum(results)}')
