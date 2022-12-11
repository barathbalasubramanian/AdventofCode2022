
my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')

for i in range (len(data)):
    data[i] = data[i].split(',')
    data[i][0] = data[i][0].split('-')
    data[i][1] = data[i][1].split('-')
    
summation  = 0

for i in range(len(data)) :
    if int(data[i][0][0]) <= int(data[i][1][0]) and int(data[i][0][1]) >= int(data[i][1][1] ) :
        summation += 1
    elif int(data[i][0][0]) >= int(data[i][1][0]) and int(data[i][0][1]) <= int(data[i][1][1] ) :
        summation += 1
    
print(summation)
