import re
def open_and_edit():
    f = open("verbs.txt", 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    s1 = s.lower()
    a = s1.split()
    for i, word in enumerate(a):
        a[i] = word.strip('.,!?();:*/\|<>-_%&#№@+~—"')
    return a

def find_and_print(a):
    arr = []
    for word in a:
        if re.search('^программир((у(ю(т|щ(и(й|ми?|е|х)|е(го|му?|й)|ая|ую))?|я|е(шь|те?))|ова(л(а|и)?|ть))(с(я|ь))?|уем(ы(й|ми?|е|х)?|о(го|му?|й)|ая?|ую))', word):
            if word not in arr:
                arr.append(word)
    for verb in arr:
        print(verb)

def main():
    text = open_and_edit()
    find_and_print(text)

main()
    
