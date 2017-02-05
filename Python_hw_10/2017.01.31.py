import re
def open_and_edit():
    f = open("hse.html", 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    return s

def find_and_print(s):
    reg1 = 'Преподаватели.*?\n.*?\n<p>[0-9]+ ?[0-9]+'
    reg2 = 'Преподаватели.*?\n.*?\n<p>'
    res1 = re.findall(reg1,s)
    res2 = re.findall(reg2,s)
    number = res1[0].replace(res2[0], '')
    print('Число преподавателей:',number)
    f = open("found_number.txt", 'w', encoding = "utf-8")
    f.write(number)
    f.close()

def main():
    text = open_and_edit()
    find_and_print(text)

main()
