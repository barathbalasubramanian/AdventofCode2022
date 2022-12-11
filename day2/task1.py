my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(' ')
symbols = {'X':1,'Y':2,'Z':3}
winning = [['A','Y'],['B','Z'],['C','X']]
lossing = [['A','Z'],['B','X'],['C','Y']]
sumation = 0 
for  i in data:
    if i in winning:
        add  = 6 + symbols[i[1]]
        sumation += add
    elif i in lossing:
        add = 0 + symbols[i[1]]
        sumation += add
    else:
        add = 3 + symbols[i[1]]
        sumation += add
print(sumation)