import sys

input = sys.stdin.read().split()

N, M = int(input[0]), int(input[1])

edges = []
idx = 2
for _ in range(M):
    edges.append((int(input[idx]), int(input[idx+1])))
    idx += 2

def dfs(v, visited, adj):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

adj = [[] for _ in range(N + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)
connected_components = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, visited, adj)
        connected_components += 1  # 새 연결 요소 발견

print(connected_components)