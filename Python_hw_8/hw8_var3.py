def read_file():
    f = open("words.csv", 'r', encoding = "utf-8")
    a = f.readlines()
    f.close()
    return(a)

def make_dict(a):
    words = {}
    for line in a:
        a2 = line.split(';')
        for i, h in enumerate(a2):
            a2[i] = h.strip()
        words[a2[1]] = a2[0]
    return words

def guess(dic):
    for noun in dic:
        print(dic[noun], '...')
        attempt = 0
        while attempt != len(dic[noun]):
            print('Осталось попыток: ', len(dic[noun]) - attempt )
            attempt += 1
            if input() == noun:
                print('Маладэц!')
                attempt = len(dic[noun])
            elif len(dic[noun]) - attempt == 0:
                print('Не угадал :(')

def main():
    text = read_file()
    words = make_dict(text)
    print(words)
    guess(words)

main()
                
            
    
