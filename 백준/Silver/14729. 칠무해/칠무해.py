import sys
import heapq

min_heap = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    num = float(sys.stdin.readline().strip())
    heapq.heappush(min_heap, -num)
    if len(min_heap) > 7:
        heapq.heappop(min_heap)

sorted_lst = sorted(min_heap, reverse=True)

for i in sorted_lst:
    print('{:.3f}'.format(-i))


'''
import sys
import heapq

input = sys.stdin.read().split()

N = int(input[0])

min_heap = []

for i in map(float, input[1:N+1]):
    heapq.heappush(min_heap, -i) # -의 크기차이, min으로 정렬
    if len(min_heap) > 7:
        heapq.heappop(min_heap)

sorted_list = sorted(min_heap, reverse=True)

for o in sorted_list:
    print('{:.3f}'.format(-o)) #다시 올바르게
'''

'''
import sys
from collections import deque

input = sys.stdin.read().split()

lst = sorted(deque(map(float, input[1:int(input[0]) + 1])))
for i in lst[:7]:
    print('{:.3f}'.format(i))
'''