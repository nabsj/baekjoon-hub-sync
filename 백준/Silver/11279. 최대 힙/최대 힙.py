import sys
import heapq

num = int(sys.stdin.readline().strip())

max_heap = []
result = []
    
for i in range(num):
    i = int(sys.stdin.readline().strip())
    if i == 0:
        if max_heap:
            result.append(-heapq.heappop(max_heap))  # 가장 큰값 출력 및 제거
        else:
            result.append(0)  # 비어있으면 0 출력
    else:
        heapq.heappush(max_heap, -i)  # 최대 힙만들기, 부호를 바꿔서 저장

print(*result, sep='\n')