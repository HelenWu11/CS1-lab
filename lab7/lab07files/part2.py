def parse_line(line):
    if line.count('/')<3:
        return None
    elif line.count('/')>=3:
        new_line = line.split('/')
        if not new_line[-1].isdigit() or \
           not new_line[-2].isdigit() or \
           not new_line[-3].isdigit():
            return None
        else:
            line_list = []
            line_list.append(new_line[-3])
            line_list.append(new_line[-2])
            line_list.append(new_line[-1])
            new_line.pop()
            new_line.pop()
            new_line.pop()
            reline = ''
            reline = '/'.join(new_line)
            return (line_list[0],line_list[1],line_list[2],reline)
        
        
        
filenumber = int(input("Please enter the file number ==> "))
paranumber = int(input("Please enter the paragraph number ==> "))
linenumber = int(input("Please enter the line number ==> "))
def get_line(fname,parno,lineno):
    f = open(str(filenumber)+'.txt')
    s = f.read().rstrip()
    s_list = s.split('\n\n')
    line_list = s_list[parno-1].strip().split('\n')
    print(line_list[lineno-1])
    
    
get_line(filenumber,paranumber,linenumber)   