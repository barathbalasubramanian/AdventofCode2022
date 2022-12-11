# [T] [V]                     [W]    
# [V] [C] [P] [D]             [B]    
# [J] [P] [R] [N] [B]         [Z]    
# [W] [Q] [D] [M] [T]     [L] [T]    
# [N] [J] [H] [B] [P] [T] [P] [L]    
# [R] [D] [F] [P] [R] [P] [R] [S] [G]
# [M] [W] [J] [R] [V] [B] [J] [C] [S]
# [S] [B] [B] [F] [H] [C] [B] [N] [L]
#  1   2   3   4   5   6   7   8   9 

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
    for j in range(i[0]):
        data[i[2]].append(data[i[1]].pop())

for i in range(len(data)):
    if i > 0 :
        print(data[i][-1], end='')
print()
