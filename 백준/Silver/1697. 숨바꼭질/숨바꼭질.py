from collections import deque

n, k = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)

def bfs(s, d):
    q = deque()
    q.append(s)

    while q:
        x = q.popleft()
        
        if x == d:
            return visited[k]
        
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= MAX and not visited[i]: 
                visited[i] = visited[x] + 1
                q.append(i)

print(bfs(n, k))