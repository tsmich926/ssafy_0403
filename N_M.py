#조합

N,M = map(int,input().split())
nums = list(map(int,input().split()))
n = len(nums)
# l = [1, 2, 3, 4]
# n = len(l)
# r = 2
answer = []

def dfs(idx, list):
    if len(list) == M:
        answer.append(list[:])
        return

    for i in range(idx, n):
        dfs(i+1,list+[nums[i]])

dfs(0, [])
print(*answer)