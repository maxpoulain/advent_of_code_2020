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


def find_my_seat_id(rows: List[Tuple]) -> int:
    seats_id = list(set([compute_seat_id(seven_first_char, last_three_char) for seven_first_char, last_three_char in rows]))
    for seat1, seat2 in zip(seats_id[:-1],  seats_id[1:]):
        if seat2 - seat1 > 1:
            return (seat1 + seat2) // 2


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    my_seat_id = find_my_seat_id(rows)
    print(f'my seat ID: {my_seat_id}')
