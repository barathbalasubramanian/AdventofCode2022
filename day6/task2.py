my_file = open('data.txt','r')
data = my_file.read()

for i in range(len(data)):

    if len(set(data[i:i+14]))  == 14 :
        print(i+14)
        break


