
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

for i in range(4) :
    for index,j in enumerate( items[i] ):
        mult = 0

        if operand[i] == 'old' : 
            if operator[i] == '*' : mult = int ((int(j) * int(j)) / 3)
            else : mult = int ((int(j) + int(j)) / 3)

        else :
            if operator[i] == '*' : mult = int ((int(j) * int(operand[i])) / 3)
            else : mult = int ((int(j) + int(operand[i])) / 3)

        print(f'{int(j)}  {operator[i]} with {operand[i]} gives {mult}')

        if mult % int(Test[i]) == 0 :
            # print(int(true[i]))
            items[int(true[i])].append(mult)

        if mult % int(Test[i]) != 0 :
            # print(int(false[i]))
            items[int(false[i])].append(mult)
        
print("Starting items   :" , items)

