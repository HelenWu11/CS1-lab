def get_words(string):
    gw_set = set()
    string = string.replace('.',' ')
    string = string.replace(',',' ')
    string = string.replace('()',' ')
    string = string.replace('"',' ')
    string = string = string.split(' ')
    for word in string:
        if word.isalpha() and len(word)>=4:
            word = word.lower()
            gw_set.add(word)
    return gw_set

file1 = 'csa.txt'
file = open(file1, encoding="utf8")
s = file.read()
string1 = s.strip().split('|')[1]
file.close()

s1 = get_words(string1)

similarity = []
for line in open('allclubs.txt', encoding="utf8"):
    line = line.strip().split('|')
    if line[1] != string1:
        s2 = get_words(line[1])
        similarity.append((len(s1&s2),line[0]))

similarity.sort(reverse=True)
for n in range(0,6):
    print(similarity[n][1])
        



