from collections import deque

n, k = map(int, input().split())

min_time = [0] * 100001
count_ways = [0] * 100001
visited = [False] * 100001

def bfs():
    queue = deque([n])
    min_time[n] = 0
    count_ways[n] = 1
    visited[n] = True

    while queue:
        x = queue.popleft()

        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000:
                if not visited[i]:
                    visited[i] = True
                    min_time[i] = min_time[x] + 1
                    count_ways[i] = count_ways[x]
                    queue.append(i)
                elif min_time[i] == min_time[x] + 1:
                    count_ways[i] += count_ways[x]

bfs()

print(min_time[k])
print(count_ways[k])