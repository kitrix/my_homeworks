import re

def open_file():
    f = open("file.txt", 'r', encoding = "utf-8")
    a = []
    for line in f:
        a.append(line)
    f.close()
    return a


def open_new_file():
    f = open("created_file.txt", 'w', encoding = "utf-8")
    return f


def write_lines_number(a,f):
    i = 0
    for line in a:
        i += 1
    f.write(str(i))
    f.write('\n')
    

def create_dictionary(a,f):
    dic = {}
    for line in a:
        if '<w lemma=' in line:
            r = re.search('type="(.+?)"', line)
            key = r.group(1)
            if key not in dic:
                dic[key] = 1
            else:
                dic[key] += 1
    for key in sorted(dic):
        s = key + '\n'
        f.write(s)


def find_adj(a):
    reg = 'type="l[a-z]f[a-z]*?"'
    freq = {}
    for line in a:
        if '<w lemma=' in line:
            if re.search(reg, line):
                r = re.search(reg, line)
                key = r.group()
                if key not in freq:
                    freq[key] = 1
                else:
                    freq[key] += 1
    f = open("freq.txt", 'w', encoding = "utf-8")
    for key in sorted(freq):
        s = key + ' ' + str(freq[key]) + '\n'
        f.write(s)
    f.close()


def main():
    text = open_file()
    f = open_new_file()
    write_lines_number(text,f)
    create_dictionary(text,f)
    f.close()
    find_adj(text)
    
            
    

main()
    

        

