from typing import List, Tuple


def load_and_process_input_file(filename: str) -> list[int]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(int(line.replace('\n', '')))
    return rows


def compute_possibilities(list_of_possible: list[int]) -> list[int]:
    return [x + y for x in list_of_possible for y in list_of_possible]


def find_problem_in_list(rows: list[int]) -> int:
    for index in range(25, len(rows)):
        if rows[index] not in compute_possibilities(rows[index - 25:index]):
            return rows[index]


def compute_sum_of_min_and_max(list_of_contigous_numbers: List[int]):
    return min(list_of_contigous_numbers) + max(list_of_contigous_numbers)


def find_contiguous_set(rows: List[int], invalid_number: int) -> List[int]:
    base_index = 0
    invalid_number_index = rows.index(invalid_number)
    while base_index < invalid_number_index:
        index = base_index
        list_of_contigous_numbers = [rows[index]]
        while sum(list_of_contigous_numbers) < invalid_number and index < invalid_number_index:
            index += 1
            list_of_contigous_numbers.append(rows[index])
        if sum(list_of_contigous_numbers) == invalid_number:
            return list_of_contigous_numbers
        base_index += 1


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = find_problem_in_list(rows)
    print(f'result: {result}')
    list_of_contigous_numbers = find_contiguous_set(rows, result)
    print(f'list_of_contigous_numbers: {list_of_contigous_numbers}')
    final_result = compute_sum_of_min_and_max(list_of_contigous_numbers)
    print(f'final_result: {final_result}')
