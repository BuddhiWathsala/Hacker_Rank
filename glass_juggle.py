l=[]
n=int(input())
if n>=3 and n<=20:
    for i in range(n):
        l.append(int(input()))
l.sort()
sort=[]
for j in range(len(l)):
    sort.append(None)


def place(ll):
    if ll%2==0:
        p=int((ll//2))
        return p
    elif ll%2==1:
        p=int((ll/2)+0.5)
        return p
length=len(l)
k=place(length)

def function(a,b):
    func=a+b
    return func

t=int(k-1)
temp=l.pop()
sort[t]=temp

gap=1    
while len(l)!=0:
    f=function(t,-gap)
    for i in range(2):
        if len(l)==0:
            break
        temp1=l.pop()
        if sort[f]==None :
            sort[f]=temp1
        elif sort[f]!=None:
            f=function(t,gap)
            sort[f]=temp1
    gap=gap+1

indx=len(sort)-1
ex=sort[0]-sort[indx]
for i in range(indx):
    result=sort[i]-sort[i+1]
    if result<0 and(-result)>ex:
        ex=-result   
    elif result>0 and(result)>ex:
        ex=result
    
    
print(ex)









