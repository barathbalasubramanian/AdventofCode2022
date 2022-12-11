my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')
for i in range(len(data)):
    data[i] = data[i].split(' ')
symbols = {'X':1,'Y':2,'Z':3}
draw = {'A':'X','B':'Y','C':'Z'}
winning = {'A':'Y','B':'Z','C':'X'}
lossing = {'A':'Z','B':'X','C':'Y'}

summation = 0
for i in data:
    if i[1] == 'X':
        add = 0 +  symbols[lossing[i[0]]]
    elif i[1] == 'Y':
        add = 3 + symbols[draw[i[0]]]
    elif i[1] == 'Z':
        add = 6 + symbols[winning[i[0]]]
    summation += add
print(summation)
    
