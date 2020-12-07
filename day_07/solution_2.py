from typing import Dict, List


class Bags:
    def __init__(self, color: str, number: int):
        self.color = color
        self.number = number

    def __str__(self):
        return str(self.number) + ' ' + self.color


class Node:
    def __init__(self, data: Bags):
        self.data = data
        self.children = []

    def add_node(self, node: 'Node'):
        self.children.append(node)


class Tree:
    def __init__(self, root: Bags):
        self.data = root
        self.children = []

    def add_node(self, node: Node):
        self.children.append(node)


def load_and_process_input_file(filename: str) -> Dict[str, List[Bags]]:
    rows = {}
    with open(filename) as f:
        for line in f.readlines():
            base_bag, others_bags = line.split('contain')
            base_bag = base_bag.strip().split(' bags')[0].strip()
            others_bags = others_bags.strip().split(', ')
            others_bags_processed = [' '.join(bag.split(' bag')[0].strip().split(' ')[1:3]) for bag in others_bags if
                                     'no' not in bag.split(' bag')[0].strip().split(' ')]
            others_bags_nb = [int(bag.split(' bag')[0].strip().split(' ')[0]) for bag in others_bags if
                              'no' not in bag.split(' bag')[0].strip().split(' ')]
            rows[base_bag] = [Bags(color, number) for (number, color) in
                              list(zip(others_bags_nb, others_bags_processed))]
    return rows


def build_tree(bags_data: Dict, node: Node or Tree) -> Node or Tree:
    for bag_color, bags in bags_data.items():
        if bag_color == node.data.color:
            for bag in bags:
                new_bag_data = Bags(bag.color, bag.number)
                node.add_node(build_tree(bags_data, Node(new_bag_data)))
    return node


def dfs(node: Tree or Node, visited: List, multiplier: int, count: List):
    if node not in visited:
        visited.append(node)
        count.append(multiplier * node.data.number)

        if len(node.children) == 0:
            multiplier = 1

        multiplier = multiplier * node.data.number

        for child in node.children:
            dfs(child, visited, multiplier, count)


def compute_result(rows: Dict[str, List[Bags]]) -> int:
    starting_bag = Bags('shiny gold', 1)
    root = Tree(starting_bag)
    tree = build_tree(rows, root)
    count = []
    dfs(tree, [], 1, count)
    return sum(count) - 1


if __name__ == '__main__':
    rows = load_and_process_input_file('input.txt')
    result = compute_result(rows)
    print(f"result: {result}")
