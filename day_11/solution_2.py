from typing import List


def load_and_process_input_file(filename: str) -> list[str]:
    seats = []
    with open(filename) as f:
        for line in f.readlines():
            seats.append(line.replace('\n', ''))
    return seats


def is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=8, row_to_explore=(-1, 0, 1),
                                    col_to_explore=(-1, 0, 1)) -> bool:
    nb_of_empty_neighbours = 0
    for new_row_pos in row_to_explore:
        for new_col_pos in col_to_explore:
            if new_col_pos != 0 or new_row_pos != 0:
                coef = 1
                last_element = None
                while True:
                    if 0 <= row_nb + new_row_pos * coef < len(seats) and 0 <= col_nb + new_col_pos * coef < len(
                            seats[row_nb]):
                        row = seats[row_nb + new_row_pos * coef]
                        col = row[col_nb + new_col_pos * coef]
                        if col == 'L':
                            nb_of_empty_neighbours += 1
                            break
                        if col == '#':
                            break
                        last_element = col
                    else:
                        if last_element == '.':
                            nb_of_empty_neighbours += 1
                        break

                    coef += 1

    if nb_of_empty_neighbours == nb_neighbours:
        return True

    return False


def is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, row_to_explore=(-1, 0, 1),
                                                col_to_explore=(-1, 0, 1)) -> bool:
    nb_of_occupied_neighbours = 0
    for new_row_pos in row_to_explore:
        for new_col_pos in col_to_explore:
            if new_col_pos != 0 or new_row_pos != 0:
                coef = 1
                while True:
                    if 0 <= row_nb + new_row_pos * coef < len(seats) and 0 <= col_nb + new_col_pos * coef < len(seats[row_nb]):
                        row = seats[row_nb + new_row_pos * coef]
                        col = row[col_nb + new_col_pos * coef]
                        if col == '#':
                            nb_of_occupied_neighbours += 1
                            break
                        if col == 'L':
                            break
                    else:
                        break

                    coef += 1

    if nb_of_occupied_neighbours >= 5:
        return True

    return False


def replace_char_in_string(sequence: str, index_to_replace: int, new_char: str):
    list_of_char = list(sequence)
    list_of_char[index_to_replace] = new_char
    return ''.join(list_of_char)


def apply_rules(seats: List[str]) -> tuple[list[str], bool]:
    seats_to_modify = seats.copy()
    is_modify = False

    for row_nb in range(0, len(seats)):
        for col_nb in range(0, len(seats[row_nb])):

            row = seats[row_nb]
            col = row[col_nb]

            if 0 < row_nb < len(seats) - 1 and 0 < col_nb < len(row) - 1:
                if col == 'L':
                    if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                elif col == '#':
                    if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

            elif row_nb == 0 and 0 < col_nb < len(row) - 1:
                if col == 'L':
                    if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=5, row_to_explore=[0, 1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                elif col == '#':
                    if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, [0, 1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

            elif row_nb == len(seats) - 1 and 0 < col_nb < len(row) - 1:
                if col == 'L':
                    if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=5, row_to_explore=[0, -1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                elif col == '#':
                    if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, [0, -1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

            elif 0 < row_nb < len(seats) - 1 and col_nb == 0:
                if col == 'L':
                    if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=5, col_to_explore=[0, 1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                elif col == '#':
                    if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, col_to_explore=[0, 1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

            elif 0 < row_nb < len(seats) - 1 and col_nb == len(row) - 1:
                if col == 'L':
                    if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=5, col_to_explore=[0, -1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                elif col == '#':
                    if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, col_to_explore=[0, -1]):
                        seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

            else:
                if row_nb == 0 and col_nb == 0:
                    if col == 'L':
                        if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=3,
                                                           row_to_explore=[0, 1],
                                                           col_to_explore=[0, 1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                    elif col == '#':
                        if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, row_to_explore=[0, 1],
                                                                       col_to_explore=[0, 1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')
                elif row_nb == 0 and col_nb == len(row) - 1:
                    if col == 'L':
                        if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=3,
                                                           row_to_explore=[0, 1],
                                                           col_to_explore=[0, -1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                    elif col == '#':
                        if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, row_to_explore=[0, 1],
                                                                       col_to_explore=[0, -1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')
                elif row_nb == len(seats) - 1 and col_nb == 0:
                    if col == 'L':
                        if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=3,
                                                           row_to_explore=[0, -1],
                                                           col_to_explore=[0, 1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                    elif col == '#':
                        if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, row_to_explore=[0, -1],
                                                                       col_to_explore=[0, 1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')
                elif row_nb == len(seats) - 1 and col_nb == len(row) - 1:
                    if col == 'L':
                        if is_all_seats_adjacent_are_empty(seats, row_nb, col_nb, nb_neighbours=3,
                                                           row_to_explore=[0, -1],
                                                           col_to_explore=[0, -1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, '#')
                    elif col == '#':
                        if is_five_or_more_seats_adjacent_are_occupied(seats, row_nb, col_nb, row_to_explore=[0, -1],
                                                                       col_to_explore=[0, -1]):
                            seats_to_modify[row_nb] = replace_char_in_string(seats_to_modify[row_nb], col_nb, 'L')

    if seats_to_modify != seats:
        is_modify = True

    return seats_to_modify, is_modify


def apply_rules_while_modification(seats: List[str]) -> int:
    is_modify = True
    while is_modify:
        new_seats, is_modify = apply_rules(seats)
        seats = new_seats

    for row in seats:
        print(row)
    return sum([1 for row in seats for element in row if element == '#'])


if __name__ == '__main__':
    seats = load_and_process_input_file('input.txt')
    result = apply_rules_while_modification(seats)
    print(f'result: {result}')
