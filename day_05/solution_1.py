from typing import List, Dict, Tuple


def load_and_process_input_file(filename: str) -> List[Tuple]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            seven_first_char = line[:7]
            three_last_char = line[7:]
            rows.append((seven_first_char, three_last_char))
    return rows


def compute_seven_first_char(sequence: str) -> int:
    return int(sequence.replace('F', '0').replace('B', '1'), 2)


def compute_last_three_char(sequence: str) -> int:
    return int(sequence.replace('R', '1').replace('L', '0'), 2)


def compute_seat_id(seven_first_char: str, last_three_char: str):
    row = compute_seven_first_char(seven_first_char)
    column = compute_last_three_char(last_three_char)
    seat_id = row * 8 + column
    return seat_id


def compute_results(rows: List[Tuple]) -> int:
    highest_seat_ID = 0
    for seven_first_char, last_three_char in rows:
        seat_id = compute_seat_id(seven_first_char, last_three_char)
        if highest_seat_ID < seat_id:
            highest_seat_ID = seat_id

    return highest_seat_ID


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    highest_seat_ID = compute_results(rows)
    print(f'highest seat ID: {highest_seat_ID}')
