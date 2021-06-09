from Documents import documents, directories


def search_name(number_doc):
    """ функция, которая спросит номер документа и выведет имя человека, которому он принадлежит
    """
    for document in documents:
        documents_sorted = dict([(document['number'], document['name'])])
        for doc, name in documents_sorted.items():
            if number_doc == doc:
                print(f"Имя пользователя: {name}")
                return name
    print(f"Документ с номером '{number_doc}' отсутствует")
    return f'Error'


def find_shelf(doc_number):
    """функция, которая спросит номер документа и выведет номер полки, на которой он находится
    """
    for keys, values in directories.items():
        if doc_number in values:
            print(f"Номер полки: {keys}")
            return keys
    print(f"Полка с номером документа {doc_number} отсутствует")
    return f'Error'


def get_list():
    """ функция, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"
    """
    result = ""
    for document in documents:
        result += f'{document["type"]} "{document["number"]}" "{document["name"]}"\n'
    print(result)
    return result


def add_new_document():
    """ функция, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и
    номер полки, на котором он будет храниться."""
    doc_new = dict()
    doc_new['type'] = input('Введите тип документа: ')
    doc_new['number'] = input('Введите номер документа: ')
    doc_new['name'] = input('Введите имя и фамилию владельца документа: ')
    shelf = input("Введите номер полки для хранения информации: ")
    if shelf in directories.keys():
        directories[shelf].append(doc_new['number'])
        documents.append(doc_new)
        print(f"Документ с номером {doc_new['number']} добавлен на полку {shelf}")
        return directories, documents, True
    print(f"Полка с номером {shelf} не существует")
    return directories, documents, False

def move_shelves():
    """функция, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.
    """
    doc_number = input("Введите номер документа: ")
    for keys, values in directories.items():
        if doc_number in values:
            shelf = input("Введите номер целевой полки: ")
            if shelf in directories.keys():
                directories[shelf].append(doc_number)
                values.remove(doc_number)
                print(f"Документ {doc_number} перемещен на полку {shelf}")
                return directories, True
            print(f"Полка с номером {shelf} не существует")
            return directories, False
    print(f"Документ с номером {doc_number} не найден")
    return directories, False

def add_new_shelf():
    """функция, которая спросит номер новой полки и добавит ее в перечень.
    """
    add_shelf = input("Введите номер новой полки: ")
    if add_shelf not in directories.keys():
        directories[add_shelf] = []
        print(f'Полка с номером {add_shelf} добавлена в перечень')
        return add_shelf, True
    print(f"Полка с номером {add_shelf} уже существует")
    return add_shelf, False

def del_number_doc():
    """ функция, которая спросит номер документа и удалит его из каталога и из перечня полок.
    """
    doc_number = input("Введите номер документа: ")
    for document in documents:
        doc = document['number']
        if doc == doc_number:
            documents.remove(document)
            for number, doc in directories.items():
                if doc_number in doc:
                    doc.remove(doc_number)
                    print(f'Документ {doc_number} удален из каталога и из перечня полок')
                    return documents, directories, True
    print(f"Документа с номером {doc_number} не существует")
    return documents, directories, False
