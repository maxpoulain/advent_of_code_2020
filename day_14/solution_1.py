from typing import List, Tuple, Optional, Dict


def load_and_process_input_file(filename: str) -> List[Tuple[str, List[str]]]:
    data = []
    with open(filename) as f:
        mask = None
        tmp = []
        for line in f.readlines():
            cleaned_line = line.replace("\n", "")
            if 'mask' in cleaned_line and mask == None:
                mask = cleaned_line.split('= ')[1]
            elif 'mask' in cleaned_line and mask :
                data.append((mask, tmp))
                tmp = []
                mask = cleaned_line.split('= ')[1]
            else:
                tmp.append(cleaned_line)
        data.append((mask, tmp))
    return data


def compute(data: List[Tuple[str, List[str]]]) -> Dict:
    results = {}
    for mask, list_of_mem in data:
        for mem in list_of_mem:
            index = int(mem.split("[")[1].split("]")[0])
            value = format(int(mem.split("= ")[1]), '#036b').replace('b', '0')

            new_value = []
            for digit_mask, digit_value in zip(mask, value):
                if digit_mask == 'X':
                    new_value.append(digit_value)
                elif digit_mask == '0':
                    new_value.append(digit_mask)
                else:
                    new_value.append(digit_mask)

            results[index] = int(''.join(new_value), 2)

    return results


def sum_results(results: Dict) -> int:
    return sum(results.values())


if __name__ == '__main__':
    data = load_and_process_input_file('input.txt')
    results = compute(data)
    result = sum_results(results)
    print(f'result: {result}')
