import random
# открывает файл, разбивает на строки
def open_file():
    f = open("words.txt", 'r', encoding = "utf-8")
    text = f.readlines()
    f.close()
    return(text)

# находит строку с нужной категорией слов, составляет массив
def find_words(word,text):
    for i in range(len(text)):
        line = []
        line = text[i].split()
        for l, w in enumerate(line):
            line[l] = w.strip('.,!?();:*/\|<>-_%&#№@')
        if line[0] == word:
            words = []
            for j in range(len(line)):
                if j > 0:
                    words.append(line[j])
    return(words)

# возвращает случайное существительное
def noun():
    find = 'существительное'
    nouns = find_words(find, text)
    return random.choice(nouns)

# возвращает случайный глагол в повелительном наклонении
def imperative():
    find = 'императив'
    imper = find_words(find, text)
    return random.choice(imper)

# возвращает случайное наречие, ставит его перед императивом
def adverb(imp):
    find = 'наречие'
    adverbs = find_words(find, text)
    return random.choice(adverbs) + ' ' + imp

# возвращает случайный глагол
def verb():
    find = 'глагол'
    verbs = find_words(find, text)
    return random.choice(verbs)

# возвращает случайное прилагательное
def adjective():
    find = 'прилагательное'
    adj = find_words(find, text)
    return random.choice(adj)

# возвращает случайное вопросительное слово
def question_word():
    find = 'вопрос'
    quest = find_words(find, text)
    return random.choice(quest)

# составляет утвердительное преложение
def pos_sentence():
    sentence = adjective() + ' ' + noun() + ' ' + verb() +\
               ' ' + adjective() + ' ' + noun() + '.'
    sentence = sentence.capitalize()
    return(sentence)

# составляет отрицательное преложение
def neg_sentence():
    sentence = adjective() + ' ' + noun() + ' не ' + verb() +\
               ' ' + adjective() + ' ' + noun() + '.'
    sentence = sentence.capitalize()
    return(sentence)

# составляет вопросительное преложение
def quest_sentence():
    sentence =  question_word()+ ' ' + adjective() + ' ' + noun() +\
               ' ' + verb() + ' ' + adjective() + ' ' + noun() + '?'
    sentence = sentence.capitalize()
    return(sentence)

# составляет повелительное преложение
def imper_sentence():
    sentence = adverb(imperative()) + ' ' + noun() + '!'
    sentence = sentence.capitalize()
    return(sentence)

# составляет условное преложение
def if_sentence():
    sentence = 'если бы ' + noun() + ' ' + verb() + ' ' + noun() +\
               ', то ' + noun() + ' ' + verb() + ' бы ' + noun() + '.'
    sentence = sentence.capitalize()
    return(sentence)
# выводит 5 предложений случайным образом
def random_print():
    spisok = [pos_sentence(), neg_sentence(), quest_sentence(),\
              imper_sentence(), if_sentence()]
    random.shuffle(spisok)
    for i in range(len(spisok)):
        print(spisok[i], end = ' ')

text = open_file()
random_print()


