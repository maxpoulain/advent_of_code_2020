from typing import List, Tuple, Dict


def load_and_process_input_file(filename: str) -> Dict[Tuple[int, int, int, int], str]:
    rows = []
    points = {}
    with open(filename) as f:
        for line in f.readlines():
            cleaned_line = line.replace('\n', '')
            splitted_line = [ch for ch in cleaned_line]
            rows.append(splitted_line)

        for x in range(len(rows)):
            for y in range(len(rows[0])):
                points[(x, y, 0, 0)] = rows[x][y]

    return points


def simulate_cycle(points: Dict[Tuple[int, int, int, int], str]) -> Dict[Tuple[int, int, int, int], str]:
    new_points = {}
    for point in points:
        ngb = get_neighbours(point[0], point[1], point[2], point[3])
        count_active = len(['#' for n in ngb if n in points and points[n] == '#'])
        if points[point] == '.':
            if count_active == 3:
                new_points[point] = '#'
            else:
                new_points[point] = '.'

        if points[point] == '#':
            if 2 <= count_active <= 3:
                new_points[point] = '#'

        for neighbour in ngb:
            if neighbour not in points:
                neighbours_of_neighbour = get_neighbours(neighbour[0], neighbour[1], neighbour[2], neighbour[3])
                count_active = len(['#' for n in neighbours_of_neighbour if n in points and points[n] == '#'])
                if count_active == 3:
                    new_points[neighbour] = '#'
                else:
                    new_points[neighbour] = '.'

    return new_points


def get_neighbours(x: int, y: int, z: int, w: int) -> List[Tuple[int, int, int, int]]:
    list_of_neighbours = []
    for new_x in range(-1, 2):
        for new_y in range(-1, 2):
            for new_z in range(-1, 2):
                for new_w in range(-1, 2):
                    if not (new_x == 0 and new_y == 0 and new_z == 0 and new_w == 0):
                        list_of_neighbours.append((x + new_x, y + new_y, z + new_z, w + new_w))

    return list_of_neighbours


if __name__ == '__main__':
    points = load_and_process_input_file('input.txt')
    for cycle in range(6):
        points = simulate_cycle(points)
        print(list(points.values()).count('#'))
