from typing import List


def load_and_process_input_file(filename: str) -> tuple[int, list]:
    bus_ids = []
    earliest_timestamp = None
    with open(filename) as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                earliest_timestamp = int(line.replace('\n', ''))
            else:
                bus_ids += [int(bus_id) for bus_id in line.replace('\n', '').split(',') if bus_id != 'x']
    return earliest_timestamp, bus_ids


def get_id_of_the_earliest_bus(earliest_timestamp: int, bus_ids: List[int]) -> int:
    minutes = 0
    while True:
        for bus_id in bus_ids:
            if (earliest_timestamp + minutes) % bus_id == 0:
                return minutes * bus_id
        minutes += 1


if __name__ == '__main__':
    earliest_timestamp, bus_ids = load_and_process_input_file('input.txt')
    result = get_id_of_the_earliest_bus(earliest_timestamp, bus_ids)
    print(f'result: {result}')
