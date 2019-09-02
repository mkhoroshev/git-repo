import os

def make_dir():
        name = input('Введите имя директории = ')
        dir_path = os.path.join(os.getcwd(),name)
        try:
            os.mkdir(dir_path)
            print('-' * 20)
            print(f'Директория {dir_path} успешно создана\n')
        except FileExistsError:
            print('Такая директория уже существует\n')
        except PermissionError:
            print('Отсутствуют права на запись\n')

def del_dir():
        name = input('Введите имя директории = ')
        dir_path = os.path.join(os.getcwd(),name)
        try:
            os.removedirs(dir_path)
            print('-' * 20)
            print(f'Директория {dir_path} успешно удалена\n')
        except NotADirectoryError:
            print('Не является директорией\n')
        except PermissionError:
            print('Отсутствуют права на удаление\n')
        except OSError:
            print(f'Директория {dir_path} отсутсвует\n')

def print_current_dir():
    try:
        dir_path = os.getcwd()
        directory = os.listdir(dir_path)
        list = [i for i in directory if os.path.isdir(i)]
        print('-' * 20)
        print('Содержимое тукущей директории')
        return print(f'{list}\n')
    except OSError:
        print('Не удалось отобразить содержимое папки')


def change_dir():
    name = input('Введите имя директории = ')
    try:
        os.chdir(name)
        print('-' * 20)
        print(f'Успешно перешел в {name}\n')
    except NotADirectoryError:
            print(f'{name} не является директорией\n')
    except OSError:
            print(f'Не удалось перейти в  {name}\n')

