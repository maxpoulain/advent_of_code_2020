from functools import reduce
from typing import List, Dict


def load_and_process_input_file(filename: str) -> tuple[Dict, set, list[int], list[list[int]]]:
    fields = {}
    fields_values = []
    my_ticket = []
    nearby_tickets = []
    with open(filename) as f:
        count_empty_row = 0
        for line in f.readlines():
            if line != '\n':
                if count_empty_row == 0:
                    cleaned_line = line.replace('\n', '')
                    field_name = cleaned_line.split(':')[0]
                    range_1_start, range_1_end = cleaned_line.split(':')[1].split(" or ")[0].strip().split("-")
                    range_2_start, range_2_end = cleaned_line.split(':')[1].split(" or ")[1].strip().split("-")
                    range_values = list(range(int(range_1_start), int(range_1_end) + 1)) + list(range(int(range_2_start), int(range_2_end) + 1))
                    fields_values.extend(range_values)
                    fields[field_name] = range_values
                elif count_empty_row == 1:
                    if 'your ticket:' not in line:
                        my_ticket = [int(i) for i in line.replace('\n', '').split(',')]
                elif count_empty_row == 2:
                    if 'nearby tickets:' not in line:
                        nearby_tickets.append([int(i) for i in line.replace('\n', '').split(',')])
            else:
                count_empty_row += 1

    return fields, set(fields_values), my_ticket, nearby_tickets


def verify_is_ticket_values_are_in_range(fields_values: set[int], nearby_tickets: List[List[int]]) -> List[List[int]]:
    valid = []
    for ticket_value in nearby_tickets:
        intersection = set(ticket_value).intersection(fields_values)
        diff = list(set(ticket_value).difference(intersection))
        if len(diff) == 0:
            valid.append(ticket_value)

    return valid


def get_all_possibilities_per_columns(fields: Dict[str, List[int]], valid_tickets: List[List[int]]) -> Dict[int, List[str]]:
    possible_fields_per_columns = {}
    for col_id in range(len(valid_tickets[0])):
        possible_fields_per_columns[col_id] = []
        for field_name, field_value in fields.items():
            is_valid_for_all_tickets = False
            for valid_ticket in valid_tickets:
                value = valid_ticket[col_id]
                if value in field_value:
                    is_valid_for_all_tickets = True
                else:
                    is_valid_for_all_tickets = False
                    break

            if is_valid_for_all_tickets:
                updated_list = possible_fields_per_columns[col_id]
                updated_list.append(field_name)
                possible_fields_per_columns[col_id] = updated_list

    return possible_fields_per_columns


def get_rules_per_columns(possible_fields_per_columns: Dict[int, List[str]]) -> Dict[int, str]:
    fixed_fields = {}
    possible_fields_per_columns2 = possible_fields_per_columns.copy()
    while len(fixed_fields) < len(possible_fields_per_columns):
        for col_id, possible_fields in possible_fields_per_columns.items():
            if len(possible_fields) == 1:
                fixed_rule = possible_fields[0]
                fixed_fields[col_id] = fixed_rule
                correct_fields = {}
                for col_id2, possible_fields2 in possible_fields_per_columns2.items():
                    if fixed_rule in possible_fields2:
                        possible_fields2.remove(fixed_rule)
                        correct_fields[col_id2] = possible_fields2
                possible_fields_per_columns2 = correct_fields

    return fixed_fields


def compute_my_ticket_departure_fields(my_ticket: List[int], fixed_fields: Dict[int, str]) -> int:
    return reduce(lambda x, y: x * y, [my_ticket[col_id] for col_id, field in fixed_fields.items() if 'departure' in field])


if __name__ == '__main__':
    fields, fields_values, my_ticket, nearby_tickets = load_and_process_input_file('input.txt')
    valid_tickets = verify_is_ticket_values_are_in_range(fields_values=fields_values, nearby_tickets=nearby_tickets)
    possible_fields_per_columns = get_all_possibilities_per_columns(fields=fields, valid_tickets=valid_tickets)
    fixed_fields = get_rules_per_columns(possible_fields_per_columns=possible_fields_per_columns)
    result = compute_my_ticket_departure_fields(my_ticket=my_ticket, fixed_fields=fixed_fields)
    print(f'result: {result}')
