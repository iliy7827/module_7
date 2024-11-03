import os
import time
'''"Файлы в операционной системе".'''
directory = '.'
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)  #формирования полного пути к файлам Объединяет корневую директорию
                                         # root и имя файла file в один полный путь
    filetime = os.path.getmtime(filepath)  #отображение времени последнего изменения файла
    # Получение форматированной строки с датой и временем.
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)  #отображение времени последнего изменения файла
    parent_dir = os.path.dirname(filepath) # отображение родительской директории файла
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,\n'
          f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')