
n,d=raw_input().split()

arry=[int(x) for x in raw_input().split()]

if(len(arry)== int(n)):

    for i in range(int(d)):
        temp=arry.pop(0)
        arry.append(temp)
    
    sarry=[str(a) for a in arry]    
    print(" " . join(sarry))
