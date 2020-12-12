from typing import Dict, List, Tuple


def load_and_process_input_file(filename: str) -> List[Tuple[str, int]]:
    instructions = []
    with open(filename) as f:
        for line in f.readlines():
            splitted_row = line.replace('\n', '')
            direction = splitted_row[0]
            value = int(splitted_row[1:])
            instructions.append((direction, value))
    return instructions


def apply_instructions(instructions: List[Tuple[str, int]]) -> Dict[str, int]:
    current_direction = 'E'
    position = {'E': 0, 'N': 0}

    for direction, value in instructions:
        if direction == 'F':
            if current_direction in position:
                position[current_direction] += value
            else:
                if current_direction == 'S':
                    position['N'] -= value

                if current_direction == 'W':
                    position['E'] -= value

        if direction in ('N', 'S', 'E', 'W'):
            if direction in position:
                position[direction] += value
            else:
                if direction == 'S':
                    position['N'] -= value

                if direction == 'W':
                    position['E'] -= value

        if direction == 'L':
            if value == 90:
                if current_direction == 'N':
                    current_direction = 'W'
                elif current_direction == 'S':
                    current_direction = 'E'
                elif current_direction == 'E':
                    current_direction = 'N'
                elif current_direction == 'W':
                    current_direction = 'S'

            if value == 180:
                if current_direction == 'N':
                    current_direction = 'S'
                elif current_direction == 'S':
                    current_direction = 'N'
                elif current_direction == 'E':
                    current_direction = 'W'
                elif current_direction == 'W':
                    current_direction = 'E'

            if value == 270:
                if current_direction == 'N':
                    current_direction = 'E'
                elif current_direction == 'S':
                    current_direction = 'W'
                elif current_direction == 'E':
                    current_direction = 'S'
                elif current_direction == 'W':
                    current_direction = 'N'

        if direction == 'R':
            if value == 90:
                if current_direction == 'N':
                    current_direction = 'E'
                elif current_direction == 'S':
                    current_direction = 'W'
                elif current_direction == 'E':
                    current_direction = 'S'
                elif current_direction == 'W':
                    current_direction = 'N'

            if value == 180:
                if current_direction == 'N':
                    current_direction = 'S'
                elif current_direction == 'S':
                    current_direction = 'N'
                elif current_direction == 'E':
                    current_direction = 'W'
                elif current_direction == 'W':
                    current_direction = 'E'

            if value == 270:
                if current_direction == 'E':
                    current_direction = 'N'
                elif current_direction == 'W':
                    current_direction = 'S'
                elif current_direction == 'S':
                    current_direction = 'E'
                elif current_direction == 'N':
                    current_direction = 'W'
    return position


def compute_manhattan_distance(position: Dict[str, int]) -> int:
    return sum([abs(v) for k, v in position.items()])


if __name__ == '__main__':
    instructions = load_and_process_input_file('input.txt')
    print(f'instructions: {instructions}')
    position = apply_instructions(instructions)
    distance = compute_manhattan_distance(position)
    print(f'distance: {distance}')
