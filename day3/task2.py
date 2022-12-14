my_file = open('data.txt','r')
data = my_file.read()
data=data.split('\n')
start = 0 
end = 3
data_new = []
for i in range(len(data)//3):
    data_new.append(data[start:end])
    start += 3
    end += 3
sumation = 0
string = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(data_new)):
    data_new[i] = list((set(data_new[i][0]).intersection(set(data_new[i][1]))).intersection(set(data_new[i][2])))
    for j in data_new[i]:
        sumation += string.index(j)
print(sumation)

