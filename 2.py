# G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
# #인접리스트
# visited = [0]*8
#
# dfs(1)

# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
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
dfs(1)