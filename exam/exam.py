import re
import os

def task1():
    for root, dirs, files in os.walk('.\\news'):
        s = ''
        for f in files:
            file = open(os.path.join(root, f), 'r', encoding = "WINDOWS-1251")
            text = file.readlines()
            words = 0
            for line in text:
                reg = '<w>'
                r = re.search(reg,line)
                if r:
                    words += 1
            s += f + '\t' + str(words) + '\n'
    f2 = open("words_in_files.txt", 'w', encoding = "utf-8")
    f2.write(s)

def task2():
    for root, dirs, files in os.walk('.\\news'):
        s = ''
        for f in files:
            file = open(os.path.join(root, f), 'r', encoding = "WINDOWS-1251")
            text = file.readlines()
            author = ''
            date = ''
            for line in text:
                reg_author = 'content="([ |(а-яА-яa-zA-Z)]+)" name="author"'
                reg_date = 'content="([0-9]+\.[0-9]+\.[0-9]+)" name="created"'
                r1 = re.search(reg_author, line)
                if r1:
                    author = r1.group(1)
                r2 = re.search(reg_date, line)
                if r2:
                    date = r2.group(1)
            s += f + '\t' + author + '\t' + date + '\n'
    f3 = open("words_in_files.csv", 'w', encoding = "utf-8")
    f3.write(s)

def task3():
    for root, dirs, files in os.walk('.\\news'):
        s = ''
        for f in files:
            file = open(os.path.join(root, f), 'r', encoding = "WINDOWS-1251")
            text = file.readlines()
            for i, line in enumerate(text):
                reg_adj = 'A=.+gen.+>?'
                reg_sumj = 'S,.+gen.+>?'
                reg_word = '([а-яА-Я]+|`)\n</w>'
                r1 = re.search(reg_adj, line)
                if r1:
                    r2 = re.search(reg_word, line)
                    word1 = r2.group(1)
                    r3 = re.search(reg_subj, text[i+1])
                    if r3:
                        word2 = r3.group(1)
                

def main():
    task1()
    task2()

main()
