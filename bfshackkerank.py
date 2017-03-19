testCase=input()
vertices_edges=str(input()).split()
ver=int(vertices_edges[0])
ed=int(vertices_edges[1])
adj_matrix=[]

for i in range(ver):
    l=[]
    adj_matrix.append(l)
    for j in range(ver):
        l.append(0)
   
for n in range(0,ed):
    v=str(input()).split()
    snode=(int(v[0]))-1
    enode=(int(v[1]))-1
    adj_matrix[snode][enode]=1    
s=int(input())
result=[]

def BFS(g,v1):
    
    for i in range(len(g)):
        if(g[v1-1][i]==1):
            result.append(6)
            
        elif(g[v1-1][i]==0):
            if (v1-1)!=i:
                result.append(-1)
            v0=g[i]
            for v in range(0,len(v0)):
                if(g[i][v]==1) and g[v][v1-1]==1:
                    result[i]=12
    
    print(" ".join(str(x) for x in result))             
                    

BFS(adj_matrix,s)
