import sys
from collections import deque, defaultdict

input = sys.stdin.read
data = input().split()

N, M, V = int(data[0]), int(data[1]), int(data[2])  # 정점의 개수 # 간선의 개수 # 탐색을 시작할 정점 번호

graph = defaultdict(list)

index = 3 # n, m, v 빠지니까 index 3부터
for _ in range(M):
    s = int(data[index])
    e = int(data[index + 1])
    index += 2
    if e not in graph[s]:
        graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)

# 각 노드에 연결된 노드들을 정렬
for key in graph:
    graph[key].sort()

# DFS 구현
def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))  
            # 번호가 작은 것부터 방문하기 위해 역순으로 push
    
    return visited

# BFS 구현
def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])  
            # 이미 정렬된 상태이므로 그대로 사용
    return visited

dfs_result = dfs(graph, V)
bfs_result = bfs(graph, V)

# 결과 출력
print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))
