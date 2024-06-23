import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, P = map(int, input().split()) #연금수금자 수, TV채널 수, TV초기채널

graph = [[] for _ in range(M+1)]
for _ in range(N):
    u, v = map(int, input().split())
    graph[v].append(u)



def dfs(start):
    count = 0
    visited = [0] * (M+1)

    cur = start

    while True:
        if visited[cur] > 0: 
            return -1
        visited[cur] = count + 1

        if not graph[cur]: # 이동할 채널이 없으면 종료
            return count
        
        cur = graph[cur][0] # 다음 선호 채널로 이동
        count += 1


print(dfs(P))