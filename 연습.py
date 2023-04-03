# from collections import deque
#
# def bfs(num, cnt):
#     global res
#     q = deque()
#     q.append((num, cnt))
#
#     while q:
#         num, cnt = q.popleft()
#         visited[num] = 1
#         if num == M:
#             res = cnt
#             return res
#             break
#         else:
#             lst = [num * 2, num - 10, num + 1, num - 1]
#             for n in lst:
#                 if 0 < n <= 1000000 and visited[n] == 0:
#                     visited[n] = 1
#                     q.append((n, cnt + 1))
#
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     visited = [0] * 1000001
#     res = 0
#     print(f'#{tc} {bfs(N, 0)}')