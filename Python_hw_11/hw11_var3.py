import re
def open_and_edit():
    f = open("linguistics.txt", 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    return s


def replace_and_output(s):
    s1 = re.sub('язык([а-я]{,3}( |\.|,|\)))','шашлык\\1', s)
    s2 = re.sub('Язык([а-я]{,3}( |\.|,|\)))','Шашлык\\1', s1)
    f = open("shashlyk.txt", 'w', encoding = "utf-8")
    f.write(s2)
    print('Текст записан в файл shashlyk.txt')
    f.close()


def main():
    text = open_and_edit()
    replace_and_output(text)

main()
