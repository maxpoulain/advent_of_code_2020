import re
from typing import Dict, List


def load_and_process_input_file(filename: str) -> List[Dict]:
    documents = []
    with open(filename) as f:
        document = {}
        for line in f.readlines():
            doc = {}
            for field in line.replace('\n', '').split():
                key, value = field.split(":")
                doc[key] = value

            if len(doc) == 0:
                documents.append(document)
                document = {}
            else:
                if len(document) == 0:
                    document = doc
                else:
                    document |= doc
        documents.append(document)

    return documents


def verify_byr(document: Dict) -> bool:
    byr = document['byr']

    if re.match(r'^\d{4}', byr):
        if 1920 <= int(byr) <= 2002:
            return True
    else:
        return False


def verify_iyr(document: Dict) -> bool:
    iyr = document['iyr']

    if re.match(r'^\d{4}', iyr):
        if 2010 <= int(iyr) <= 2020:
            return True
    else:
        return False


def verify_eyr(document: Dict) -> bool:
    eyr = document['eyr']

    if re.match(r'^\d{4}', eyr):
        if 2020 <= int(eyr) <= 2030:
            return True
    else:
        return False


def verify_hgt(document: Dict) -> bool:
    hgt = document['hgt']

    try:
        value = int(hgt[:3])
    except ValueError:
        value = int(hgt[:2])

    unit = hgt[-2:]

    if unit == 'cm':
        if 150 <= value <= 193:
            return True

    if unit == 'in':
        if 59 <= value <= 76:
            return True

    return False


def verify_hcl(document: Dict) -> bool:
    hcl = document['hcl']

    if re.match(r'^#[0-9a-f]{6}$', hcl):
        return True
    else:
        return False


def verify_ecl(document: Dict) -> bool:
    ecl = document['ecl']

    if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False


def verify_pid(document: Dict) -> bool:
    pid = document['pid']

    if re.match(r'^[0-9]{9}$', pid):
        return True
    else:
        return False


def verify_documents(documents: List[Dict]) -> int:
    valid_documents = 0
    for document in documents:
        if len(document) == 8 or (len(document) == 7 and 'cid' not in document):
            if verify_byr(document) and verify_iyr(document) and verify_eyr(document) and verify_hgt(
                    document) and verify_hcl(document) and verify_ecl(document) and verify_pid(document):
                valid_documents += 1

    return valid_documents


if __name__ == '__main__':
    documents = load_and_process_input_file('input.txt')
    nb_valid_documents = verify_documents(documents)
    print(f'nb of valid documents: {nb_valid_documents}')
