#깊이 우선탐색으로 2랑연결된거를 다 타고 내려가서 조사해봄
#조사결과 최소값 출력
#못가면 0 출력


from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def solve(x,y,cnt):
    for row in range(N):
        for col in range(N):
            if  arr[row][col] == 3 :
                r = row
                c = col
            if arr[row][col] == 2:
                r2 = row
                c2 = col

    Q = deque()
    Q.append((r2,c2))


    while Q:
        x,y= Q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx<N and 0<=ny<N :
                if arr[nx][ny]==0:
                    solve(nx,ny,cnt+1)
                if arr[nx][ny]==3:
                    return cnt
                # arr[nx][ny] = arr[x][y] +1
                # Q.append((nx,ny))
    return arr[r][c]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)] #2차원의 visited배열


    ans = solve(0,0)

    print(f'#{tc} {ans}')