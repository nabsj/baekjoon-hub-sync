from collections import deque
import math
import sys

input = sys.stdin.read().split()

v, m = int(input[0]), int(input[1])
xs, ys = float(input[2]), float(input[3])
xt, yt = float(input[4]), float(input[5])

bnkrs = [(xs, ys), (xt, yt)]

for i in range(6, len(input), 2):
    bnkrs.append((float(input[i]), float(input[i+1])))

max_d = v * m * 60  # 최대 이동 가능 거리
start = 0
goal = 1

def func_dis(x1, y1, x2, y2, d):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) <= d

def bfs(s, g, nodes, d):
    q = deque([(s, 0)])
    visited = set()
    visited.add(s)
    
    while q:
        c, h = q.popleft()
        
        if c == g:
            return h - 1
        
        for n in range(len(nodes)):
            if n not in visited and func_dis(nodes[c][0], nodes[c][1], nodes[n][0], nodes[n][1], d):
                visited.add(n)
                q.append((n, h + 1))
    
    return -1

res = bfs(start, goal, bnkrs, max_d)

if res >= 0:
    print(f"Yes, visiting {res} other holes.")
else:
    print("No.")
