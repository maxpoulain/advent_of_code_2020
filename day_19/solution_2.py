from typing import List, Dict


def load_and_process_input_file(filename: str) -> tuple[dict[int, List[List]], List[str]]:
    rules = {}
    messages = []
    with open(filename) as f:
        is_messages = False
        for line in f.readlines():
            cleaned_line = line.replace('\n', '')
            if cleaned_line == '':
                is_messages = True
            else:
                if not is_messages:
                    splitted_line = cleaned_line.split(': ')
                    if 'a' in splitted_line[1]:
                        rls = 'a'
                    elif 'b' in splitted_line[1]:
                        rls = 'b'
                    else:
                        rls = [[int(vvv) for vvv in vv.split(' ')] for vv in splitted_line[1].split(' | ')]

                    rules[int(splitted_line[0])] = rls

                if is_messages:
                    messages.append(cleaned_line)

    return rules, messages


def apply_rules(rule: List, message: str) -> bool:
    if len(rule) > len(message):
        return False
    elif len(rule) == 0 or len(message) == 0:
        return len(rule) == 0 and len(message) == 0

    rule_id_or_str = rule[0]
    if type(rule_id_or_str) == str:
        if message[0] == rule_id_or_str:
            return apply_rules(rule[1:], message[1:])
    else:
        for r in rules[rule_id_or_str]:
            if apply_rules(list(r) + rule[1:], message):
                return True
    return False


def apply_rules_on_messages(rules: Dict, messages: List[str]) -> int:
    nb_valid_messages = 0
    for message in messages:
        if apply_rules(rules[0][0], message):
            nb_valid_messages += 1

    return nb_valid_messages


if __name__ == '__main__':
    rules, messages = load_and_process_input_file('input2.txt')
    result = apply_rules_on_messages(rules, messages)
    print(f'result: {result}')

