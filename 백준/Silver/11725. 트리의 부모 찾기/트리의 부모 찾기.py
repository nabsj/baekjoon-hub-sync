import sys

sys.setrecursionlimit(10**6) ### 추가)런타임 에러 (RecursionError) 뜸

num = int(sys.stdin.readline().strip())

# 인접리스트 생성, 빈배열
list = [[] for _ in range(num+1)] #0~6이 아니라, 1~7이기 때문에 0번에 빈배열냅둠

for _ in range(num-1):
    input = sys.stdin.readline().strip().split()
    a = int(input[0])
    b = int(input[1])
    list[a].append(b)
    list[b].append(a)
    
#print(list)
# 각번의 인접한 정점 노드를 리스트로 넣음

#DFS 활용
visit = [-1]*(num+1)
#print(par) # 방문했는지 보는 리스트

def dfs(n):
    for i in list[n]:
        if visit[i] == -1:
            visit[i] = n
            dfs(i)

dfs(1)


for i in range(2, num+1):
    print(visit[i])