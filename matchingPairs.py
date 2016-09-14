class node:
    def __init__(self,data):
        self.data=data
        self.next=None
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mainList=[]
input1=int(input())
for i in range(input1):
    input2=str(input())
    l=[str(i) for i in input2]
    mainList.append(l)
    print(mainList)
count=0

for i in range(len(mainList)-1):
    temp1=mainList.pop(0)
    c=0
    
    while c!=(len(mainList)):
        count=count+1
        l=[]
        for h in range(26):
            l.append(None)
        
          temp2=mainList[c]
        
        if len(temp1)==len(temp2):
              
            for j in range(len(temp1)):
                
                if l[n]==None and l[m]==None:
                        
                    if temp1[j]!=temp2[j]:
                        temp_m=node(m)
                        temp_n=node(n)
                        l[n]=(temp_m)
                        l[m]=(temp_n)
                    elif temp1[j]==temp2[j]:
                        temp_m=node(m)
                        temp_n=node(n)
                        l[n]=(temp_m)
                        l[m]=(temp_n)
                elif l[n]==None and l[m]!=None :
                    count=count-1
                    break
                    
                elif l[n]!=None :
                    v=l[n]
                    w=l[m]
                    
                    if v.data!=m:
                        count=count-1
                        break
                    elif w.data!=n:
                        count=count-1
                        break
            
            c=c+1               
    
print(count)
