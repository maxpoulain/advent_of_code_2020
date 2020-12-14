from typing import List, Tuple, Optional, Dict


def load_and_process_input_file(filename: str) -> List[Tuple[str, List[str]]]:
    data = []
    with open(filename) as f:
        mask = None
        tmp = []
        for line in f.readlines():
            cleaned_line = line.replace("\n", "")
            if 'mask' in cleaned_line and mask is None:
                mask = cleaned_line.split('= ')[1]
            elif 'mask' in cleaned_line and mask:
                data.append((mask, tmp))
                tmp = []
                mask = cleaned_line.split('= ')[1]
            else:
                tmp.append(cleaned_line)
        data.append((mask, tmp))
    return data


def get_all_possible(new_value: List[str], index: int) -> List[int]:
    if index == len(new_value):
        return [int(''.join(new_value), 2)]

    if new_value[index] != 'X':
        return get_all_possible(new_value, index + 1)

    if new_value[index] == 'X':
        new_value_0 = new_value.copy()
        new_value_0[index] = '0'
        new_value_1 = new_value.copy()
        new_value_1[index] = '1'
        return get_all_possible(new_value_0, index + 1) + get_all_possible(new_value_1, index + 1)


def compute_new_value(mask: str, index: str) -> List[str]:
    new_value = []
    for digit_mask, digit_value in zip(mask, index):
        if digit_mask == 'X':
            new_value.append(digit_mask)
        elif digit_mask == '0' and digit_value == '1':
            new_value.append(digit_value)
        elif digit_mask == '0' and digit_value == '0':
            new_value.append(digit_value)
        else:
            new_value.append(digit_mask)

    return new_value


def compute(data: List[Tuple[str, List[str]]]) -> Dict:

    results = {}

    for mask, list_of_mem in data:
        for mem in list_of_mem:
            index = format(int(mem.split("[")[1].split("]")[0]), '#036b').replace('b', '0')
            value = int(mem.split("= ")[1])

            new_value = compute_new_value(mask=mask, index=index)
            all_possible = get_all_possible(new_value, 0)

            for poss in all_possible:
                results[poss] = value

    return results


def sum_results(results: Dict) -> int:
    return sum(results.values())


if __name__ == '__main__':
    data = load_and_process_input_file('input.txt')
    results = compute(data)
    result = sum_results(results)
    print(f'result: {result}')
