from os import listdir
from os.path import isdir
from string import ascii_letters

keyword = input('Keyword: ')
list_of_dirs = []
results = open('results.txt', 'w')
def go_dir(path):
    try:
        if listdir(path) != list():
            for name in listdir(path):
                file_path = f'{path}\\{name}'
                if isdir(file_path):
                    if file_path not in list_of_dirs:
                        list_of_dirs.append(file_path)
                        go_dir(file_path)
                else:
                    try:
                        with open(file_path, 'r') as f:
                            file_path = file_path.replace('\\\\', '\\')
                            if keyword.lower() in f.read().lower():
                                print('Keyword found!')
                                results.write(f'FILENAME: {name}\nDIRECTORY: {file_path.replace(name, "")}\n{"-"*50}\n')
                            print(file_path)
                    except (PermissionError, UnicodeDecodeError):
                        pass
    except (PermissionError, FileNotFoundError):
        pass

for letter in list(ascii_letters.upper()[:26]):
    go_dir(f'{letter}:\\')
