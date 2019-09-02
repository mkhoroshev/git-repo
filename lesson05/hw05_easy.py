# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def make_dir(number):
    for idx in range(1,number+1):
        dir_path = os.path.join(os.getcwd(),'dir_' + str(idx))
        try:
            os.mkdir(dir_path)
            print(f'Директория ./dir_{idx} успешно создана')
        except FileExistsError:
            print('Такая директория уже существует')

def del_dir(number):
    for idx in range(1,number+1):
        dir_path = os.path.join(os.getcwd(),'dir_' + str(idx))
        try:
            os.removedirs(dir_path)
            print(f'Директория ./dir_{idx} успешно удалена')
        except NotADirectoryError:
            print('Не является директорией')
        except PermissionError:
            print('Отсутствуют права на удаление')
        except OSError:
            print(f'Директория ./dir_{idx} отсутсвует')


while True:
    question = input('Удалить или создать del|create\n')
    if question.lower() == "create":
        make_dir(9)
        break
    elif question.lower() == "del":
        del_dir(9)
        break

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dir_path = os.getcwd()
directory = os.listdir(dir_path)

list = [i for i in directory if os.path.isdir(i)]
print(list)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, sys
from pathlib import Path

name = sys.argv[0]
filename, file_extension = os.path.splitext(name)
new_file = filename +'_copy' + file_extension

try:
       if os.name == 'posix':
              operator = 'cp'
       elif os.name == 'nt':
              operator = 'copy'
       if not os.path.exists(new_file):
              os.system(f'{operator} {name} {new_file}')
              print(f'Копия файла {name} создана успешно')
       else:
              print(f'Файл {new_file} уже существует')
except OSError:
       Print('Ошибка копирования')

