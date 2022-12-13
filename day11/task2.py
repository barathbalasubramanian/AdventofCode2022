
my_file = open('data.txt','r')
data_move = my_file.read()

data_move = data_move.split('\n\n')

for i in range(len(data_move)) :
    data_move[i] = data_move[i].split('\n')

available_mon = []
items = []
item = []
operation= []
Test = []
true = []
false = []

for i in data_move :
    for each in i :
        if 'Monkey' in each :
            available_mon.append(each[7:8])

        elif 'Starting items' in each :
            item.append(each[18:])

        elif 'Operation' in each :
            operation.append(each[-5:])
        
        elif 'Test' in each :
            Test.append(each[-2:])

        elif 'true' in each :
            true.append(each[-1:])
        
        elif 'false' in each :
            false.append(each[-1:])
        
for i in item :
    i = i.strip()
    i = i.split(',')
    items.append(i)

sym = ['*','+']
operator,operand = [],[]
for i in operation :
    i = i.split(' ')
    operator.append(i[-2])
    operand.append(i[-1])

print("AVAILABLE MONKEY :" , available_mon)
print("Starting items   :" ,items)
print("Operator  :" , operator , 'Operand :' , operand)
print("Test   :" ,Test)
print('True :', true)
print('False : ', false)

monks = [0, 0, 0, 0, 0, 0, 0, 0]

# str into int type
test1 = []
for i in Test :
    i = int(i)
    test1.append(i)

# Finding LCM
lcm = 0
import math
def LCMofArray(a):
    global lcm
    lcm = a[0]
    for i in range(1,len(a)):
        lcm = lcm*a[i]//math.gcd(lcm, a[i])
    lcm = lcm

LCMofArray(test1)


def main() :
    global lcm

    for i in range(len(available_mon)) :
        to_remove = []
        for j in  items[i] :
            mult = 0

            if operand[i] == 'old' : 
                if operator[i] == '*' : mult = int ((int(j) * int(j)) % lcm)
                else : mult = int ((int(j) + int(j)) % 3)

            else :
                if operator[i] == '*' : mult = int ((int(j) * int(operand[i])) % lcm)
                else : mult = int ((int(j) + int(operand[i])) % lcm)

            if mult % int(Test[i]) == 0 :
                items[int(true[i])].append(mult)

            if mult % int(Test[i]) != 0 :
                items[int(false[i])].append(mult)
            
            to_remove.append([j,i])
            monks[i] += 1

        for i in to_remove :
            items[i[1]].remove(i[0])
                
for i in range(10000) :
    main()

monks.sort()
monks.reverse()
print(monks[0] * monks[1])