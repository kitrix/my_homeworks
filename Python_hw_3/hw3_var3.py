words = []
while True:
    newword = input('Введите слово: ')
    if newword == '':
        break
    else:
        words.append(newword)
for i in range(len(words)):
    string = words[i]
    if (i+1) >= len(string):
        print('В этом слове не осталось символов')
    else:
        print(string[i+1:])
