file = open('wrpi.txt')
s = file.read()
string = s.strip().split('|')[1]
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
    return len(gw_set),gw_set

print(get_words(string))