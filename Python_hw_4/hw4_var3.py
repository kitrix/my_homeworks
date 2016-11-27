word = input('Введите слово: ')
if word == '':
    print ('Слово не введено')
word2 = ''
for i in range(len(word)):
    for k in range(len(word)):
        if k + i < len(word):
            word2 += word[k + i]
        else:
            word2 += word[k + i - len(word)]
    print (word2)
    word2 = ''
