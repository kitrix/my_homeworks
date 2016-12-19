f = open("aphor.txt", 'r', encoding = "utf-8")
a = f.readlines()
f.close()
#выводит цитаты, в которых менее 15 слов
for i in range(len(a)):
    words = []
    words = a[i].split()
    numb = 0
    for j in range(len(words)):
        if words[j] != '—':
            numb += 1
    if numb < 16:
        print(a[i])
#в скольки цитатах есть "ум", печатает через запятую источники
author = []
um = 0
for i in range(len(a)):
    words = []
    words = a[i].split()
    for l, word in enumerate(words):
            words[l] = word.strip('.,!?();:*/\|<>-_%&#№@')
    for j in range(len(words)):
        if words[j] == 'ум':
            um += 1
            povtor = 0
            for k in range(len(author)):
                if author[k] == words[len(words)-1]:
                    povtor += 1
            if povtor == 0:
                author.append(words[len(words)-1])
out = ''
out = ', '.join(author)
print('Количество цитат = ', um)
print('Источники: ', out)

#спрашивает слова, выводит слово и цитаты, в которых встречается.
inp_words = []
while True:
    newword = input('Введите слово: ')
    if newword == '':
        break
    else:
        inp_words.append(newword)
for j in range(len(inp_words)):
    found = 0
    print(inp_words[j])
    for i in range(len(a)):
        words = []
        words = a[i].split()
        for l, word in enumerate(words):
            words[l] = word.strip('.,!?();:*/\|<>-_%&#№@')
        for k in range(len(words)):
            if inp_words[j] == words[k]:
                print(a[i])
                found += 1
                break
    if found == 0:
        print('Цитата с этим словом не найдена')
