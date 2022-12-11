my_file = open('data.txt','r')
data_move = my_file.read()
data_move = data_move.split('\n')

for i in range(len(data_move)) :
    data_move[i] = data_move[i].split(' ')

cycle = 0
pos = 0
crt = ''
crts = []

def checking () :
    global crt, pos, cycle
    if pos <= cycle <= pos + 2:
        crt += '#'
    else:
        crt += ' '

    if len(crt) == 40: 
        crts.append(crt)
        crt = ''
        pos += 40

for i in range(len(data_move)) :
    if data_move[i][0] == 'addx' :

        checking () 
        cycle += 1

        checking () 
        cycle += 1

        pos += int(data_move[i][1])

    elif data_move[i][0] == 'noop' :

        checking () 
        cycle += 1

for c in crts:
    print(c)