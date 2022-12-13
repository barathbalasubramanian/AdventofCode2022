data  = open('data.txt' )
data  = data.read()
data=data.split('\n')

data = [[int(data) for data in line] for line in data]


right_count = {}
left_count = {}
top_count = {}
btm_count = {}

for line in range(1,len(data)-1) :
    for c_data in range(1,len(data[line])-1) :

        x,y = line,c_data

        # right checking    
        r_count = 0
        i = 1
        while True :
            if y + i == len(data):
                break
            if data[x][y] <= data[x][y+i]:
                r_count += 1
                break
            if data[x][y] > data[x][y+i]:
                i += 1
                r_count += 1

        right_count[(x,y)] = r_count

        i = -1
        l_count = 0
        while True :
            if y + i == -1 :
                break
            if data[x][y] <= data[x][y+i]:
                l_count += 1
                break
            if data[x][y] > data[x][y+i]:
                i -= 1
                l_count += 1
            
        left_count[(x,y)] = l_count

        b_count = 0
        i = 1
        while True :
            if x + i == len(data):
                break
            if data[x][y] <= data[x+i][y]:
                b_count += 1
                break
            if data[x][y] > data[x+i][y]:
                i += 1
                b_count += 1

        btm_count[(x,y)] = b_count


        t_count = 0
        i = -1

        while True :
            if x + i == -1:
                break
            if data[x][y] <= data[x+i][y]:
                t_count += 1
                break
            if data[x][y] > data[x+i][y]:
                i -= 1
                t_count += 1

        top_count[(x,y)] = t_count

value = 0
for i in top_count.keys() :

    value = max(right_count[i] * left_count[i] * top_count[i] * btm_count[i] , value)

print(value)

