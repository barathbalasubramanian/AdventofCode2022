
my_file = open('data.txt','r')
data_move = my_file.read()
data_move = data_move.split('\n')

for i in range(len(data_move)) :
    data_move[i] = data_move[i].split(' ')

points = [20,60,100,140,180,220]
final = []

for point in points :
    count = [1]
    i = 0
    for data in data_move :
        if data[0] == 'addx' :
            i += 2
            if i >= point :
                break
            count.append(int(data[1]))

        if data[0] == 'noop' :
            i += 1

    final.append(point*sum(count))
print(sum(final))