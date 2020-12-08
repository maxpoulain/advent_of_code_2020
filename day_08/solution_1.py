from typing import List, Tuple


def load_and_process_input_file(filename: str) -> List[Tuple[str, int]]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            splited_line = line.replace('\n', '').split(' ')
            operation_type = splited_line[0]
            argument = int(splited_line[1])
            rows.append((operation_type, argument))
    return rows


def compute_instruction(rows: List[Tuple[str, int]]):
    accumulator = 0
    prev_instructions_index = []
    index = 0
    while True:
        operation_type, argument = rows[index]

        if index in prev_instructions_index:
            return accumulator
        else:
            prev_instructions_index.append(index)

        if operation_type == 'acc':
            accumulator += argument
            index += 1
        elif operation_type == 'jmp':
            index += argument
        else:
            index += 1



if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    print(rows)
    accumulator = compute_instruction(rows)
    print(f'accumulator: {accumulator}')
