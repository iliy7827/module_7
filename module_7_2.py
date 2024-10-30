'''Задача "Записать и запомнить"'''

def custom_write(file_name, strings):
    strings_positions = {}
    number = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(number, byte)] = string
        number += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = ['Text for tell.', 'Используйте кодировку utf-8.','Because there are 2 languages!',
        'Спасибо!']
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы\
# file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),\
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.