data  = open('data.txt' )
data  = data.read()
data=data.split('\n')

w_left_list = []
w_top_list = []

for i in data :
    data_list = []
    for j in i :
        data_list.append(int(j))
    w_left_list.append(data_list)

for i in range(len(data)):
    top_list = []
    for j in range(len(data[i])) :
        top_list.append(data[j][i])
    w_top_list.append(top_list)

#---------- checking visiblity towards right

visited = []
row = 0
for i in w_left_list :

    max = i[0]
    for j in range(1,len(i)-1) :
        if max < i[j] :
            if row != 0 and row != len(w_left_list)- 1:
                visited.append([row,j])
            max = i[j]
    row += 1


row = 0
for i in w_left_list :
    rev = list(reversed(i))
    max = rev[0]
    col = 97
    for j in range(1,len(rev)-1) :
        if max < rev[j] :
            if row != 0 and row != len(w_left_list) - 1 :
                if [row,col] not in visited :
                    visited.append([row,col])
            max = rev[j]
        col -= 1
    row += 1


row = 0
for i in w_top_list :
    max = i[0]
    col = 1
    for j in range(1,len(i)-1) :
        if max < i[j] :
            if row != 0 and row != len(w_top_list)- 1:
                if [col,row] not in visited :
                    visited.append([col,row])
            max = i[j]
        col += 1 
    row += 1


row = 0
for i in w_top_list :
    rev = list(reversed(i))
    max = rev[0]
    col = 97
    for j in range(1,len(rev)-1) :
        if max < rev[j] :
            if row != 0 and row != len(w_top_list) - 1 :
                if [col,row] not in visited :
                    visited.append([col,row])
            max = rev[j]
        col -= 1
    row += 1

grid = 99 + 99 + 97 + 97

print(len(visited) + grid)