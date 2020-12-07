from typing import Dict, List


def load_and_process_input_file(filename: str) -> Dict[str, List[str]]:
    rows = {}
    with open(filename) as f:
        for line in f.readlines():
            base_bag, others_bags = line.split('contain')
            base_bag = base_bag.strip().split(' bags')[0].strip()
            others_bags = others_bags.strip().split(', ')
            rows[base_bag] = [bag.split(' bag')[0].strip().split(' ', 1)[1] for bag in others_bags]
    return rows


def can_contains_shiny_gold_bag(colors: List[str], rows: Dict[str, List[str]]) -> List[str]:
    possible_colors = []
    if len(colors) == 0:
        return []

    for base_color, other_colors in rows.items():
        for color in colors:
            if color in other_colors:
                possible_colors.append(base_color)

    return colors + can_contains_shiny_gold_bag(possible_colors, rows)


def compute_possible_colors(rows: Dict[str, List[str]]) -> int:
    return len(set(can_contains_shiny_gold_bag(['shiny gold'], rows))) - 1


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = compute_possible_colors(rows)
    print(f'result: {result}')
