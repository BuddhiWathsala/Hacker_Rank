m, n = map(int, raw_input().strip().split(' '))

magazine = raw_input().strip().split(' ')

ransom = raw_input().strip().split(' ')

def ransom_note(mag,rans):
    flag=1
    
    common=list(set(mag) & set(rans))
    
    # ransTup=tuple(rans)
    # commonTup=tuple(common)
    
    if(len(common)!=len(rans)):
        flag=0
    else:
        hrans=0
        for i in rans:
            hrans+=hash(i)
            
        hcommon=0
        for j in common:
            hcommon+=hash(j)
            
        print(hrans)
        print(hcommon)
        
        if (hrans!=hcommon):
            flag=0
        else:
            for i in rans:
                if i not in common:
                    flag=0
    return flag


answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"

    
