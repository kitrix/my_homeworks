word = input ('Введите слово: ')
indx = len(word)-1
while indx >= 0:
    if (word[indx]!= 'я') & (word[indx]!= 'з') :
            print (word[indx])
            indx -= 1
    else:
        indx -= 1
