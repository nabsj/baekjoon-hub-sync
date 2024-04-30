import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split()) # M가로 N세로

grid = []

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)
    for j in range(M):
        if row[j] == 2:
            target = (i, j)
#입력끝

def bfs(start, grid):
    n, m = len(grid), len(grid[0]) #n은 높이, m은 너비
    directions = [(-1, 0), (1, 0), (0,-1), (0, 1)] #상 하 좌 우 #방향
    queue = deque([start]) # 목적지 설정
    #print(queue)
    
    distances = [[-1] * m for _ in range(n)]  # 초기값은 -1
    distances[start[0]][start[1]] = 0  # 시작점의 0
    #print(distances)

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy #nx, ny는 방향까지 추가했을때
            if (0 <= nx < n) and (0 <= ny < m) and (grid[nx][ny] == 1) and (distances[nx][ny] == -1):
                #1. nx, ny가 그리드 안에 있는지
                #2. (원본)grid에 이동이 가능한 좌표인지, 0인 경우엔 갈수 없음
                #3. (목표까지거리)distance 아직 방분하지 않은 곳인지
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    
    # 갈 수 없는 땅 위치는 0으로 처리
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                distances[i][j] = 0

    return distances


distances = bfs(target, grid)

for line in distances:
    print(' '.join(map(str, line)))