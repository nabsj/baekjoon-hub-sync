from collections import deque

N = int(input())

def bfs(N):
    queue = deque([(N, 0)])  # 현재 숫자, 현재까지 연산 횟수
    visit = [False] * (N+1)
    visit[N] = True
    
    while queue:
        num, count = queue.popleft()
        
        if num == 1:
            return count
        
        # 3 나누기
        if num % 3 == 0 and not visit[num // 3]:
            visit[num // 3] = True
            queue.append((num // 3, count + 1))
        
        # 2 나누기
        if num % 2 == 0 and not visit[num // 2]:
            visit[num // 2] = True
            queue.append((num // 2, count + 1))
        
        # 1 빼기
        if num - 1 >= 1 and not visit[num - 1]:
            visit[num - 1] = True
            queue.append((num - 1, count + 1))

print(bfs(N))