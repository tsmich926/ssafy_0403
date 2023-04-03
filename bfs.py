def dfs(s):
    ST = []
    ST.append(s)
    visited[s] = True
    while ST:
        v =ST.pop(-1)
        print(v)
        for w in G[v]: #연결된 얘들은 스택에 넣음
            if not visited[w]:
                ST.append(w)
                visited[w] =True


def bfs(s):
    Q = []
    Q.append(s)
    visited[s]=True
    while Q:
        v=Q.pop(0)
        print(v)
    for w in G[v]:
        if not visited[w]:
            Q.append(w)
            visited[w] =True


def dfsr(v):
    visited[v]=True
    print(v)
    for w in G[v]:
        if not visited[w]: #방문안한경우에만
            dfsr(w)



V,E = map(int,input().split())
lst = list(map(int,input().split()))

G = [[] for _ in range(V+1)]
for idx in range(0,len(lst),2):
    v1 = lst[idx]
    v2 = lst[idx+1]
    G[v1].append(v2)
    G[v2].append(v1)

print(G)
visited = [False]*(V+1)
dfsr(1)