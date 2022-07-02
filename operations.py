import phone_item


def phone_list(file_directory: str, book: list):
    with open(file_directory, 'r', encoding='utf_8') as file:
        items = file.readlines()
        for i in range(0, len(items)):
            phone_item = tuple(items[i].split('**'))
            book.append(phone_item)


def open_book(book: list):
    if len(book) == 0:
        print('*** Телефонная книга пуста. ***')
    else:
        for i in range(0, len(book)):
            print(f'{i}     Имя: {book[i][0]} \n      Комментарий: {book[i][1]} \n      Номер: {book[i][2]}')
            print('')


def add_item(item, book: list):
    book.append(item)


def delete_item(index, book: list):
    book.pop(index)


def edit_item(index, name, comment, phone, book: list):
    # old_item = book[index]
    book.pop(index)
    book.insert(index, phone_item.phone_item(name, comment, phone))


def save_changes(book: list, file_directory: str):
    with open(file_directory, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            name = book[i][0]
            comment = book[i][1]
            phone = book[i][2]
            file.writelines(f'{name}**{comment}**{phone}')


def import_phone_book(new_file: str, phone_book_file: str, book: list):
    with open(new_file, 'r', encoding='utf_8') as file:
        items = file.readlines()
        for i in range(0, len(items)):
            phone_item = tuple(items[i].split('**'))
            book.append(phone_item)
    with open(phone_book_file, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            name = book[i][0]
            comment = book[i][1]
            phone = book[i][2]
            file.writelines(f'{name}**{comment}**{phone}')


def export_phone_book(book: list, file_directory: str, form: str, new_direct: str = 'export_file'):
    with open(file_directory, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            name = book[i][0]
            comment = book[i][1]
            phone = book[i][2]
            file.writelines(f'{name}**{comment}**{phone}')
    new_direct = f'{new_direct}.{form}'
    with open(new_direct, 'w', encoding='utf-8') as file:
        for i in range(0, len(book)):
            name = book[i][0]
            comment = book[i][1]
            phone = book[i][2]
            file.writelines(f'{name}**{comment}**{phone}')