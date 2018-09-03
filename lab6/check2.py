bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

nl = bd.copy()
for n in range(len(nl)):
    nl[n] = bd[n].copy()
    for number in range(0,len(nl[n]),4):
        nl[n].insert(number,'|')
    nl[n] = ' '.join(nl[n])
    nl[n] = str(nl[n])+' '+'|'
    if n==0:
        print('-'*(len(nl[n])))    
    print(nl[n])
    if (n+1)%3==0:
        print('-'*(len(nl[n])))
print()

number = int(input("number: "))
row = int(input("row: "))
column = int(input("column: "))
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
        
    for item in three:
        for n in item:
            if str(number) == n:
                return 'number exist in the same 3X3 block'
            
    if bd[row][column] != '.':
        return 'spots has been taken'
    elif bd[row][column] == '.':
        bd[row][column] = bd[row][column].replace('.',str(number))
        
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

        return ''.join('\n'.join(bd2)) 
    
    
         
print(ok_to_add(number,row,column))
    


        
        
        
