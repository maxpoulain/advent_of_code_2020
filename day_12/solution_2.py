from typing import Tuple, List, Dict


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
    waypoint = {'E': 10, 'N': 1}
    position_ship = {'E': 0, 'N': 0, 'W': 0, 'S': 0}

    for direction, value in instructions:
        if direction == 'F':
            for k, v in waypoint.items():
                position_ship[k] = v * value + position_ship[k]

        if direction in ('N', 'S', 'E', 'W'):
            if direction in waypoint:
                waypoint[direction] += value
            else:
                if direction == 'S':
                    waypoint['N'] -= value
                    if waypoint['N'] < 0:
                        waypoint['S'] = abs(waypoint['N'])
                        del waypoint['N']

                if direction == 'W':
                    waypoint['E'] -= value
                    if waypoint['E'] < 0:
                        waypoint['W'] = abs(waypoint['E'])
                        del waypoint['E']

                if direction == 'N':
                    waypoint['S'] -= value
                    if waypoint['S'] < 0:
                        waypoint['N'] = abs(waypoint['S'])
                        del waypoint['S']

                if direction == 'E':
                    waypoint['W'] -= value
                    if waypoint['W'] < 0:
                        waypoint['E'] = abs(waypoint['W'])
                        del waypoint['W']

        if direction == 'L':
            if value == 90:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['W'] = val
                    elif dir == 'S':
                        new_waypoint['E'] = val
                    elif dir == 'E':
                        new_waypoint['N'] = val
                    elif dir == 'W':
                        new_waypoint['S'] = val
                waypoint = new_waypoint

            if value == 180:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['S'] = val
                    elif dir == 'S':
                        new_waypoint['N'] = val
                    elif dir == 'E':
                        new_waypoint['W'] = val
                    elif dir == 'W':
                        new_waypoint['E'] = val
                waypoint = new_waypoint

            if value == 270:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['E'] = val
                    elif dir == 'S':
                        new_waypoint['W'] = val
                    elif dir == 'E':
                        new_waypoint['S'] = val
                    elif dir == 'W':
                        new_waypoint['N'] = val
                waypoint = new_waypoint

        if direction == 'R':
            if value == 90:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['E'] = val
                    elif dir == 'S':
                        new_waypoint['W'] = val
                    elif dir == 'E':
                        new_waypoint['S'] = val
                    elif dir == 'W':
                        new_waypoint['N'] = val
                waypoint = new_waypoint

            if value == 180:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['S'] = val
                    elif dir == 'S':
                        new_waypoint['N'] = val
                    elif dir == 'E':
                        new_waypoint['W'] = val
                    elif dir == 'W':
                        new_waypoint['E'] = val
                waypoint = new_waypoint

            if value == 270:
                new_waypoint = {}
                for dir, val in waypoint.items():
                    if dir == 'N':
                        new_waypoint['W'] = val
                    elif dir == 'S':
                        new_waypoint['E'] = val
                    elif dir == 'E':
                        new_waypoint['N'] = val
                    elif dir == 'W':
                        new_waypoint['S'] = val
                waypoint = new_waypoint

    return position_ship


def compute_manhattan_distance(position_ship: Dict[str, int]) -> int:
    sumNS = abs(position_ship['N'] - position_ship['S'])
    sumEW = abs(position_ship['E'] - position_ship['W'])
    return sumEW + sumNS


if __name__ == '__main__':
    instructions = load_and_process_input_file('input.txt')
    print(f'instructions: {instructions}')
    position_ship = apply_instructions(instructions)
    distance = compute_manhattan_distance(position_ship)
    print(f'distance: {distance}')
