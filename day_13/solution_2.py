from functools import reduce
from math import lcm
from typing import List


def load_and_process_input_file(filename: str) -> list:
    bus_ids = []
    with open(filename) as f:
        for index, line in enumerate(f.readlines()):
            if index != 0:
                bus_ids += [int(bus_id) if bus_id != 'x' else bus_id for bus_id in line.replace('\n', '').split(',')]
    return bus_ids


def get_id_of_the_earliest_bus(bus_ids: List) -> int:
    start_timestamp = 100000000000000
    bus_ids_without_x = [id for id in bus_ids if id != 'x']
    minutes = [i for i in range(0, len(bus_ids))]
    while True:
        modulos_equals_0 = []
        for minute, bus_id in zip(minutes, bus_ids):
            if bus_id != 'x':
                if (start_timestamp + minute) % bus_id > 0:
                    break
                else:
                    modulos_equals_0.append(bus_id)
        if len(modulos_equals_0) == len(bus_ids_without_x):
            return start_timestamp
        else:
            if len(modulos_equals_0) > 1:
                start_timestamp += reduce(lcm, modulos_equals_0)
            else:
                start_timestamp += 1


if __name__ == '__main__':
    bus_ids = load_and_process_input_file('input.txt')
    result = get_id_of_the_earliest_bus(bus_ids)
    print(f'result: {result}')
