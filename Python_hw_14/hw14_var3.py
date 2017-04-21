import os
import re

def extensions():
    ext_count = {}
    for root, dirs, files in os.walk('.'):
        for file in files:
            ext = re.findall('\.[a-z0-9A-Z]+$', file)
            if ext[0] not in ext_count:
                ext_count[ext[0]] = 1
            else:
                ext_count[ext[0]] += 1
    numb = 0
    found_ext = ''
    for ext in ext_count:
        if ext_count[ext] > numb:
            numb = ext_count[ext]
            found_ext = ext
    print(found_ext)

def main():
    extensions()

main()
