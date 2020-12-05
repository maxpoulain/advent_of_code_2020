from typing import List, Dict


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


def verify_documents(documents: List[Dict]) -> int:
    valid_documents = 0
    for document in documents:
        if len(document) == 8:
            valid_documents += 1

        if len(document) == 7 and 'cid' not in document:
            valid_documents += 1
    return valid_documents


if __name__ == '__main__':
    documents = load_and_process_input_file('input.txt')
    nb_valid_documents = verify_documents(documents)
    print(f'nb of valid documents: {nb_valid_documents}')
