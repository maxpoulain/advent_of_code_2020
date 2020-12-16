from typing import List, Union


def load_and_process_input_file(filename: str) -> tuple[set, list[int], list[list[int]]]:
    fields_values = []
    my_ticket = []
    nearby_tickets = []
    with open(filename) as f:
        count_empty_row = 0
        for line in f.readlines():
            if line != '\n':
                if count_empty_row == 0:
                    cleaned_line = line.replace('\n', '')
                    # field_name = cleaned_line.split(':')[0]
                    range_1_start, range_1_end = cleaned_line.split(':')[1].split(" or ")[0].strip().split("-")
                    range_2_start, range_2_end = cleaned_line.split(':')[1].split(" or ")[1].strip().split("-")
                    range_values = list(range(int(range_1_start), int(range_1_end) + 1)) + list(range(int(range_2_start), int(range_2_end) + 1))
                    fields_values.extend(range_values)
                elif count_empty_row == 1:
                    if 'your ticket:' not in line:
                        my_ticket = [int(i) for i in line.replace('\n', '').split(',')]
                elif count_empty_row == 2:
                    if 'nearby tickets:' not in line:
                        nearby_tickets.append([int(i) for i in line.replace('\n', '').split(',')])
            else:
                count_empty_row += 1

    return set(fields_values), my_ticket, nearby_tickets


def verify_is_ticket_values_are_in_range(fields_values: set[int], nearby_tickets: List[List[int]]) -> List[int]:
    bad_values = []
    for ticket_value in nearby_tickets:
        intersection = set(ticket_value).intersection(fields_values)
        bad_values.extend(list(set(ticket_value).difference(intersection)))

    return bad_values


def sum_bad_values(bad_values: List[int]) -> int:
    return sum(bad_values)


if __name__ == '__main__':
    fields_values, my_ticket, nearby_tickets = load_and_process_input_file('input.txt')
    bad_values = verify_is_ticket_values_are_in_range(fields_values, nearby_tickets)
    result = sum_bad_values(bad_values)
    print(f'result: {result}')