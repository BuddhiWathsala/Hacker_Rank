a=list(raw_input().strip())
b=list(raw_input().strip())

la= len(a)
lb= len(b)

common=list(reversed(list( set(a) & set(b))))


comA=list()
for i in range(la):
    if(a[i] in common):
        comA.append(a[i])        

def match(s,com):
    c=0
    for j in range(len(s)):
        if(len(com)==0):
            break
        
        elif(s[0]!=com[0]):
            s.pop(0)
            
        elif(s[0]==com[0]):
            s.pop(0)
            com.pop(0)
            c+=1
    return c

count=0

for k in range(len(comA)):
    b1=b[:]
    comT=comA[:]

    for l in range(k):
        comT.pop(0)

    n=match(b1,comT)
    if(count<=n):
        count=n
        
   
print(la+lb-(2*count))