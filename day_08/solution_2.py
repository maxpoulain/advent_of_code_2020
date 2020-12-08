from typing import List, Tuple, Optional


def load_and_process_input_file(filename: str) -> List[Tuple[str, int]]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            splited_line = line.replace('\n', '').split(' ')
            operation_type = splited_line[0]
            argument = int(splited_line[1])
            rows.append((operation_type, argument))
    return rows


def compute_instruction(rows: List[Tuple[str, int]]) -> Optional[int]:
    accumulator = 0
    prev_instructions_index = []
    index = 0
    while True:
        if index in prev_instructions_index:
            return None
        elif index >= len(rows):
            return accumulator
        else:
            prev_instructions_index.append(index)

        operation_type, argument = rows[index]

        if operation_type == 'acc':
            accumulator += argument
            index += 1
        elif operation_type == 'jmp':
            index += argument
        else:
            index += 1


def change_instruction(rows: List[Tuple[str, int]], index: int, index_of_instruction_to_change: int,
                       instruction_to_change: Tuple[str, int]) -> Tuple[int, Tuple[str, int]]:
    if index_of_instruction_to_change:
        rows[index_of_instruction_to_change] = instruction_to_change

    op, arg = rows[index]
    if op == 'jmp':
        instruction_to_change = (op, arg)
        rows[index] = ('nop', 0)
        index_of_instruction_to_change = index

    return index_of_instruction_to_change, instruction_to_change


def find_instruction_to_change(rows: List[Tuple[str, int]]) -> Optional[int]:
    index_of_instruction_to_change = None
    instruction_to_change = None
    for index in range(0, len(rows)):
        index_of_instruction_to_change, instruction_to_change = change_instruction(rows, index,
                                                                                   index_of_instruction_to_change,
                                                                                   instruction_to_change)

        accumulator = compute_instruction(rows)
        if accumulator:
            print(f'index of instruction to change: {index_of_instruction_to_change}')
            print(f'instruction to change: {instruction_to_change}')
            return accumulator


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    accumulator = find_instruction_to_change(rows)
    print(f'accumulator: {accumulator}')
