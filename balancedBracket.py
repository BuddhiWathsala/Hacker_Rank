def is_matched(expression):
    
    flag=1
    
    stack=list()
    openBracket=['(','[','{']
    closeBracket=[')',']','}']
    dict={')':'(',']':'[','}':'{'}
    
    for i in expression:
        if(i in openBracket):
            stack.append(i)
            
        elif(i in closeBracket):
            if (len(stack)==0):
                flag=0
            else:
                bracket=stack.pop()
                if (dict[i]!=bracket):
                    flag=0
                    
    if(len(stack)!=0):
        flag=0
                    
    return flag
    
    #print (expression[0])

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
