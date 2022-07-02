import datetime


def log(index: int, operation: str, book: list):
    time = datetime.datetime.now().strftime('%d.%m.%y %H:%M')
    name = book[index][0]
    comment = book[index][1]
    phone = book[index][2]
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'{time}  --  {operation}  --  № {index} -> Name: {name}  |  Comment: {comment}  |  Phone: {phone} \n')


def log_import_export(operation: str, new_file_direct: str):
    time = datetime.datetime.now().strftime('%d.%m.%y %H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'{time}  --  {operation}  -> {new_file_direct}\n')


def clear_log():
    with open('log.txt', 'w') as file:
        file.write('')