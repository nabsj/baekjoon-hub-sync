import sys
from collections import deque

input = list(map(int, sys.stdin.read().split()))

N, M = input[0], input[1] # N명, M개의 조건

in_degree = [0] * (N + 1)
in_degree[0] = -1
graph = [[] for _ in range(N+1)]

for i in range(M):
    A, B = input[(2 * i + 2)], input[(2 * i + 3)]
    in_degree[B] += 1
    graph[A].append(B)

#print(graph)

queue = deque()
for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    print(node,end=' ')
    for i in graph[node]:
        if in_degree[i] == 1:
            queue.append(i)
        in_degree[i] -= 1