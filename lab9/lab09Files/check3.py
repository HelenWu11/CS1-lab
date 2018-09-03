from Date import *

f = open('birthdays.txt')
s = f.read().strip().split('\n')
for n in range(len(s)):
    s[n] = s[n].split(' ')
    s[n][0] = int(s[n][0])
    s[n][1] = int(s[n][1])
    s[n][2] = int(s[n][2])
    s[n] = Date(s[n][0],s[n][1],s[n][2])

'''
for n in s:
    print(n)
print()
'''

earliest = s[0]
latest = s[0]

for i in range(1,len(s)):
    if s[i].__lt__(earliest):
        earliest, latest = s[i], earliest
        
    else:
        if not s[i].__lt__(latest):
            latest = s[i]   

print("The earlest birthday:",earliest)
print("The latest birthday:",latest)
print()
'''
mn = dict()
for item in s:
    if item.month not in mn:
        mn[item.month] = 0
        mn[item.month] += 1
    elif item.month in mn:
        mn[item.month] += 1

print(mn)
for n in mn:
    if mn[n] == max(mn.values()):
        print("The name of the month that has the most birthdays:",month_names[int(n)])
    '''


