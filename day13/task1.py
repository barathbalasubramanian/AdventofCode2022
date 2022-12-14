data_ = open('text.txt')
data_ = data_.read()
data_ = data_.split('\n\n')

data = []
for i in data_ :
    i = i.split('\n')
    data.append([eval(k) for k in i])

# checking parallel
def check(left,right) :
    global value

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

count = 0
for index , pair in enumerate(data) :
    
    value = check(pair[0],pair[1])
    print(value)
    
    if value < 0 :
        print('-----',value)
        count += index + 1

print(count)

