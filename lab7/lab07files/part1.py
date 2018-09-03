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
        
print(parse_line(" Here is some spaces 12/32/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4"))
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Again some spaces\n/12/12/12"))
