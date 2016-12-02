f = open("1.txt", 'r', encoding = "utf-8")
word1 = 0
word3 = 0
for line in f:
    words = line.split()
    for i in range(len(words)):
        if len(words[i]) == 3:
            word3 += 1
        elif len(words[i]) == 1:
            word1 += 1
    words = []
if word1 == 0:
    print("Нет слов длинны 1")
else:
    print(float(word3)/float(word1))
    
