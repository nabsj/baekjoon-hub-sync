import sys
import heapq

input = sys.stdin.read
data = input().split()
N = int(data[0])
operations = map(int, data[1:])

min_heap = []
results = []

for op in operations:
    if op == 0:
        if min_heap:
            results.append(heapq.heappop(min_heap))
        else:
            results.append(0)
    else:
        heapq.heappush(min_heap, op)

for result in results:
    print(result)
