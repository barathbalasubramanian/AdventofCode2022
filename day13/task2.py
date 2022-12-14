
data_ = open('text.txt')
data_ = data_.read()
data_ = data_.split('\n')

data = []
for i in data_ :
    if i == '' :
        continue
    data.append([eval(i), 0])


# checking parallel
def check(left,right) :

    if type(left) == int :
        if type(right) == int :
            return left - right
        else :
            return check([left],right)

    elif type(right) == int :
        return check(left,[right])

    for l,r in zip(left,right) :
        v = check(l,r)        
        if v :
            return v

    return len(left) - len(right) 

data.append([[[2]], 0])
data.append([[[6]], 0])
final = [0 for _ in range(len(data))]


for ind, i in enumerate(data) :
    for j in data :
        if i != j :
            if check(i,j) < 0:
                data[ind][-1] += 1

data.sort(key = lambda x : x[-1])
data.reverse()

solution = 1

for ind, i in enumerate(data):
    if i[0] == [[2]] or i[0] == [[6]]:
        solution *= ind + 1

print(solution)
