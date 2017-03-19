import sys
in1 = raw_input()
in2 = raw_input()
in3 = raw_input()
in4 = raw_input()
in5 = raw_input()

input_lst = in1.split()

operends1 = list(in2.strip())
operends2 = list(in3.strip())
operends2 = operends2[1:]
operends2 = (filter(lambda a:a != ' ',operends2))


base = int(input_lst[0])
symbols = list(input_lst[1])
numbers = []
for i in range(len(symbols)):
    numbers.append(i)

op1 = []
op2 = []
for i in operends1:
    op1.append(symbols.index(i))
for i in operends2:
    op2.append(symbols.index(i))


##print(op1)
##print(op2)
l1 = len(operends1)
l2 = len(operends2)
##print(l1,l2)
answer = []
if(l1 < l2):
    j = l2 -1
    rem = 0
    for i in range(l1-1,-1,-1):
        temp = op1[i] + op2[j] + rem
        j-=1
        
        if(temp>= base):
            
            answer.append(temp%base)
            rem = temp / base
        else:
            answer.append(temp)
            rem = 0
    op2[j] = op2[j]+rem
    answer.reverse()
    answer = op2[0:j+1]+answer
else:
    j = l1 -1
    rem = 0
    for i in range(l2-1,-1,-1):
        temp = op1[j] + op2[i] + rem
        j-=1
        #print(temp)
        if(temp>= base):
            #print(symbols[temp%base])
            answer.append(temp%base)
            rem = temp / base
        else:
            answer.append(temp)
            rem = 0
            
    
    op1[j] = op1[j]+rem
    answer.reverse()
    answer = op1[0:j+1]+answer
#print(answer)
full = []
for i in answer:
    full.append(symbols[i])
    
print(in1)
print(in2)
print(in3)
print(in4)
#print(full)
sys.stdout.write(" ")
for i in full:
    sys.stdout.write(i)
            
        
        



