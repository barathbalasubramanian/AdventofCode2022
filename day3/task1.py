
my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')

for i in range(len(data)):
    half = len(data[i])//2
    data[i] = [data[i][:half],data[i][half:]]

string = '0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

summation = 0 
for i in range(len(data)):
    data[i] = list(set(data[i][0]).intersection(set(data[i][1])))
for i in data:
    for j in i:
        summation += string.index(j)
print(summation)


