def get_name(documents, doc_number):
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
    return "Документ не найден"


def get_directory(directories, doc_number):
    for key, dir in directories.items():
        if doc_number in dir:
            return key
    return "Полки с таким документом не найдено"


def add_doc(documents, directories, document_type, number, name, shelf_number):
    documents.append({"type": document_type, "number": number, "name": name})
    shelf_key = str(shelf_number)
    if shelf_key not in directories:
        directories[shelf_key] = []
    directories[shelf_key].append(number)

    return "Документ успешно добавлен"


if __name__ == '__main__':
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
    ]

    directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
    }

    print(get_name(documents, "10006"))
    print(get_directory(directories, "11-2"))
    print(add_doc(documents, directories, 'international passport', '311 020203', 'Александр Пушкин', 3))
