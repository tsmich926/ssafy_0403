from collections import deque

def bfs(s):
    # Q = []
    Q = deque()
    Q.append((s, 1))  #큐에 처음시작하는 수넣고 횟수1부터 시작
    # visited[s] = True

    while Q:
        v, cnt =Q.popleft() #노드에 적용된 값이랑 횟수가 튀어나오도록 한다
        # v, cnt = Q.pop(0)
        for w in [v*2, v-10, v+1, v-1]: #for문돌면서 차례로 계산하도록
            if w == M: #만약 계산 값이 M 원하는 값이면 cnt를 반환한다
                return cnt
 
            if 0 < w <= 1000000: #문제에서 백만 이하의 수라고 했으니깐..
                if not visited[w]: #visited배열을 안썼더니 계속 시간초과남...
                    visited[w] = True
                    Q.append((w, cnt+1)) #cnt+1을 여기서 하니까 1부터 시작 while 바로 다음부터 하면 2번하는 효과...


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    visited = [False]*1000001

    ans = bfs(N)

    print(f'#{tc} {ans}')




# def bfs(s,cnt):
#     Q = []
#     Q.append((s, 0))
#     visited[s] = True
#     while Q:
#         v, cnt =Q.pop(0)
#         if v == M:
#             return cnt
#         Q.append((v+1, cnt+1))
#         Q.append((v-1, cnt+1))
#         Q.append((v*2, cnt+1))
#         Q.append((v-10, cnt+1))
#
#         # for w in G[v]:
#             # if not visited[w]:
#             #     Q.append(w)
#                 # visited[w] =True
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     visited = [False]*1000000
#
#     ans = bfs(N,0)
#
#     print(f'{tc} {ans}')





