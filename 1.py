# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#1에서 7번까지의  정점
# 진출차수 몇개의 정점에 도착하게 되는지 가로로 더함
# 진입차수 세로로 더하면 그 정점에 진입하는 갯수

#인접행렬
# V,E =map(int,input().split())
# arr = list(map(int,input().split()))
# adjm = [[0]*(V+1) for _ in range(V+1) ]
# for i in range(E):
#     n1,n2 =arr[i*2],arr[i*2+1]
#     adjm[n1][n2] = 1
#     adjm[n2][n1] = 1 #방향이 없다면 둘다 연결
#
# print()

#인접리스트
# V,E =map(int,input().split())
# arr = list(map(int,input().split()))
# adjl = [[] for _ in range(V+1)]
# for i in range(E):
#     n1,n2 =arr[i*2],arr[i*2+1]
#     adjl[n1].append(n2)
#     adjl[n2].append(n1)
#
# print()


# 재귀나 스택으로 지나온것중 가장 가까운것을 꺼낼수있음
def dfs1(i,k): #중복없이 빠짐없이
    visited[i] = 1 #중복방지용
    print(i)
    for w in adjl[v]: #v와 인접하고
        if visited[w]==0: # 방문한적이 없는 w가 있음년
            dfs1(w,k)

    # for w in range(1,k+1):
    #     if adjm[v][w]==1 and visited[w]==0:
    #         dfs1(w,k)
def dfs2(s,k):
    stack = []
    visited = [0]*(k+1)
    v = s
    while True:
        if visited[v]==0:
            print(v)
            visited[v]= 1
        for w in range(1,k+1):
            if adjm[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break
                #갈 수 있는 곳이 있을때
        else: #더 이상 인접인 정점이 없으면
            if stack: #스택이 비어있지 않으면
                v = stack.pop()
            else: #스택이 비어있으면
                break

    return


def dfs3(v,k,g):
    global cnt
    if v==g:
        cnt += 1
    else:
        visited[i] = 1  # 중복방지용
        for w in range(1,k+1):  # v와 인접하고
            if adjm[v][w]==1 and visited[w]==0:  # 방문한적이 없는 w가 있음년
                dfs3(w, k,g)


V,E =map(int,input().split())
arr = list(map(int,input().split()))
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1,n2 =arr[i*2],arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)

print()


visited = [0]*(v+1) #중복방문 방지
cnt = 0
dfs2(1,V,7)
