# opening the file in read mode
my_file = open("data.txt", "r")

# reading the file
data = my_file.read()

data_into_list = data.replace('\n\n', ',')
data_fin = data_into_list.replace('\n', '/')
data_fin = data_fin.split(',')
for i in range(len(data_fin)):
    data_fin[i] = data_fin[i].split('/',)
    data_fin[i] = list(map(int,data_fin[i]))

elf = []
for index,value in enumerate(data_fin):
    calories = sum(value)
    elf.append(calories)

p = sorted(elf)[::-1]

# task 1
print(p[0])

# task 2
print(sum(p[:3]))
