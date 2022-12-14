my_file = open('data.txt','r')
data = my_file.read()

for i in range(len(data)):

    if len(set(data[i:i+4]))  == 4 :
        print(i+4)
        break


