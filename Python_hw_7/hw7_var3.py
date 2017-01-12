def open_and_edit():
    name = input('Введите название файла: ')
    f = open(name, 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    s1 = s.lower()
    a = s1.split()
    for i, word in enumerate(a):
        a[i] = word.strip('.,!?();:*/\|<>-_%&#№@+~')
    return a

def find_in_text(t):
    hood = []
    for word in t:
        if word.endswith('hood'):
            hood.append(word)
    print('В тексте нашлось ', len(hood), ' существительных с суффиксом -hood')
    return hood

def short_list(arr):
    short = [] #массив существительных и их вхождений без повторов
    arr2 = []
    for k in arr:
        arr2.append(k)
    for i in range(len(arr2)-1):
        if arr2[i]:
            short.append(arr2[i])
            x = 1
            for j in range(i+1, len(arr2)):
                if arr2[i]:
                    if arr2[i] == arr2[j]:
                        x += 1
                        arr2[j] = []
            short.append(x)
    return short

def min_freq(arr):
    short = short_list(arr)
    min = short[1]
    index = 1
    for k in range(1, len(short), 2):
        if short[k] < min:
            index = k
            min = short[k]
    print('Минимальную частотность имеет существительное', short[index-1])

def print_nouns(arr):
    nouns = []
    short = short_list(arr)
    for word in short:
        if type(word) != int:
            nouns.append(word.replace('hood', ''))
    all_nouns = ', '.join(nouns)
    print('Найденный слова образованы от существительных ', all_nouns)
           

def main():
    text = open_and_edit()
    found = find_in_text(text)
    min_freq(found)
    print_nouns(found)

main()
