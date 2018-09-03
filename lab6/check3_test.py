from lab06_util import read_sudoku

filename = input("File name: ")

nl = read_sudoku(filename).copy()
for n in range(len(nl)):
    nl[n] = read_sudoku(filename)[n].copy()
    for number in range(0,len(nl[n]),4):
        nl[n].insert(number,'|')
    nl[n] = ' '.join(nl[n])
    nl[n] = str(nl[n])+' '+'|'
    if n==0:
        print('-'*(len(nl[n])))    
    print(nl[n])
    if (n+1)%3==0:
        print('-'*(len(nl[n])))

def ok_to_add(board):
    bd = board.copy()
    row = 0
    column = 0
    while row<len(bd) and column<len(bd):
        for n in bd[row]:
            if bd[row].count(n)>1:
                print('number exist in the same row')
                print(bd[row])
                new = str(input("input: "))
                bd[row].insert(bd[row].index(n),new)
                bd[row].remove(n)
            
        column_list = []
        for n in bd:
            column_list.append(n[column])
        if column_list.count(n)>1:
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
            
        for item in three:
            if item.count(str(n))>1:
                return 'number exist in the same 3X3 block'
        row+=1
        column+=1
        
    bd2 = []
    for n in range(len(bd)):
        for number in range(0,len(bd[n]),4):
            bd[n].insert(number,'|')
        bd[n] = ' '.join(bd[n])
        bd[n] = str(bd[n])+' '+'|'
        if n==0:
            bd2.append('-'*(len(bd[n])))    
        bd2.append(bd[n])
        if (n+1)%3==0:
            bd2.append('-'*(len(nl[n]))) 
        ' '.join(bd2)

        #return ''.join('\n'.join(bd2)) 
    return True

def verify_board(board):
    for i in board:
        for n in range(len(i)):
            if i[n] == '.':
                print('Error:',i[n])
                new = str(input('input: '))
                i[n] = new
    if ok_to_add(board) != True:
        return ok_to_add(board)
    
    print ('valid')
    three = []
    nl = board.copy()
    for n in range(len(nl)):
        for number in range(0,len(nl[n]),4):
            nl[n] = nl[n]
        nl[n] = ' '.join(nl[n])
        nl[n] = str(nl[n])+' '+'|'
        if n==0:
            three.append('-'*(len(nl[n])))    
        three.append(nl[n])
        if (n+1)%3==0:
            three.append('-'*(len(nl[n])))

    return '\n'.join(three)
            
print(verify_board(read_sudoku(filename)))