def bfs(g, d, s):
    q = [s]
    while len(q) != 0:
        v = q.pop(0)
        for i in range(len(g[v])):
            #print g[v], i
            if d[g[v][i]] == -1:
                d[g[v][i]] = d[v]+6
                q.append(g[v][i])
    return d

t = int(raw_input())
for x in range(t):
    graph = {}
    n, m = map(int, raw_input().split())
    distance = [-1]*(n+1)
    for y in range(m):
        i, j = map(int, raw_input().split())
        try:
            graph[i].append(j)
            
        except:
            graph[i] = [j]
        try:
            graph[j].append(i)
        except:
            graph[j] = [i]
    for node in range(1, n):
        if node not in graph:
            graph[node] = []
    #print graph
    end = int(raw_input())
    distance[end] = 0
    ans = bfs(graph, distance, end)[1:]
    #print ans
    final = []
    for i in range(len(ans)):
        if i+1 != end:
            final.append(ans[i])
    print " ".join(map(str, final))
