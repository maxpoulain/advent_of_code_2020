from typing import List, Optional


def load_and_process_input_file(filename: str) -> List[int]:
    with open(filename) as f:
        numbers = []
        for line in f.readlines():
            numbers.append(int(line.split('\n')[0]))
        return numbers


def find_numbers_and_multiply(numbers: List[int]) -> Optional[int]:
    for index1, number1 in enumerate(numbers):
        for index2, number2 in enumerate(numbers[index1:]):
            for number3 in numbers[index2:]:
                total = number1 + number2 + number3
                if total == 2020:
                    return number1 * number2 * number3
    return None


if __name__ == '__main__':
    numbers = load_and_process_input_file('input.txt')
    result = find_numbers_and_multiply(numbers)
    print(f'result: {result}')
