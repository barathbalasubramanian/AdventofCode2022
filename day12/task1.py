my_file = open('text.txt','r')
data_move = my_file.read()
data_move = data_move.split('\n')

import sys
sys.setrecursionlimit(10**3)

line = []
for i in data_move :
    letter = []
    for j in i :
        letter.append(j)
    line.append(letter)

starting = 'S'
ending = 'z'
start = []
# visited = [[17, 133],[5, 123],[34, 119],[35, 122],[35, 123],[36,125],[0,32],[8,36],[13,40],[0,56],[0,55],[0,54],[1,52],[2,52],[2,53],[1,53],[0,53],[0,52],[0,51],[0,50],[2,48],[1,45],[3,55],[10,60],[1,98],[5,102],[0,137],[18,137],[19,137],[20,137],[23,137],[22,135],[23,135],[24,134],[26,132],[27,132],[30,131],[32,130]] 
steps = 0
visited = []
path = 'SabcdefghijklmnopqrstuvwxyzE'

# lookup = [['   ' for _ in range(len(line[0]))] for _ in range(len(line))]

for index, i in enumerate(line) :
    if starting in i :
        start.append([index,i.index(starting)])
        visited.append([index,i.index(starting)])

# def backtrack(possible) :
#     global visited 
#     print('backtracing',possible)
#     line[possible[0][0]][possible[0][1]] = '1'
#     visited.pop()
#     return visited

def main() :
    global path,starting,ending,start,visited,possible, steps
    try:
        possible = []
        curr_pos = visited[-1]
        print(curr_pos)
        # lookup[curr_pos[0]][curr_pos[1]] = str(steps).zfill(3)
        steps += 1
        x , y = curr_pos[0] , curr_pos[1]
        
        # up
        if x-1 >= 0 :
            if [x-1,y] not in visited : possible.append([x-1,y])

        # right  
        if y+1 < len(line[0]) :
            if [x,y+1] not in visited : possible.append([x,y+1])

        # down
        if x+1 < len(line) :
            if [x+1,y] not in visited : possible.append([x+1,y])

        # left
        if  y - 1 >= 0 :
            if [x,y-1] not in visited : possible.append([x,y-1])

        # print(possible)

        # if len(possible) == 0 :
        #     visited = backtrack(possible)
        #     curr_pos = visited[-1]

        for i in possible :
            pos_vertex = line[i[0]][i[1]] 
            req_vertex = path.index(starting)

            if pos_vertex == path[req_vertex + 1]:
                starting = pos_vertex
                if starting == ending :
                    visited.append([i[0],i[1]])
                    return
                visited.append([i[0],i[1]])
                break

            elif  pos_vertex == path[req_vertex]:
                starting = pos_vertex
                if starting == ending :
                    visited.append([i[0],i[1]])
                    return
                visited.append([i[0],i[1]])
                break
        
        main()
    except RecursionError:
        # for i in lookup:
        #     print(" ".join(i))
        st = visited[-1]
        visited[0].append(st)
        # main()
        print(len(visited))

main()


