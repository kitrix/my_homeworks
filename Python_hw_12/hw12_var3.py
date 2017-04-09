import re


def open_and_read():
    f = open("animal_farm.txt", 'r', encoding = "utf-8")
    s = f.read()
    f.close()
    return s


def read_sentences(s):
    s1 = re.sub('[a-z](\.|!|\?)','\\1@@', s)
    a = s1.split('@@')
    return a


def split_and_count(a):
    for i in range(len(a)):
        words = a[i].split()
        words2 = [words[j].strip('.,!?();:*/\|<>-_%&#№@+~—"«»^') for j in range(len(words))]
        for word in range(len(words2)):
            print('%s_%s' %(words2[word], len(words2[word])))


def main():
    text = open_and_read()
    sent = read_sentences(text)
    split_and_count(sent)


main()
