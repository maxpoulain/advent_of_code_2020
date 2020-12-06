from typing import List


def load_and_process_input_file(filename: str) -> List[List[set]]:
    groups = []
    with open(filename) as f:
        group = []
        for line in f.readlines():
            splitted_value = line.replace('\n', '').split()

            if len(splitted_value) == 0:
                groups.append(group)
                group = []
            else:
                group.append({char for char in splitted_value[0]})

        groups.append(group)

    return groups


def count_number_of_yes_for_each_group_and_sum(groups: List[List[set]]) -> int:
    return sum([len(set.intersection(*group)) for group in groups])


if __name__ == '__main__':
    groups = load_and_process_input_file('input.txt')
    result = count_number_of_yes_for_each_group_and_sum(groups)
    print(f'result: {result}')
