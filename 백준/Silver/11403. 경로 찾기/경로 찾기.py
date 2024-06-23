import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            graph[i].append(j)

def dfs(graph, cur, target, visited, started):
    if cur == target and started:
        return 1
    visited[cur] = True
    for element in graph[cur]:
        if not visited[element] or (element == target and started):
            if dfs(graph, element, target, visited, True):
                return 1
    return 0

res = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        visited = [False] * N
        res[i][j] = dfs(graph, i, j, visited, False)

for p in res:
    print(*p)