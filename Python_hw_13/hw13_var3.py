import os
import re

def count_folders():
    result = 0
    for f in os.listdir('.'):
        if os.path.isdir(f):
            if re.search('^([а-яА-Я]| )+$',f):
                result += 1
    print('Найдено папок:',result)

def print_names():
    names = {}
    file_name = '^(.+)(\.[a-z]+)$'
    for f in os.listdir('.'):
        if os.path.isdir(f):
            if f not in names:
                names[f] = 1
        if os.path.isfile(f):
            r = re.search(file_name,f)
            if r:
                name = r.group(1)
                if name not in names:
                    names[name] = 1
    for name in sorted(names):
        print(name)

def main():
    count_folders()
    print_names()

main()
