line = ''
for n in range(9):
    line = line+str(n)+' '
    
row_list = []
for n in line:
    if n != ' ':
        new_line = ''
        for i in range(9):
            new_line += n+','+str(i)+' '
        row_list.append(new_line)

column_list = []
for n in range(9):
    new_line = ''
    for small_list in row_list:
        new_line = new_line+small_list.split(' ')[n]+' '
    column_list.append(new_line)

print(row_list)    
print()
row = int(input("row = "))
print(row_list[row])
column = int(input("column = "))
print(column_list[column])

def ok_to_add(number,row,column):
    for n in bd[row]:
        if n == str(number):
            return 'number exist in the same row'

    for n in bd:
        if n[column] == str(number):
            return 'number exist in the same column'
    
    truerow = row//3
    truecolumn = column//3
    three = []
    n_n = truerow*3
    while n_n<(truerow*3+3):
        line = ''
        for n in range(truecolumn*3,truecolumn*3+3):
            line = line+bd[n_n][n]
        three.append(line)
        n_n+=1

