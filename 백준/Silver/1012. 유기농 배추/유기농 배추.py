from sys import stdin
from collections import deque

input = stdin.read

def bfs(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and cabbage_field[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))

def process_case():
    global m, n, cabbage_field, visited
    m, n, k = map(int, input().split())
    cabbage_field = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    worms_needed = 0

    for _ in range(k):
        x, y = map(int, input().split())
        cabbage_field[y][x] = True

    for i in range(n):
        for j in range(m):
            if cabbage_field[i][j] and not visited[i][j]:
                bfs(j, i)
                worms_needed += 1

    print(worms_needed)

# Read the input
data = input().split()
index = 0
t = int(data[index])
index += 1

for _ in range(t):
    m = int(data[index])
    n = int(data[index+1])
    k = int(data[index+2])
    index += 3

    cabbage_field = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    worms_needed = 0

    for _ in range(k):
        x = int(data[index])
        y = int(data[index+1])
        index += 2
        cabbage_field[y][x] = True

    for i in range(n):
        for j in range(m):
            if cabbage_field[i][j] and not visited[i][j]:
                bfs(j, i)
                worms_needed += 1

    print(worms_needed)
