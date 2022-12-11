
my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')

for i in range (len(data)):
    data[i] = data[i].split(',')
    data[i][0] = data[i][0].split('-')
    data[i][1] = data[i][1].split('-')

summation  = 0

for i in range(len(data)):
    data[i][0] = set(range(int(data[i][0][0]), int(data[i][0][1])+1))
    data[i][1] = set(range(int(data[i][1][0]), int(data[i][1][1])+1))
    get = data[i][0].intersection(data[i][1])
    
    if len(list(get)) >= 1:
        summation += 1
        
print(summation)

   




