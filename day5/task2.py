data = [[],['S','M','R','N','W','J','V','T'],['B','W','D','J','Q','P','C','V'],
        ['B','J','F','H','D','R','P'],['F','R','P','B','M','N','D'],['H', 'V', 'R', 'P', 'T', 'B'],['C', 'B', 'P', 'T'],['B', 'J', 'R', 'P', 'L'],['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W'],['L','S','G']]


my_file = open('data.txt','r')
data_move = my_file.read()
data_move=data_move.split('\n')
for i in range(len(data_move)):
    data_move[i] = data_move[i].split(' ')
    data_move[i].remove('move')
    data_move[i].remove('from')
    data_move[i].remove('to')
    data_move[i] = list(map(int,data_move[i]))

for i in data_move:
    data[i[2]] = data[i[2]]+data[i[1]][-i[0]:]
    data[i[1]] = data[i[1]][:-i[0]]
    
for i in range(len(data)):
    if i > 0 :
        print(data[i][-1], end='')
print()

# BRQWDBBJM