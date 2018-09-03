file1 = 'wrpi.txt'
file = open(file1)
s = file.read()
string1 = s.strip().split('|')[1]
file.close()

file2 = 'csa.txt'
file = open(file2)
s = file.read()
string2 = s.strip().split('|')[1]
file.close()

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

print('Comparing clubs wrpi and csa: ')
s1 = get_words(string1)
s2 = get_words(string2)
print('Same words:',s1 & s2)
print('Unique to wrpi:', s1 - s2)
print('Unique to csa:', s2 - s1)

