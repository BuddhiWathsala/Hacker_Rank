result_lst=[]
def swap(a,b,c):
    j=max(a,b,c)
    
    if((a>b>c) or(a==b==c)):
        j=a
        k=b
        l=c
    elif((a>c) and (c>b)):
        j=a
        k=c
        l=b
    elif((b>a>c)):
        j=b
        k=a
        l=c
    elif((b>c) and (c>a)):
        j=b
        k=c
        l=a
    elif(c>b>a):
        j=c
        k=b
        l=a
    elif((c>a) and (a>b)):
        j=c
        k=a
        l=b

    return(j,k,l)

def function(w,x,y,z):
    if (w<x):
        answer=w
        

    else:
        
        if (x>=(y+z)):
            answer=y+z
            
            

        elif(x<(y+z)):
            answer=((x+y+z)/2)
            if answer<=w:
               answer=int(((x+y+z)/2)) 
            else:
                answer=w
    result=answer
    result_lst.append(result)
    

days=int(input(""))
j=0
if (1<=days<=100):
    while (j<days):
        
        day1=(input(""))
        a=day1.split()
        if((0<=int(a[0])<=10**9) or (0<=int(a[1])<=10**9) or (0<int(a[2])<=10**9) or (0<=int(a[3])<=10**9)
           ):
            s=int(a[0])
            m=int(a[1])
            r=int(a[2])
            b=int(a[3])
            swap(m,r,b)
            function(s,m,r,b)
            
            
            j=j+1
    i=0            
    while(i<days):
        print(result_lst.pop(0))
        i=i+1

else:
    print("Your inputs are not valid")

       
    



    


    
